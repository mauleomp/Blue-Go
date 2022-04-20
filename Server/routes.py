from Server import app
from flask import render_template, request, url_for, redirect
from Server.script import valid_login, matchPass, registerNewUser, errorMessage, connectDB, confirmationMessage \
    , getAllCourses, getStudentsC, getStudentsRank, getTeamsRank, getConnectedBuzzers, updateCourseNameS \
    , setToFavouriteS, unsetToFavouriteS, deleteCourseS, updateStudentDetailsFromCourseS, deleteStudentFromCourseS \
    , createStudentToCourseS, createGameS, startGameS, isQuestionDoneS

# from Server.BLEserver import initiateGame, startQuestion, finishGame


# new changes
@app.route('/')
def homePage():  # put application's code here
    # connectDB()
    return render_template('MainPage.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        # modify valid login within the db
        if valid_login(request.form['email'], request.form['pass']):
            usr = request.form['email']
            return render_template('TeacherSide.html', error=error)
        else:
            error = 'Invalid username / password'
            return render_template('login.html', error=error)
    return render_template('login.html')


@app.route('/signUp', methods=['GET'])
def signUp():
    return render_template('SignUp.html')


@app.route('/signUp/registerUser', methods=['POST'])
def registerNewUserS():
    if matchPass(request.form['pass'], request.form['pass2']):
        response = registerNewUser(request.form['email'],
                                   request.form['username'],
                                   request.form['pass'])

        if response:
            return confirmationMessage('Thank you for registering! User was registered correctly.')

        else:
            return confirmationMessage('User could not be registered. Please try again.')

    else:
        return errorMessage('Passwords do not match. Please try again.')


# log the user in using the email.
@app.route('/login', methods=['POST', 'GET'])
def logTeacher():
    if 'user' in session:
        usr = session['user']
        return render_template("####")
    else:
        return redirect(url_for("loginPage"))


# Returns all the courses.
@app.route('/courses/getAllCourses', methods=['GET'])
def getCoursesAll():
    """
        Returns a JSON object with this format:

        { courses: [ {"code": 00000, "name": Course1},
                     {"code": 00001, "name": Course2},
                     ....  ]
        }

    """
    return getAllCourses()


@app.route('/courses/setToFavorite', methods=['POST'])
def setToFavouriteR():
    course_code = request.form['course_code']

    return setToFavouriteS(course_code)


@app.route('/courses/unsetToFavorite', methods=['POST'])
def unsetToFavouriteR():
    course_code = request.form['course_code']

    return unsetToFavouriteS(course_code)


@app.route('/courses/deleteCourse', methods=['POST'])
def deleteCourseR():
    course_code = request.form['course_code']

    return deleteCourseS(course_code)


# Returns all the courses.
@app.route('/courses/class/<course_code>/getStudents', methods=['GET'])
def getStudentsFromCourse(course_code):
    """
        Returns a JSON object with this format:

        { students: [ {s_lastname": Otto, s_name: "Mark", s_number: "s2356546", t_teams: "Team1"},
                      {s_lastname": Watson, s_name: "Mary", s_number: "s2257547", t_teams: "Team2"},
                    ....  ]
        }

    """
    return getStudentsC(course_code)


@app.route('/courses/class/<course_code>/updateStudentDetails', methods=['POST'])
def updateStudentDetailsFromCourseR(course_code):

    s_number = request.form['s_number']
    s_name = request.form['s_name']
    s_lastname = request.form['s_lastname']
    t_teams = request.form['t_teams']

    return updateStudentDetailsFromCourseS(course_code, s_number, s_name, s_lastname, t_teams)


@app.route('/courses/class/<course_code>/createStudent', methods=['POST'])
def createStudentToCourseR(course_code):

    s_number = request.form['s_number']
    s_name = request.form['s_name']
    s_lastname = request.form['s_lastname']
    t_teams = request.form['t_teams']

    return createStudentToCourseS(course_code, s_number, s_name, s_lastname, t_teams)


@app.route('/courses/class/<course_code>/createRandomTeam', methods=['POST'])
def createRandomTeamR(course_code):
    students_number = request.form['students_number']

    # TODO: implement this function

    return errorMessage("There is no method to implement this function for " + students_number + " students.")


@app.route('/courses/class/<course_code>/deleteStudent', methods=['POST'])
def deleteStudentFromCourseR(course_code):
    s_number = request.form['s_number']

    # TODO: implement this function

    return deleteStudentFromCourseS(course_code, s_number)


# Returns the student ranking from this course
@app.route('/courses/class/<course_code>/getStudentsRanking', methods=['GET'])
def getStudentsRankingC(course_code):
    return getStudentsRank(course_code)


# Returns the student ranking from this course
@app.route('/courses/class/<course_code>/getTeamsRanking', methods=['GET'])
def getTeamsRankingC(course_code):
    return getTeamsRank(course_code)


@app.route('/courses/updateCourseName', methods=['POST'])
def updateCourseNameR():
    course_code = request.form["course_code"]
    course_name = request.form["course_name"]
    return updateCourseNameS(course_code, course_name)


@app.route('/play/getAllCourses', methods=['GET'])
def getAllCoursesFromPlay():
    return getAllCourses()


@app.route('/play/save_game_preferences', methods=['POST'])
def postCourseAndGameMode():
    course_code = request.form['course_code']
    print(course_code)
    game_mode = request.form['game_mode']
    #asyncio.run(initiateGame(game_mode))
    print(game_mode)
    game_settings = request.form['game_settings']
    print(">" + str(game_settings) + "<")

    # bs12
    response = createGameS(game_mode, conf, course_code)

    return confirmationMessage("Game settings updated")


@app.route('/buzzers/getConnectedBuzzers', methods=['GET'])
def getConnectedBuzzersS():
    return getConnectedBuzzers()


@app.route('/buzzers/start_game', methods=['POST'])
def postStartGame():
    # TODO: call function startGame(game_mode)
    return confirmationMessage("Game has started properly.")
    #return startGameS()


@app.route('/leaderboard/isCorrect', methods=['GET'])
def getIsAnswerCorrectL():
    return isQuestionDoneS()
    # return '{"iscorrect": true}'
    # return '{"iscorrect": false, "nextname":"Bryan"}'


@app.route('/leaderboard/ranking', methods=['GET'])
def getRankingLeaderBoard():
    return '{"totalpoints": 100, "ranking": [{"name": "Fatima", "points": 75, "pointsdifference": 10},{"name": "Bas", "points": 60, "pointsdifference": 5},{"name": "Judith", "points": 60, "pointsdifference": -10}]}';


questionnumber = 1


@app.route('/leaderboard/status', methods=['GET'])
def getStatus(usr=None):
    global questionnumber
    return '{"questionnumber": ' + str(questionnumber) + ', "status": "waiting"}'
    # return '{"questionnumber": 1, "status": "waiting"}'
    # return '{"questionnumber": 1, "status": "nextround"}'
    # return '{"questionnumber": 1, "status": "endgame"}'


# receives: "questionnumber": questionnumber, "status": "nextround"}
# or: {"status": "endgame"}
@app.route('/leaderboard/status', methods=['POST'])
def postStatus(usr=None):
    global questionnumber
    questionnumber += 1

    # Should call this function, so the server will know that a next round of questions has started
    # it will return a JSON with a confirmation, or error, for knowing if the SQL transaction was a success or not

    # status: nextround     ==>   Server state WAITING;  the server will know that a next round of questions has started
    # status: endgame       ==>   Server state ENDGAME;  the server will know that the game has ended via the interface
    # changeStateS("WAITING")

    return 'OK'



'''
@app.route('/teacher', methods=['POST, GET'])
def logTeacher():
'''


@app.route('/courses')
def courses(usr=None):
    return render_template('Groups.html')


@app.route('/play2')
def playPage2(usr=None):
    return render_template('Play.html')


# Potentially temporary
@app.route('/play')
def playPage(usr=None):
    return render_template('InitializeGame.html')


@app.route('/teacher')
def teacher(usr=None):
    return render_template('TeacherSide.html')


@app.route('/courses/class/<course_code>')
def classroom(course_code):
    print(course_code)
    return render_template('class.html', course_code=str(course_code))


@app.route('/game')
def game(usr=None):
    return render_template('StartGame.html')


@app.route('/profile')
def profile(usr=None):
    return render_template('Settings.html')


@app.route('/buy')
def buy(usr=None):
    return render_template('Buy.html')


@app.route('/buzzers')
def buzzers(usr=None):
    return render_template('checkbuzzers.html')


@app.route('/leaderboard')
def leaderboard(usr=None):
    return render_template('leaderboard.html')

@app.route('/main2')
def main2(usr=None):
    return render_template('MainPage2.html')

@app.route('/buy2')
def buy2(usr=None):
    return render_template('Buy2.html')


@app.route('/help')
def help(usr=None):
    return render_template('Help&Contact.html')

@app.route('/test')
def test(usr=None):
    return render_template('Test.html')

@app.route('/controller')
def controller(usr=None):
    return render_template('Controller.html')
