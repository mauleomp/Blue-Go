# IMPORTS FOR THE BLE SERVER
import bluetooth
import selectors
import types
import asyncio
from game import Game, Buzzer, State
# IMPORTS FOR IR CONTROLLER
import RPi.GPIO as GPIO
from time import time
import time as t
import timeit
from dbpi import *

pins = {"0xff18e7": "UP", "0xff4ab5": "DOWN", "0xff10ef": "LEFT", "0xff5aa5": "RIGHT", "0xff38c7": "OK"}

global sel
ng = '\'1\''
# VARIABLES FOR THE GAME AND THE SERVER
sel = selectors.DefaultSelector()
playing = False


# ----------------------- FUNCTIONS OF THE SERVER -------------------------------------
# This function is in charge of creating the socket for connecting the bluetooth devices

async def initiateServer():
    # unique uuid to connect with. used previously when connecting with BLE
    uuid = "ca52bb51-cab6-4122-ad2c-df2d5f733d04"
    # creation of the server socket with the mac and port
    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    addr = bluetooth.read_local_bdaddr()[0]
    server_sock.bind((addr, bluetooth.PORT_ANY))
    server_sock.listen(1)
    # Advertise the service with our socket and uuid
    bluetooth.advertise_service(server_sock, "blue", service_id=uuid,
                                service_classes=[uuid, bluetooth.SERIAL_PORT_CLASS],
                                profiles=[bluetooth.SERIAL_PORT_PROFILE],
                                # protocols=[bluetooth.OBEX_UUID]
                                )
    print("Listening on : ", server_sock.getsockname())
    # trying to handle different sockets within a selector
    sel.register(server_sock, selectors.EVENT_READ, data=None)
    t.sleep(10)
    while not fetchStart(ng)[0]:
        print("Waiting the game for being Started...")
        t.sleep(10)


    print("################   GAME HAS STARTED  ##################")
    s_game = fetchGame(ng)
    game = Game(s_game[0])
    print("GAME GENERATED")

    try:
        while True:
            events = sel.select(timeout=None)
            for key, mask in events:
                if key.data is None:
                    await acceptClient(key.fileobj, game)
                else:
                    await servConnexion(key, mask, game)
            await asyncio.sleep(0.1)
    except KeyboardInterrupt:
        print("keyboard interruption. ")
        pass
    finally:
        sel.close()


async def acceptClient(sock, game):
    client_sock, client_info = sock.accept()
    print("-----------------------------------------")
    print("Accepted connection from", client_info)
    data = types.SimpleNamespace(addr=client_info, inb=b"", outb=b"")
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(client_sock, events, data=data)
    # TODO: get the information from the database and create a class
    group = 0
    if game.getBuzzers():
        group = len(game.getBuzzers().keys()) + 1

    points = game.getPoints()
    to_rest = game.getRestPoints()
    lives = game.getLives()
    buzzer = Buzzer(client_sock, group, points, to_rest, lives)
    game.appendBuzzer(client_info, buzzer)
    # TODO: send a notification to the server (WebApp)


# This method handles the connection (it handles the received )
async def servConnexion(key, mask, game):
    sock = key.fileobj
    data = key.data
    # Event to read the data received from the buzzer
    if mask & selectors.EVENT_READ:
        msg = sock.recv(1024)
        if msg:
            # handle the data here
            ans = handleMessage(key, msg, game)
            print(data.addr, " : ", msg)
            data.outb += ans
        else:
            print("Closing the connection with ", data.addr)
            sel.register(sock)
            sock.close()

    # Event to send the correspondent data to the user
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print(f"Sending back {data.outb!r} to {data.addr}")
            sent = sock.send(data.outb)
            data.outb = data.outb[sent:]


