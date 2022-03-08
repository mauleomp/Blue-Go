from flask import Flask, render_template, request, url_for, redirect



app = Flask(__name__)

app.secret_key = "AFr_256897/@"
## new changes
@app.route('/')
def homePage():  # put application's code here
    return render_template('MainPage.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        #modify valid login within the db
        if valid_login(request.form['email'], request.form['pass']):
            usr = request.form['email']
            #session['user'] = usr
            print(usr)
            return redirect(url_for('teacher'))
        else:
            error = 'Invalid username / password '
    return render_template('login.html', error=error)


@app.route('/signUp', methods=['POST', 'GET'])
def signUp():
    error = None
    if request.method == 'POST':
        if matchPass(request.form['pass'], request.form['pass2']):
            register(request.form['email'], request.form['username'],
                     request.form['pass'])
            return redirect(url_for('teacher'))
        else:
            error = 'Passwords do not match'
    elif request.method == 'GET':
        print('sign')
    return render_template('SignUp.html')


## create it and validate with the user and passwword from the data base
def valid_login(email, password):
    return True

#log the user in using the email.
@app.route('/login', methods=['POST', 'GET'])
def logTeacher():
    if 'user' in session:
        usr = session['user']
        return render_template("####")
    else:
        return redirect(url_for("loginPage"))

#compare if the passwords match
def matchPass(ps1, ps2):
    return True

#register the user within the database
def register(email, username, password):
    print(email, username, password)

'''
@app.route('/teacher', methods=['POST, GET'])
def logTeacher():'''


@app.route('/groups')
def groups(usr=None):
    return render_template('Groups.html')

@app.route('/play')
def playPage(usr=None):
    return render_template('Play.html')

@app.route('/teacher')
def teacher(usr=None):
    return render_template('TeacherSide.html')


if __name__ == '__main__':
    app.run(debug=True)
