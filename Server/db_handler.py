import psycopg2
from db_config import config


# conn = psycopg2.connect("dbname=BlueApp user=pi password=BlueAndGo")


def connect():
    """ Connect to the PostgreSQL database server """

    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def newStudent(s_name, s_lastname, s_number, points):
    connect('PREPARE newStudent(text, text, text, text) AS INSERT INTO students VALUES($1, $2, $3, $4); EXECUTE newStudent('+s_name+', '+s_lastname+', '+s_number+', '+points +');')


def newTeacher(t_name, t_lastname, t_email, t_password):
    connect(
        f'PREPARE newTeacher(text, text, text, text) AS INSERT INTO teachers VALUES($1, $2, $3, $4); EXECUTE newTeacher('+t_name+', '+t_lastname+', '+t_email+', '+t_password +');')


def newCourse(c_code, c_name, s_set, ranking):
    connect(
        f'PREPARE newCourse(text, text, text, integer) AS INSERT INTO courses AS($1, $2, $3, $4); EXECUTE newCourse('+c_code+', '+c_name+', '+s_set+', '+ranking +');')


def newTeam(team_name, t_students, t_ranking, last_score):
    connect(
        f'PREPARE newTeam(text, text, integer, integer) AS INSERT INTO teams AS($1, $2, $3, $4); EXECUTE newTeam('+team_name+', '+t_students+', '+t_ranking+', '+last_score +');')


def newScore(date, score):
    connect(f'PREPARE newScore(text, integer) AS INSERT INTO scores AS($1, $2); EXECUTE newScore('+date+', '+score+');')


def deleteStudent(sid):
    connect(f'DELETE FROM students WHERE st_id = ' + sid + ';')


def deleteTeacher(tid):
    connect('DELETE FROM teachers WHERE t_id = ' + tid + ';')


def deleteCourse(cid):
    connect(f'DELETE FROM courses WHERE c_id = ' + cid + ';')


def deleteTeam(teamid, cid):
    connect('DELETE FROM teams WHERE team_id = ' + teamid + ' AND c_id = ' + cid + ';')


def deleteScore(scid, teamid):
    connect('DELETE FROM scores WHERE score_id = ' + scid + ' AND team_id = ' + teamid + ';')


def updateStudent(sname, slastname, snumber, spoints, sid, change: int):
    if change == 1:
        connect('UPDATE students SET s_name = ' + sname + ' WHERE st_id = ' + sid + ';')
    elif change == 2:
        connect('UPDATE students SET s_lastname = ' + slastname + ' WHERE st_id = ' + sid + ';')
    elif change == 3:
        connect('UPDATE students SET s_number = ' + snumber + ' WHERE st_id = ' + sid + ';')
    elif change == 4:
        connect('UPDATE students SET points = ' + spoints + ' WHERE st_id = ' + sid + ';')
    else:
        connect('UPDATE students SET s_name = ' + sname + ', s_lastname = ' + slastname + ', s_number = '
                + snumber + ', points = ' + spoints + ' WHERE st_id = ' + sid + ';')


def updateTeacher(tname, tlastname, temail, tpassword, tid, change: int):
    if change == 1:
        connect('UPDATE teachers SET t_name = ' + tname + ' WHERE t_id = ' + tid + ';')
    elif change == 2:
        connect('UPDATE teachers SET t_lastname = ' + tlastname + ' WHERE t_id = ' + tid + ';')
    elif change == 3:
        connect('UPDATE teachers SET t_email = ' + temail + ' WHERE t_id = ' + tid + ';')
    elif change == 4:
        connect('UPDATE teachers SET t_password = ' + tpassword + ' WHERE t_id = ' + tid + ';')
    else:
        connect('UPDATE teachers SET t_name = ' + tname + ', t_lastname = ' + tlastname + ', t_email = '
                + temail + ', t_password = ' + tpassword + ' WHERE t_id = ' + tid + ';')


def updateCourses(ccode, cname, sset, ranking, cid, tid, change):
    if change == 1:
        connect('UPDATE courses SET course_code = ' + ccode + ' WHERE t_id = ' + tid + ' AND c_id = ' + cid + ';')
    elif change == 2:
        connect('UPDATE courses SET course_name = ' + cname + ' WHERE t_id = ' + tid + ' AND c_id = ' + cid + ';')
    elif change == 3:
        connect('UPDATE courses SET students_set = ' + sset + ' WHERE t_id = ' + tid + ' AND c_id = ' + cid + ';')
    elif change == 4:
        connect('UPDATE courses SET ranking = ' + ranking + ' WHERE t_id = ' + tid + ' AND c_id = ' + cid + ';')
    else:
        connect('UPDATE courses SET course_code = ' + ccode + ', course_name = ' + cname + ', students_set = '
                + sset + ', ranking = ' + ranking + ' WHERE t_id = ' + tid + ' AND c_id = ' + cid + ';')

def updateTeams(tm_name, tstudents, ranking, lscore, cid, teamid, change):
    if change == 1:
        connect('UPDATE teams SET team_name = ' + tm_name + ' WHERE team_id = ' + teamid + ' AND c_id = ' + cid + ';')
    elif change == 2:
        connect('UPDATE teams SET t_students = ' + tstudents + ' WHERE team_id = ' + teamid + ' AND c_id = ' + cid + ';')
    elif change == 3:
        connect('UPDATE teams SET ranking = ' + ranking + ' WHERE team_id = ' + teamid + ' AND c_id = ' + cid + ';')
    elif change == 4:
        connect('UPDATE teams SET last_score = ' + lscore + ' WHERE team_id = ' + teamid + ' AND c_id = ' + cid + ';')
    else:
        connect('UPDATE teams SET team_name = ' + tm_name + ', t_students = ' + tstudents + ', ranking = '
                + ranking + ', last_score = ' + lscore + ' WHERE t_id = ' + tid + ' AND c_id = ' + cid + ';')

def updateScores(date, score, teamid, scid, change):
    if change == 1:
        connect('UPDATE scores SET date = ' + date + ' WHERE team_id = ' + teamid + ' AND score_id = ' + scid + ';')
    elif change == 2:
        connect('UPDATE scores SET score = ' + score + ' WHERE team_id = ' + teamid + ' AND c_id = ' + cid + ';')
    else:
        connect('UPDATE scores SET date = ' + date + ', score = ' + score + ' WHERE team_id = ' + teamid + ' AND score_id = ' + scid + ';')


def fetchStudents():
    connect('SELECT * FROM students;')


def fetchTeachers():
    connect('SELECT * FROM teachers;')


def fetchCourses():
    connect('SELECT * FROM courses;')


def fetchTeams():
    connect('SELECT * FROM teams;')


def fetchScores():
    connect('SELECT * FROM scores;')


def fetchStudent(sid):
    connect('SELECT * FROM students WHERE st_id = ' + sid + ';')


def fetchTeachers(tid):
    connect('SELECT * FROM teachers WHERE t_id = ' + tid + ';')


def fetchCourse(cid):
    connect('SELECT * FROM courses WHERE c_id = ' + cid + ';')


def fetchTeam(teamid):
    connect('SELECT * FROM teams WHERE team_id = ' + teamid + ';')


def fetchScore(scid):
    connect('SELECT * FROM scores WHERE score_id = ' + scid + ';')
