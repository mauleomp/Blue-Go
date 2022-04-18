from Server import app
from flask import render_template, request, url_for, redirect
from Server.script import valid_login, matchPass, registerNewUser, errorMessage, connectDB, confirmationMessage \
    , getAllCourses, getStudentsC, getStudentsRank, getTeamsRank, getConnectedBuzzers, updateCourseNameS
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


@app.route('/signUp', methods=['POST', 'GET'])
def signUp():
    if request.method == 'POST':
        if matchPass(request.form['pass'], request.form['pass2']):
            response = registerNewUser(request.form['email'],
                                       request.form['username'],
                                       request.form['pass'])

            if response:
                message = 'Thank you for registering! User was registered correctly.'
                return render_template('SignUp.html', message=message)
            else:
                message = 'User could not be registered. Please try again.'
                return render_template('SignUp.html', message=message)

        else:
            message = 'Passwords do not match. Please try again.'
            return render_template('SignUp.html', message=message)
    elif request.method == 'GET':
        print('sign')
    return render_template('SignUp.html')


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
    print(game_settings)

    # TODO: check the values, and return a response

    return confirmationMessage("Game settings updated")


@app.route('/buzzers/getConnectedBuzzers', methods=['GET'])
def getConnectedBuzzersS():
    return getConnectedBuzzers()


@app.route('/buzzers/start_game', methods=['POST'])
def postStartGame():
    # TODO: call function startGame(game_mode)
    return confirmationMessage("Game has started properly.")


@app.route('/leaderboard/isAnswerCorrect', methods=['GET'])
def getIsAnswerCorrectL():
    return '{"iscorrect": true, "nextname":"Bas"}'


@app.route('/leaderboard/getRanking', methods=['GET'])
def getRankingLeaderBoard():
    return '{"totalpoints": 100, "ranking": [{"name": "Fatima", "points": 75, "pointsdifference": 10},{"name": "Bas", "points": 60, "pointsdifference": 5},{"name": "Judith", "points": 60, "pointsdifference": -10}]}';


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
