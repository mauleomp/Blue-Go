#from _tkinter import Tk
from enum import Enum
import random
'''
MODES:

- FAST
- RANDOM
- RLIVES
- FLIVES
'''

class Game:

    # mode: is the mode of the game that could be NORMAL,RANDOM, LIFETIMES
    # buzzers: list of buzzers, clients of the game


    def __init__(self, mode, teams, conf: list = None):
        # --------SETTINGS OF THE GAME ----------------
        self.plus_points: int = 10
        self.rest_points: int = 5
        self.time: int = 10
        self.lives: int = 10
        self.st = None

        # -------- ATRIBUTES OF THE GAME ----------------
        self.ranking = list()
        self.mode = mode
        self.buzzers = dict()
        self.queue = list()
        self.sate: State = State.CONNECTING
        self.turn = None
        self.teams = teams
        self.anonymous = False

        # -------- MANAGE ACCORDING THE SETTINGS  ------------
        if teams is None:
            self.anonymous = True
        if conf is not None:
            self.plus_points = conf[0]
            self.rest_points = conf[1]
            if mode == "RANDOM":
                self.time = conf[2]
            elif mode == "LIVES":
                self.time = conf[2]
                self.lives = conf[3]

    # ----------------- GET PROPERTIES OF THE GAME --------------------
    @property
    def getMode(self):
        return self.mode

    @property
    def getBuzzers(self):
        return self.buzzers

    @property
    def getQueue(self):
        return self.queue

    @property
    def getSate(self):
        return self.sate

    @property
    def getRanking(self):
        return self.ranking

    @property
    def getTurn(self):
        return self.turn

    @property
    def isAnon(self):
        return self.anonymous

    @property
    def getTeams(self):
        return self.teams

    @property
    def getPoints(self):
        return self.plus_points

    @property
    def getRestPoints(self):
        return self.rest_points

    @property
    def getSt(self):
        return self.st

    def setSt(self, time):
        #root = Tk()
        self.st = time
        #root.after(self.time*100, self.toVerify())

    def getTime(self):
        return self.time

    def setState(self, newState):
        self.sate = newState

    def joinQueue(self, socket):
        self.queue.append(socket)

    def appendBuzzer(self, address, buzz):
        self.buzzers[address] = buzz

    def setTurn(self, buzzer):
        self.turn = buzzer

    def toVerify(self):
        self.mode = State.VERIFYING

        # TODO : inform the front end
    def setRandomTurn(self):
        if self.queue:
            self.turn = random.choice(self.queue)
        else:
            self.mode = State.QFINISHED


    def updateRanking(self):
        if self.buzzers:
            rank = self.buzzers.keys()
            n = len(rank)
            for i in range(n, 0, -1):
                for j in range(n, n-1, -1):
                    pres = rank[j]
                    prev = rank[j-1]
                    if self.buzzers[pres].getPoints() > self.buzzers[prev].getPoints():
                        rank[j], rank[j-1] = rank[j-1], rank[j]

            table = dict()
            for b in rank:
                points = self.buzzers[b].getPoints()
                table[b] = points
            return table
        else:
            return None


class Buzzer:
    def __init__(self, button, group, to_sum, to_rest, lives):
        self.button = button
        self.group = group
        self.students = list()
        self.increment = to_sum
        self.decrease = to_rest
        self.points = 0
        self.lives = 10

    @property
    def getButton(self):
        return self.button

    @property
    def getGroup(self):
        return self.group

    @property
    def getPoints(self):
        return self.points

    @property
    def getLives(self):
        return self.lives

    @property
    def getStudents(self):
        return self.students

    def increasePoints(self):
        self.points = self.points + self.increment

    def decreasePoints(self):
        if self.points > (self.decrease - 1):
            self.points = self.points - self.decrease

    def restLive(self):
        self.lives = self.lives - 1

    def setStudents(self, lst):
        if len(lst) > len(self.students):
            for student in lst:
                if student not in self.students:
                    self.students.append(student)


class State(Enum):
    CONNECTING = 1
    INITIATE = 2
    WAITING = 3
    VERIFYING = 4
    QFINISHED = 5
    ENDGAME = 6


    '''
    CREATE = 1
    SEARCHING = 2
    INITIATE = 3
    WAITING = 4
    ENDGAME = 5
    '''

