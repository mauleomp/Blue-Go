from Server import app

from flask import render_template, request, url_for, redirect
from Server.script import valid_login, matchPass, registerNewUser, errorMessage, connectDB, confirmationMessage\
    , getAllCourses, getStudentsC, getStudentsRank, getTeamsRank


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
            return redirect(url_for('teacher'))
        else:
            error = 'Invalid username / password '
            return errorMessage(error)
    return render_template('login.html', error=error)


@app.route('/signUp', methods=['POST', 'GET'])
def signUp():
    if request.method == 'POST':
        if matchPass(request.form['pass'], request.form['pass2']):
            response = registerNewUser(request.form['email'],
                                       request.form['username'],
                                       request.form['pass'])

            if response:
                return confirmationMessage("User was registered correctly.")
            else:
                return errorMessage("User could not be registered. Please try again.")

        else:
            return errorMessage("Passwords do not match. Please try again.")
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
@app.route('/groups/getAllCourses', methods=['GET'])
def getCoursesAll():
    return getAllCourses()


# Returns all the courses.
@app.route('/groups/class/<course_code>/getStudents', methods=['GET'])
def getStudentsFromCourse(course_code):
    return getStudentsC(course_code)


# Returns the student ranking from this course
@app.route('/groups/class/<course_code>/getStudentsRanking', methods=['GET'])
def getStudentsRankingC(course_code):
    return getStudentsRank(course_code)    
# Returns the student ranking from this course


@app.route('/groups/class/<course_code>/getTeamsRanking', methods=['GET'])
def getTeamsRankingC(course_code):
    return getTeamsRank(course_code)


'''
@app.route('/teacher', methods=['POST, GET'])
def logTeacher():
'''


@app.route('/groups')
def groups(usr=None):
    return render_template('Groups.html')


@app.route('/play')
def playPage(usr=None):
    return render_template('Play.html')


@app.route('/teacher')
def teacher(usr=None):
    return render_template('TeacherSide.html')


@app.route('/groups/class/<course_code>')
def classroom(course_code):
    print(course_code)
    return render_template('class.html', course_code=str(course_code))


@app.route('/game')
def game(usr=None):
    return render_template('StartGame.html')


@app.route('/buy')
def buy(usr=None):
    return render_template('Buy.html')
