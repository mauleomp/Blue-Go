import bluetooth
import selectors
import types

sel = selectors.DefaultSelector()
msgs = []

# def handleData(data):


def initiateServer():
    # unique uuid to connect with. used previously when connecting with BLE
    uuid = "ca52bb51-cab6-4122-ad2c-df2d5f733d04"
    # creation of the server socket with the mac and port
    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    server_sock.bind(('B8:27:EB:94:BC:91', bluetooth.PORT_ANY))
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



    try:
        while True:
            events = sel.select(timeout=None)
            for key, mask in events:
                if key.data is None:
                    acceptClient(key.fileobj)
                else:
                    servConnexion(key, mask)
    except KeyboardInterrupt:
        print("keyboard interruption. ")
        pass
    finally:
        sel.close()


def acceptClient(sock):
    client_sock, client_info = sock.accept()
    print("Accepted connection from", client_info)
    data = types.SimpleNamespace(addr=client_info, inb=b"", outb=b"")
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(client_sock, events, data=data)


def servConnexion(key, mask):
    sock = key.fileobj
    data = key.data
    # Event to read the data received from the buzzer
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)
        if recv_data:
            # handle the data here
            print(recv_data)
            data.outb += recv_data
        else:
            print("Closing the connection with ", data.addr)
            sel.register(sock)
            sock.close()

    # Event to send the correspondent data to the user
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print(f"Sending back {data.outb!r} to {data.addr}" )
            sent = sock.send(data.outb)
            data.outb = data.outb[sent:]


if __name__ == '__main__':
    print("##### INITIATING SERVER")
    initiateServer()


