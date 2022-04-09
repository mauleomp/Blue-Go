from Server import app
from flask import render_template, request, url_for, redirect
from Server.script import valid_login, matchPass, registerNewUser, errorMessage


# new changes
@app.route('/')
def homePage():  # put application's code here
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
    return render_template('login.html', error=error)


@app.route('/signUp', methods=['POST', 'GET'])
def signUp():
    if request.method == 'POST':
        if matchPass(request.form['pass'], request.form['pass2']):
            registerNewUser(request.form['email'], request.form['username'],
                            request.form['pass'])
            return redirect(url_for('teacher'))
        else:
            return errorMessage("Passwords do not match.")
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

# Potentially temporary
@app.route('/play2')
def playPage2(usr=None):
    return render_template('InitializeGame.html')


@app.route('/teacher')
def teacher(usr=None):
    return render_template('TeacherSide.html')

@app.route('/groups/class')
def classroom(usr=None):
    return render_template('class.html')

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

@app.route('/leaderboard/isCorrect', methods=['GET'])
def isCorrect(usr=None):
    # return '{"iscorrect": false, "nextname":"Bas"}';
    return '{"iscorrect": true, "nextname":"Bas"}';

@app.route('/leaderboard/ranking', methods=['GET'])
def ranking(usr=None):
    return  '{"totalpoints": 100, "ranking": [{"name": "Fatima", "points": 75, "pointsdifference": 10},{"name": "Bas", "points": 60, "pointsdifference": 5},{"name": "Judith", "points": 60, "pointsdifference": -10}]}';

@app.route('/help')
def help(usr=None):
    return render_template('Help&Contact.html')
