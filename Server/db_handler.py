# import psycopg2
# import os
# from Server.db_config import config

# Only for testing purposes, we have these fields
# Later on we will store any information on a DataBase

# teacher Table
t_names = ["Bryan"]
t_lastnames = ["Sanchez"]
t_usernames = ["b"]
t_emails = ["admin@admin.com"]
t_passwords = ["password"]

# Student Table
s_names = ["Mauricio", "Mark", "Jacob", "Maria"]
s_lastname = ["Merchan", "Otto", "Thornton", "Perez"]
s_number = ["s2147856", "s2356546", "s2356545", "s2356541"]
s_points = ["5", "10", "4", "7"]

# Courses Table
c_course_code = ["c123456"]
c_course_name = ["Academic Skills"]
c_students_set = ["[{\"s_name\": Mauricio}, {\"s_name\": Mark}, {\"s_name\": Jacob}, {\"s_name\": Maria}]"]
c_ranking = ["1"]
c_teacher = ["Bryan"]

# Teams Table
t_team_name = ["Team1", "Team2"]
t_students = ["[{\"s_name\": Mauricio}, {\"s_name\": Mark}]", "[{\"s_name\": Jacob}, {\"s_name\": Maria}]"]
t_ranking = ["1", "2"]
t_last_score = ["15", "11"]   # should be renamed to total_score
t_course_name = ["Academic Skills", "Academic Skills"]

# Scores Table
s_team_name = ["Team1", "Team2", "Team1", "Team2"]
s_date = ["25/03/2022", "25/03/2022", "19/03/2022", "19/03/2022"]
s_score = ["7", "5", "8", "6"]


def signup(email, username, password):
    t_usernames.append(username)
    t_emails.append(email)
    t_passwords.append(password)

    print("User [" + username + "] was successfully registered.")

    return True


def checkLoginWithUser(username, password):
    try:
        index = t_usernames.index(username)
        print("User [" + username + "] was logged in correctly.")
        return t_passwords[index] == password
    except ValueError:
        print("User [" + username + "] was not logged in. Credentials are incorrect.")
        return False


def checkLoginWithEmail(email, password):
    try:
        index = t_emails.index(email)
        print("User [" + email + "] was logged in correctly.")
        return t_passwords[index] == password
    except ValueError:
        print("User [" + email + "] was not logged in. Credentials are incorrect.")
        return False
    

def getCoursesNames():
    temp = []

    index = 0
    while index < len(c_course_name):
        item = [c_course_name[index], c_course_code[index]]
        temp.append(item)
        index += 1

    return temp


def getStudentsFromCourseCode(course_code):

    """
    try:
        index = c_course_code.index(course_code)

        result = []

        i = 0
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        while i < len(s_names):
            it = 0
            if it >= 2:
                it = 1
            item = [s_number[i], s_names[i], s_lastname[i], t_team_name[it]]
            result.append(item)
            i += 1
        print("^^^^^^^^^^^^^^^^^^^^^^^^")
        return result
    except ValueError:
        return ["-1"]

    """

    return [["s2147856", "Mauricio", "Merchan", "Team1"],
            ["s2356546", "Mark", "Otto", "Team1"],
            ["s2356545", "Jacob", "Thornton", "Team2"],
            ["s2356541", "Maria", "Perez", "Team2"]]


def getStudentRanking(course_code):

    return [["Mark", "Otto", "10"],
            ["Maria", "Perez", "7"],
            ["Mauricio", "Merchan", "5"]]


def getTeamRanking(course_code):

    return [["Team1", "15"],
            ["Team2", "11"]]


def updateCourseNameDB(course_code, course_name):
    try:
        index = c_course_code.index(course_code)

        c_course_name[index] = course_name
        return "OK"
    except ValueError:
        return "-1"


# conn = psycopg2.connect("dbname=BlueApp user=pi password=BlueAndGo")


def connect():
    """ Connect to the PostgreSQL database server """

    conn = None
    try:
        # read connection parameters
        #BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        #print(BASE_DIR)
        #params = config(filename=BASE_DIR + '/Server/database.ini', section='postgresql')
        # params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        #conn = psycopg2.connect(**params)

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
    except (Exception) as error: #, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
         

# This method will update the database            
def update(sentence):
    conn = None
    try:
        # read the connection parameters
        parser = ConfigParser()
        parser.read('database.ini')
        db = {}
        if parser.has_section('postgresql'):
            params = parser.items('postgresql')
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format('postgresql', 'database.ini'))

        print("trying to connect with the Data Base")
        conn = psycopg2.connect(**db)

        # creating the cursor
        cur = conn.cursor()

        # execute a statement
        cur.execute(sentence)
        conn.commit()
        cur.rowcount
        # close the communication with the PostgreSQL
    except Exception as err:
        print(err)
    finally:
        cur.close()
        if conn is not None:
            conn.close()



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


def updateTeams(tm_name, tstudents, ranking, lscore, cid, teamid, change, tid):
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


def updateScores(date, score, teamid, scid, cid, change):
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
    

# ----------------------- METHODS FOR GAME IN DATABASE ------------------------

# it is TRUE or FALSE
def updateStart(start):
    return update('UPDATE game SET start = '+start+' WHERE n_game = \'1\';')


def updateState(state):
    return update('UPDATE game SET state = \''+state+'\' WHERE n_game = \'1\';')


# conf es una string como antes('10;10;10;10')
def updateConf(game_mode, conf):
    return update('UPDATE game SET game_mode = \''+game_mode+'\', conf = \''+conf+'\' WHERE n_game = \'1\';')


# TRUE or FALSE
def updateAnon(anon):
    return update('UPDATE game SET isanon = '+anon+' WHERE n_game = \'1\';')


# TRUE or FALSE
def updateFinished(finish):
    return update('UPDATE game SET has_finished = '+finish+' WHERE n_game = \'1\';')


'''
the posibilities are:
"correct" -> to validate an asnwer
"wrong" -> to say that answer is wrong
"no answer" -> if you change of question(new question) set it to no answer
'''
def updateCorrect(question):
    return update('UPDATE game SET correct = \''+question+'\' WHERE n_game = \'1\';')


def fetchRank():
    return update('SELECT ranking FROM game WHERE n_game = \'1\';')


def fetchState():
    return update('SELECT state FROM game WHERE n_game = \'1\';')


def fetchState():
    return update('SELECT state FROM turn WHERE n_game = \'1\';')
