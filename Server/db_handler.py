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

def newTeacher(t_name, t_lastname, t_email, t_password):
    connect(f'PREPARE newTeacher(text, text, text, text) AS INSERT INTO teachers VALUES($1, $2, $3, $4); EXECUTE newTeacher({t_name}, {t_lastname}, {t_email}, {t_password});')

def newCourse(c_code, c_name, s_set, ranking):
    connect(f'PREPARE newCourse(text, text, text, integer) AS INSERT INTO courses AS($1, $2, $3, $4); EXECUTE newCourse({c_code}, {c_name}, {s_set}, {ranking});')

def newTeam(team_name, t_students, t_ranking, last_score):
    connect(f'PREPARE newTeam(text, text, integer, integer) AS INSERT INTO teams AS($1, $2, $3, $4); EXECUTE newTeam({team_name}, {t_students}, {t_ranking}, {last_score});')

def newScore(date, score):
    connect(f'PREPARE newScore(text, integer) AS INSERT INTO scores AS($1, $2); EXECUTE newScore({date}, {score});')