# this function handles the message received by a certain buzzer
def handleMessage(key, message, game):
    addr = key.data.addr
    mbytes = message.decode('utf-8')
    bars = mbytes.split('\r')
    msg = bars[0].split(';')
    command = msg[0]
    ans = None
    print(command)

    if command == 'game-mode':
        if game.isAnon():
            ans = bytes('Y', 'utf-8')
        else:
            ans = bytes('N', 'utf-8')


    elif command == 'students':
        print(">>students received")
        students = command[1].split(';')
        if addr in game.getBuzzers().keys():
            buzz = game.getBuzzers()[addr]
            buzz.setStudents(students)
        ans = bytes('1', 'utf-8')

    elif command == 'game-started':
        print(" >>game started received")
        state = fetchState(ng)
        st = state[0]
        if st == 'WAITING':
            game.setState(State.WAITING)
            print(">>game started")

        if game.getSate == State.WAITING:
            ans = bytes('Y', 'utf-8')
        else:
            ans = bytes('N', 'utf-8')

    elif command == 'signal':
        ans = handleGameMode(key, game)


    elif command == 'question-finished':
        turn = fetchTurn(ng)

        state = turn[2]
        if state == 'VERIFYING':
            if turn[1] == 'correct':
                correctAnswer(game)
            elif turn[1] == 'wrong':
                wrongAnswer(game)

        if game.getSate() == State.VERIFYING:
            if game.getTurn() == key.data.addr:
                ans = bytes('5', 'utf-8')
            else:
                ans = bytes('N', 'utf-8')
        elif game.getSate() == State.ENDGAME or game.getSate() == State.WAITING:
            ans = bytes('Y', 'utf-8')
        print(">> question finished received")

    elif command == 'game-finished':
        if fetchState(ng) == '\'ENDGAME\'':
            game.setState(State.ENDGAME)
        if game.getSate() == State.ENDGAME():
            ans = bytes('Y', 'utf-8')
        else:
            ans = bytes('N', 'utf-8')
    else:
        print(">>ERROR")
        ans = bytes('0', 'utf-8')
    return ans



def handleGameMode(key, game):
    asn = bytes('0', 'utf-8')

    if game.getMode() == 'FAST' or game.getMode() == 'FLives':
        if game.getSate() == State.WAITING:
            if checkQueue(key, game):
                ans = bytes('Y', 'utf-8')
            else:
                ans = bytes('N', 'utf-8')
            #correctAnswer(game)
        elif game.getSate() == State.VERIFYING:
            if key not in game.getQueue():
                game.joinQueue(key)
        elif game.getSate() == State.ENDGAME:
            ans = bytes('9', 'utf-8')
    elif game.getMode() == 'RANDOM' or game.getMode() == 'RLIVES':
        # TODO needs to be implemennted
        if game.getSate() == State.WAITING:
            tm = timeit.default_timer()
            if (tm - game.getSt()) < game.getTime()*100:
                game.joinQueue(key.data.addr)
                ans = bytes('N', 'utf-8')

    return ans






# check the message and respond to it using key.data.outb += response in a byte
# this function should check if the person is the first
# it will add it to the queue, otherwise
def checkQueue(key, game):

    if not game.getQueue():
        game.joinQueue(key)
        buzz = game.getBuzzers()[key.data.addr]
        game.setTurn(buzz )
        game.setState(State.VERIFYING)
        updateState(ng, '\'VERIFYING\'')
        updateCorrect(ng, '\'correct\'')
        return True
    else:
        game.joinQueue(key)
        return False


# called when commands says that is a wrong answer
def wrongAnswer(game):
    id = game.getTurn()
    buzz = game.getBuzzers()[id]
    buzz.decreasePoints()
    if game.getMode() == 'RLIVES' or game.getMode() == 'FLIVES':
        buzz.restLive()

    if game.getMode() == 'FAST' or game.getMode() == 'FLIVES':
        next = nextInQueue(game)
        if next != None:
            game.setTurn(next)
        else:
            game.setMode(State.QFINISHED)
            updateState(ng, '\'Q_FINISHED\'')
            updateRanking(ng, game.getRanking())
            # TODO: notify the front//




# method to return the next socket in queue
def nextInQueue(game):
    game.getQueue().pop(0)
    if game.getQueue():
        turn = game.getQueue()[0]
        return turn.data.addr
    else:
        None


# Method that is called when buzzer gives a good answer
def correctAnswer(game):
    id = game.getTurn()
    buzz = game.getBuzzers()[id]
    buzz.increasePoints()
    nextQuestion(game)

def nextQuestion(game):
    game.setTurn(None)
    game.setState(State.QFINISHED)
    updateState(ng, '\'Q_FINISHED\'')
    updateRanking(ng, game.getRanking())
    if game.getMode() == 'RANDOM' or game.getMode() == 'RLIVES':
        game.setState(timeit.default_timer())

def startQuestion(game):
    game.setState(State.WAITING)
    if game.getMode() == 'RANDOM' or game.getMode() == 'RLIVES':
        game.setSt(timeit.default_timer())




