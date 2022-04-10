import bluetooth



def displayDev():
    print("Performing inquiry...")

    nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True, lookup_class=False)

    print("Found {} devices".format(len(nearby_devices)))
    for addr, name in nearby_devices:
        try:
            print("   {} - {}".format(addr, name))
        except UnicodeEncodeError:
            print("   {} - {}".format(addr, name.encode("utf-8", "replace")))


#def handleData(data):


def initiateServer():
    server_sock = bluetooth.BluetoothSoket(bluetooth.RFCOMM)
    server_sock.bind(("", bluetooth.PORT_ANY))
    server_sock.lsiten(1)

    port = server_sock.getSockname()[1]
    uuid = '28ffb42a-a8fd-11ec-b909-0242ac120002'

    bluetooth.advertuse_servise(server_sock, "RaspServer", service_id = uuid,
                                service_classes=[uuid, bluetooth.SERIAL_PORT_CLASS],
                                profiles=[bluetooth.SERIAL_PORT_PROFILE]
                                )
    print("WAITING FOR CONECTIONS ON RFCOMM CHANNEL.. ", port)

    client_sock, client_info = server_sock.accept()
    print("Accepted conection from", client_info)

    try:
        while True:
            data = client_sock.recv(1024)
            if not data:
                break
            ###we will handle the data here
            #handleData(data)
            print("DATA: ", data)
    except OSError:
        #correct and handlle the error
        pass

    print("DISCONECTED..")

    client_sock.close()
    server_sock.close()
    print("ALL FINISHED")


if __name__ == '__main__':
    initiateServer()



