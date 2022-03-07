from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

app.secret_key = "AFr_256897/@"

@app.route('/')
def homePage():  # put application's code here
    return render_template('MainPage.html')


@app.route('/login', methods=['POST', 'GET'])
def loginPage():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['email'], request.form['pass']):
            usr = request.form['email']
            session['user'] = user
            return redirect(url_for('logTeacher'))
        else:
            error = 'Invalid username / password '

    return render_template('login.html', error=error)


@app.route('/signUp', methods = ['POST', 'GET'])
def signUp():
    error = None
    if request.method == 'POST':
        if matchPasswords(request.form['pass'], request.form['pass2']):
            return register(request.form['email'], request.form['username'],
                            request.form['pass'])
        else:
            error = 'Passwords do not match'
    elif request.method == 'GET':
        print('sign')
    return render_template('SignUp.html')


## create it and validate with the user and passwword from the data base
##def valid_login(email, password):

#log the user in using the email.
@app.route('/teacher', methods=['POST', 'GET'])
def logTeacher():
    if 'user' in session:
        usr = session['user']
        return render_template("####")
    else:
        return redirect(url_for("loginPage"))

#compare if the passwords match
#matchPass(ps1, ps2):

#register the user within the database
#register(email, username, password)
'''
@app.route('/user', methods=['POST, GET'])
def logTeacher():'''


if __name__ == '__main__':
    app.run(debug=True)
