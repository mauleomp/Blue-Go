from enum import Enum
'''
MODES:

- FAST
- RANDOM
- LIVES
'''

class Game:
    # mode: is the mode of the game that could be NORMAL,RANDOM, LIFETIMES
    # buzzers: list of buzzers, clients of the game

    def __init__(self, mode, teams, conf: list = None):
        self.plus_points = 10
        self.rest_points = 5
        self.time = 0
        self.conf4 = 0
        self.ranking = list()
        self.mode = mode
        self.buzzers = dict()
        self.queue = list()
        self.sate: State = State.CONNECTING
        self.turn = None
        self.teams = teams
        self.isAnon = False
        if teams is None:
            self.isAnon = True
        if conf is not None:
            self.plus_points = conf[0]
            self.rest_points = conf[1]
            if mode == "RANDOM":
                self.time = conf[2]
            elif mode == "LIVES":
                self.time = conf[2]
                self.conf4 = conf[3]




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
        return self.isAnon

    @property
    def getTeams(self):
        return self.teams

    def setState(self, newState):
        self.sate = newState

    def joinQueue(self, socket):
        self.queue.append(socket)

    def appendBuzzer(self, address, buzz):
        self.buzzers[address] = buzz

    def setTurn(self, buzzer):
        self.turn = buzzer

    def updateRanking(self):
        rank = list()
        for k, buzzers in self.buzzers.items():
            # TODO: create the algorithm to rank the buzzers
            pass
        return rank


class Buzzer:
    def __init__(self, button, group):
        self.button = button
        self.group = group
        self.students = list()
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

    def increasePoints(self, p: int = 10):
        self.points = self.points + p

    def decreasePoints(self, p: int = 3):
        if self.points > 2:
            self.points = self.points - p

    def restLive(self):
        self.lives = self.lives - 1

    def setStudents(self, lst):
        #TODO: handle the students here
        # do an algorithm that puts only the new students
        self.students = lst


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

