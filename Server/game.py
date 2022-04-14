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

    def __init__(self, mode, teams, settings):
        self.ranking = list()
        self.mode = mode
        self.buzzers = dict()
        self.queue = list()
        self.sate: State = State.CONNECTING
        self.playing = False
        self.turn = None
        self.teams = teams
        self.isAnon = False
        if teams is None:
            True


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
    def isPlaying(self):
        return self.playing

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

    def setPlaying(self, is_playing):
        self.playing = is_playing

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
        self.students = lst


class State(Enum):
    CONNECTING = 1
    # INITIATE = 2
    WAITING = 2
    VERIFYING = 3
    ENDGAME = 4


    '''
    CREATE = 1
    SEARCHING = 2
    INITIATE = 3
    WAITING = 4
    ENDGAME = 5
    '''

