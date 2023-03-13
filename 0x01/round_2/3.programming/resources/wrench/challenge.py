#!/usr/bin/python3
import socket
import random
import time
import logging
import threading
import string

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = 'localhost'
PORT = 54321

flag = "flag{i_feel_the_need_the_need_for_speed}"

# bind to the port
serversocket.bind((HOST, PORT))

# start listening and hold a queue of 10 requests if at threading capacity
serversocket.listen(10)

# start listening for connections
while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()

    logging.info(f"Got a connection from {str(addr)}")

    correct_count = 0
    total_value = 0

    clientsocket.settimeout(3.0)
    try:

        # hold the connection open until empty or broken pipe
        while True:
            clientsocket.send("here we go, adddddm up:\n".encode('utf-8'))

            for i in range(200):
                match random.randint(0,3):
                    case 0:
                        clientsocket.send(f"{''.join(random.sample(string.ascii_lowercase, 8))}\n".encode('utf-8'))
                    case 1:
                        number = random.randint(0,1000)
                        total_value += number
                        clientsocket.send(f"{number}\n".encode('utf-8'))
                    case 2:
                        clientsocket.send(f"{hex(random.randint(0,10000))}\n".encode('utf-8'))

                time.sleep(0.01)

            # get result
            print(total_value)
            clientsocket.send("total: ".encode('utf-8'))
            
            msg = clientsocket.recv(1024).decode('utf-8')
            if not msg: raise EOFError
            else:
                # check for flag condition
                if int(msg.strip()) == total_value:
                    clientsocket.send(f"\n{flag}".encode('utf-8'))
                    break
                else:
                    raise SystemExit

    except TimeoutError:
        clientsocket.send("\ntoo slow...".encode('utf-8'))

    except EOFError:
        clientsocket.send("\ni mean... how about you send me something!".encode('utf-8'))

    except ValueError:
        clientsocket.send("\nsend me a number, you don't add letters together do you?".encode('utf-8'))

    except SystemExit:
        clientsocket.send("\nthat ain't it, give it another go...".encode('utf-8'))

    except Exception as e:
        logging.error(e)

    clientsocket.close()