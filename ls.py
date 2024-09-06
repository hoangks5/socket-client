import socket
import json
import os

import requests





def get_clients():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('3.18.29.6', 12345)
    client_socket.connect(server_address)
    # Send command to the server
    command = {
        'cmd': 'ls_clients'
    }
    print('Sending command to server:', command)
    client_socket.sendall(json.dumps(command).encode())
    # Receive response from server
    response = client_socket.recv(1024)
    response = json.loads(response.decode())
    print('Received response from server:', response)
    return response['result']

get_clients()