import json
from Server.db_handler import signup, checkLoginWithUser, checkLoginWithEmail, getCoursesNames \
    , getStudentsFromCourseCode, getStudentRanking, getTeamRanking, updateCourseNameDB, setToFavouriteDB \
    , unsetToFavouriteDB, deleteCourseDB, updateStudentDetailsFromCourseDB, deleteStudentFromCourseDB \
    , createStudentToCourseDB, createGame, startGame, changeState, isQuestionDone, isQuestionDone,getBuzzers \
    , signalCorrectAnswer, signalIncorrectAnswer, signalNextQuestion, signalEndGame


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
        y = {"name": str(x[0]), "code": str(x[1]), "img": str(images_set[index]), "favorite": str(x[2])}
        temp['courses'].append(y)
        index = index + 1

    json.dumps(temp, sort_keys=True, indent=4)
    return temp


def submitNewCourseS(course_name, favorite, photo, cvs_file):
    s_names = []
    s_lastname = []
    s_number = []
    s_points = []

    print("Incoming CVS file. processing.")
    print(cvs_file)
    with open(cvs_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                s_names.append(row[0])
                s_lastname.append(row[0])
                s_number.append(row[0])
                s_points.append(row[0])

                line_count += 1
        print(f'Processed {line_count} lines.')

    students = [s_names, s_lastname, s_number, s_points]

    response = submitNewCourseDB(course_name, favorite, photo, students)

    if response != "-1":
        return confirmationMessage("Course name \'" + course_name + "\' with course code \'"
                                   + course_code + "\' was updated successfully.")
    else:
        return errorMessage("Course name could not be changed.")


def updateCourseNameS(course_code, course_name):
    response = updateCourseNameDB(course_code, course_name)

    if response != "-1":
        return confirmationMessage("Course name \'" + course_name + "\' with course code \'"
                                   + course_code + "\' was updated successfully.")
    else:
        return errorMessage("Course name could not be changed.")


def setToFavouriteS(course_code):
    response = setToFavouriteDB(course_code)

    if response != "-1":
        return confirmationMessage("Course name \'" + response + "\' with course code \'"
                                   + course_code + "\' was set to favourite.")
    else:
        return errorMessage("Course name could not be set to favourite.")


def unsetToFavouriteS(course_code):
    response = unsetToFavouriteDB(course_code)

    if response != "-1":
        return confirmationMessage("Course name \'" + response + "\' with course code \'"
                                   + course_code + "\' was unset to favourite.")
    else:
        return errorMessage("Course name could not be unset to favourite.")


def deleteCourseS(course_code):
    response = deleteCourseDB(course_code)

    if response != "-1":
        return confirmationMessage("Course name \'" + response + "\' with course code \'"
                                   + course_code + "\' was deleted successfully.")
    else:
        return errorMessage("Course name could not be deleted.")


def updateStudentDetailsFromCourseS(course_code, s_number, s_name, s_lastname, t_teams):
    response = updateStudentDetailsFromCourseDB(course_code, s_number, s_name, s_lastname, t_teams)

    if response != "-1":
        return confirmationMessage("Student \'" + s_name + " " + s_lastname + "\' in course \'"
                                   + course_code + "\' was updated successfully.")
    else:
        return errorMessage("This student could not be updated.")


def createStudentToCourseS(course_code, s_number, s_name, s_lastname, t_teams):
    response = createStudentToCourseDB(course_code, s_number, s_name, s_lastname, t_teams)

    if response != "-1":
        return confirmationMessage("Student \'" + s_name + " " + s_lastname + "\' in course \'"
                                   + course_code + "\' was created successfully.")
    else:
        return errorMessage("This student could not be created.")


def deleteStudentFromCourseS(course_code, s_number):
    response = deleteStudentFromCourseDB(course_code, s_number)

    if response != "-1":
        return confirmationMessage("Student \'" + response + "\' in course \'"
                                   + course_code + "\' was deleted successfully.")
    else:
        return errorMessage("This student could not be deleted.")


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


# For testing purposes:
counter = 0


def createGameS(game_mode, conf, course_code):

    if createGame(game_mode, conf, course_code):
        return confirmationMessage("SQL transaction was submitted successfully.")
    else:
        return errorMessage("There is an error in SQL syntax.")


def startGameS():

    if startGame():
        return confirmationMessage("SQL transaction was submitted successfully.")
    else:
        return errorMessage("There is an error in SQL syntax.")


def changeStateS(state):

    if changeState(state):
        return confirmationMessage("SQL transaction was submitted successfully.")
    else:
        return errorMessage("There is an error in SQL syntax.")


def isQuestionDoneS():
    return isQuestionDone()


def getConnectedBuzzers():
    '''
    temp = {'buzzers': []}
    y = {"buzzerID": "0",
         "teamConnected": "true",
         "teamName": "Team0"}
    temp['buzzers'].append(y)

    json.dumps(temp, sort_keys=True, indent=4)
    return temp
    '''
    return getBuzzers()


def signalCorrectAnswerS():

    response = signalCorrectAnswer()

    if changeState(state):
        return confirmationMessage("SQL transaction was submitted successfully.")
    else:
        return errorMessage("There is an error in SQL syntax.")


def signalIncorrectAnswerS():
    response = signalIncorrectAnswer()

    if changeState(state):
        return confirmationMessage("SQL transaction was submitted successfully.")
    else:
        return errorMessage("There is an error in SQL syntax.")


def signalNextQuestionS():
    response = signalNextQuestion()

    if changeState(state):
        return confirmationMessage("SQL transaction was submitted successfully.")
    else:
        return errorMessage("There is an error in SQL syntax.")


def signalEndGameS():
    response = signalEndGame()

    if changeState(state):
        return confirmationMessage("SQL transaction was submitted successfully.")
    else:
        return errorMessage("There is an error in SQL syntax.")