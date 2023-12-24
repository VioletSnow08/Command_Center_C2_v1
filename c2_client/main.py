# This is a C2 server that will connect to a C2 client and execute commands
# The server will be able to execute commands and send the output back to the client

# Date: 12/22/2023
# Version: 0.1
# Developed by: Violet Lauro

import uuid
import requests
import platform
import socket

C2_SERVER = "127.0.0.1"
C2_SERVER_PORT = 8000


def connect():
    # Connect to the server
    # Send a ping every x seconds
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            client_socket.connect((C2_SERVER, C2_SERVER_PORT))
            print("Connected to server: " + str(C2_SERVER) + " on port: " + str(C2_SERVER_PORT))
        except:
            print("Unable to connect to server: " + str(C2_SERVER) + " on port: " + str(C2_SERVER_PORT))
            continue
        client_socket.sendall(b"New Client.")
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print('Received', repr(data))
    client_socket.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    connect()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
