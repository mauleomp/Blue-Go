import psycopg2
import os
from configparser import ConfigParser


def connect(sentence, task):
    conn = None
    db_version = None
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

        # display the PostgreSQL database server version
        if task:
            db_version = cur.fetchone()
        else:
            conn.commit()
            db_version = cur.rowcount
        # close the communication with the PostgreSQL

    except Exception as err:
        print(err)
    finally:
        cur.close()
        if conn is not None:
            conn.close()

    return db_version


def updateGame(game, state, started, mode, conf, ranking, turn, anon, finish, correct, change):
    if change == 1:
        return connect('UPDATE game SET has_started = ' + started + ' WHERE n_game = ' + game + ';', False)
    elif change == 2:
        return connect('UPDATE game SET state = ' + state + ' WHERE n_game = ' + game + ';', False)
    elif change == 3:
        return connect('UPDATE game SET game_mode = ' + mode + ' WHERE n_game = ' + game + ';', False)
    elif change == 4:
        return connect('UPDATE game SET conf = ' + conf + ' WHERE n_game = ' + game + ';', False)
    elif change == 5:
        return connect('UPDATE game SET ranking = ' + ranking + ' WHERE n_game = ' + game + ';', False)
    elif change == 6:
        return connect('UPDATE game SET turn = ' + turn + ' WHERE n_game = ' + game + ';', False)
    elif change == 7:
        return connect('UPDATE game SET isAnon = ' + anon + ' WHERE n_game = ' + game + ';', False)
    elif change == 8:
        return connect('UPDATE game SET has_finished = ' + finish + ' WHERE n_game = ' + game + ';', False)
    elif change == 9:
        return connect('UPDATE game SET correct = ' + correct + ' WHERE n_game = ' + game + ';', False)


def fetchGame(game):
    return connect('SELECT game_mode, conf FROM game WHERE n_game = ' + game + ';', True)


def fetchState(game):
    return connect('SELECT state FROM game WHERE n_game = ' + game + ';', True)


def fetchStart(game):
    return connect('SELECT has_started FROM game WHERE n_game = ' + game + ';', True)


def fetchTurn(game):
    return connect('SELECT turn, correct, state FROM game WHERE n_game = ' + game + ';', True)


def fetchFinish(game):
    return connect('SELECT has_finished FROM game WHERE n_game = ' + game + ';', True)


def updateState(game, state):
    return connect('UPDATE game SET state = ' + state + ' WHERE n_game = ' + game + ';, False')


def updateRanking(game, ranking):
    return connect('UPDATE game SET ranking = ' + ranking + ' WHERE n_game = ' + game + ';', False)


def updateTurn(game, turn):
    return connect('UPDATE game SET turn = ' + turn + ' WHERE n_game = ' + game + ';', False)


def updateFinish(game, finish):
    return connect('UPDATE game SET has_finished = ' + finish + ' WHERE n_game = ' + game + ';', False)


def updateCorrect(game, correct):
    return connect('UPDATE game SET correct = ' + correct + ' WHERE n_game = ' + game + ';', False)
