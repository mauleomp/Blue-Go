import json
# from Server.db_handler import connect

# Only for testing purposes, we have these fields
# Later on we will store any information on a DataBase

# teacher Table
t_names = ["Bryan"]
t_lastnames = ["Sanchez"]
t_usernames = ["b"]
t_emails = ["admin@admin.com"]
t_passwords = ["password"]

# Student Table
s_names = []
s_lastname = []
s_number = []
s_points = []

# Courses Table
c_course_code = []
c_course_name = []
c_students_set = []
c_ranking = []
c_teacher = []

# Teams Table
t_team_name = []
t_students = []
t_ranking = []
t_last_score = []
t_course_name = []

# Scores Table
s_team_name = []
s_date = []
s_score = []


session_open = False


def connectDB():
    print("########")
    # connect()
    print("########")


# Create and store credentials from the Sign up page
def registerNewUser(username, email, password):
    t_usernames.append(username)
    t_emails.append(email)
    t_passwords.append(password)

    print("User [" + username + "] was successfully registered.")


# create it and validate with the user and password from the data base
def valid_login(account, password):
    index = 0

    try:
        index = t_usernames.index(account)
        print("User [" + account + "] was logged in correctly.")
        return matchPass(t_passwords[index], password)
    except ValueError:
        pass

    try:
        index = t_emails.index(account)
        print("User [" + account + "] was logged in correctly.")
        return matchPass(t_passwords[index], password)
    except ValueError:
        print("User [" + account + "] was not logged in. Credentials are incorrect.")
        return False


# compare if the passwords match
def matchPass(ps1, ps2):
    return ps1 == ps2


# Create a JSON object which returns an error message
def errorMessage(message):
    temp = {'error': []}

    y = {"message": str(message)}
    temp['error'].append(y)

    json.dumps(temp, sort_keys=True, indent=4)
    return temp
