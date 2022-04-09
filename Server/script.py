import json
from Server.db_handler import signup, checkLoginWithUser, checkLoginWithEmail, getCoursesNames \
    , getStudentsFromCourseCode, getStudentRanking, getTeamRanking

session_open = False
images_set = ["https://images.unsplash.com/photo-1639815189096-f75717eaecfe?ixlib=rb-1.2.1&ixid"
              "=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1632&q=80",
              "https://images.unsplash.com/photo-1642698166111-1e736132b0ee?ixlib=rb-1.2.1&ixid"
              "=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1632&q=80",
              "https://images.unsplash.com/photo-1627637819848-7074cb1565e8?ixlib=rb-1.2.1&ixid"
              "=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1632&q=80",
              "https://images.unsplash.com/photo-1639815189096-f75717eaecfe?ixlib=rb-1.2.1&ixid"
              "=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1632&q=80",
              "https://images.unsplash.com/photo-1639815189096-f75717eaecfe?ixlib=rb-1.2.1&ixid"
              "=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1632&q=80"]


def connectDB():
    print("########")
    # connect()
    print("########")


# Create and store credentials from the Sign up page
def registerNewUser(username, email, password):
    # Calls
    return signup(email, username, password)


# create it and validate with the user and password from the data base
def valid_login(account, password):
    response = checkLoginWithUser(account, password)

    if response:
        return response
    else:
        return checkLoginWithEmail(account, password)


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


# Create a JSON object which returns an confirmation message
def confirmationMessage(message):
    temp = {'confirmation': []}

    y = {"message": str(message)}
    temp['confirmation'].append(y)

    json.dumps(temp, sort_keys=True, indent=4)
    return temp


def getAllCourses():
    courses = getCoursesNames()

    temp = {'courses': []}
    index = 0
    for x in courses:
        if index >= len(images_set):
            index = 0
        y = {"name": str(x[0]), "code": str(x[1]), "img": str(images_set[index])}
        temp['courses'].append(y)
        index = index + 1

    json.dumps(temp, sort_keys=True, indent=4)
    return temp


def getStudentsC(course_code):
    students = getStudentsFromCourseCode(course_code)

    if students[0] == -1:
        return errorMessage("Course not found.")
    else:
        temp = {'students': []}
        for x in students:
            y = {"s_number": str(x[0]),
                 "s_name": str(x[1]),
                 "s_lastname": str(x[2]),
                 "t_teams": str(x[3])}
            temp['students'].append(y)

        json.dumps(temp, sort_keys=True, indent=4)
        return temp


def getStudentsRank(course_code):
    ranking = getStudentRanking(course_code)

    temp = {'s_ranking': []}
    for x in ranking:
        y = {"s_name": str(x[0]),
             "s_lastname": str(x[1]),
             "s_rank": str(x[2])}
        
        temp['s_ranking'].append(y)

    json.dumps(temp, sort_keys=True, indent=4)
    return temp


def getTeamsRank(course_code):
    ranking = getTeamRanking(course_code)

    temp = {'c_ranking': []}
    for x in ranking:
        y = {"c_name": str(x[0]),
             "c_rank": str(x[1])}

        temp['c_ranking'].append(y)

    json.dumps(temp, sort_keys=True, indent=4)
    return temp