# -------------------------------- FUNCTIONS OF THE CONTROLLER ------------------------------

#  up the pin reading on the raspberry board
def setup():
    GPIO.setmode(GPIO.BOARD)  # Numbers GPIOs by physical location
    GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


# obtain the binary data from the ir remote
def binary_aquire(pin, duration):
    # aquires data as quickly as possible
    t0 = time()
    results = []
    while (time() - t0) < duration:
        results.append(GPIO.input(pin))
    return results


# catch read the pulsation from the certain pin
def on_ir_receive(pinNo, bouncetime=150):
    # when edge detect is called (which requires less CPU than constant
    # data acquisition), we acquire data as quickly as possible
    data = binary_aquire(pinNo, bouncetime / 1000.0)
    if len(data) < bouncetime:
        return
    rate = len(data) / (bouncetime / 1000.0)
    pulses = []
    i_break = 0
    # detect run lengths using the acquisition rate to turn the times in to microseconds
    for i in range(1, len(data)):
        if (data[i] != data[i - 1]) or (i == len(data) - 1):
            pulses.append((data[i - 1], int((i - i_break) / rate * 1e6)))
            i_break = i
    # decode ( < 1 ms "1" pulse is a 1, > 1 ms "1" pulse is a 1, longer than 2 ms pulse is something else)
    # does not decode channel, which may be a piece of the information after the long 1 pulse in the middle
    outbin = ""
    for val, us in pulses:
        if val != 1:
            continue
        if outbin and us > 2000:
            break
        elif us < 1000:
            outbin += "0"
        elif 1000 < us < 2000:
            outbin += "1"
    try:
        return int(outbin, 2)
    except ValueError:
        # probably an empty code
        return None


# clean the GPIO port for not reading IR signals
def destroy():
    GPIO.cleanup()


def handleCommand(command, game):

    # TODO :  call the server on each interaction
    if command == "OK":
        if game.getSate() == State.CONNECTING:
            if len(game.getBuzzers()) > 0:
                game.setState(State.INITIATE)
            else:
                pass
        elif game.getSate() == State.INITIATE:
            game.setState(State.WAITING)

        elif game.getSate() == State.QFINISHED:
            game.setState(State.WAITING)

    elif command == "UP":
        if game.getSate() == State.VERIFYING:
            game.setState(State.QFINISHED)
            nextQuestion(game)

    elif command == "LEFT":
        if game.getSate() == State.VERIFYING:
            wrongAnswer(game)

    elif command == "RIGHT":
        if game.setState() == State.VERIFYING:
            game.setState(State.QFINISHED)
            correctAnswer(game)
    elif command == "DOWN":
        if game.getSate() == State.QFINISHED:
            game.setState(State.ENDGAME)




async def activateIR(game):
    setup()
    try:
        print("Starting IR Listener")
        while True:
            GPIO.wait_for_edge(11, GPIO.FALLING)
            code = on_ir_receive(11)
            if code:
                intCode = str(hex(code))
                if intCode in pins:
                    # Handle the commands here
                    command = pins[intCode]
                    await handleCommand(command, game)

            else:
                print("Invalid code")
            await asyncio.sleep(0.01)
    except KeyboardInterrupt:
        pass
    except RuntimeError as err:
        print(err)
        pass
    print("Quitting")
    destroy()


# -------------------  FUNTIONS TO CALL FROM THE SERVER ----------------------

'''
MODE could be : 'FAST' 'RANDOM' 'FLIVES' 'RLIVES'
teams: array of the group of students
settings: array of the settings
'''


def initiateGame():
    loop = ""
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = None

    if loop and loop.is_running():
        print('Async event loop is running.')
        tsk = loop.create_task(initiateServer())
        # ^-- https://docs.python.org/3/library/asyncio-task.html#task-object
        # Optionally, a callback function can be executed when the coroutine completes
        tsk.add_done_callback(
            lambda t: print(f'Task done with result={t.result()} << return val of main()')
        )
    else:
        print('Starting new even loop')
        asyncio.run(initiateServer())
    #asyncio.ensure_future(initiateServer(game))
    # asyncio.ensure_future(activateIR(game))


def finishGame(game):
    game.setState(State.ENDGAME)
    sel.close()



if __name__ == "__main__":
    initiateGame()


