import socket
import json
import os
from login import Ui_MainWindow
import requests
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
import time
import redis
from PyQt6.QtWidgets import QMessageBox


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
    # ghi code vào file
    with open('temp.py', 'w', encoding='utf-8') as f:
        f.write(code)
    # chạy code
    os.system('python temp.py')
    
class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.connect)
        self.load_config()
        
    def load_config(self):
        # kiểm tra file config.json có tồn tại không
        if not os.path.exists('config.json'):
            return
        with open('config.json', 'r', encoding='utf-8') as f:
            data = json.loads(f.read())
            self.ui.lineEdit.setText(f"{data['ip_socket']}:{data['port_socket']}")
            self.ui.lineEdit_2.setText(f"{data['ip_redis']}:{data['port_redis']}")
              
    def connect(self):
        if self.ui.lineEdit.text() == '' or self.ui.lineEdit_2.text() == '':
            QMessageBox.critical(self, 'Error', 'Vui lòng nhập đầy đủ thông tin')
            return
        
        ip_socket = self.ui.lineEdit.text().split(':')[0]
        port_socket = int(self.ui.lineEdit.text().split(':')[1])
        ip_redis = self.ui.lineEdit_2.text().split(':')[0]
        port_redis = int(self.ui.lineEdit_2.text().split(':')[1])
        self.r = redis.Redis(host=ip_redis, port=port_redis, db=0)
        
        # lưu thông tin vào file config
        with open('config.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps({
                'ip_socket': ip_socket,
                'port_socket': port_socket,
                'ip_redis': ip_redis,
                'port_redis': port_redis
            }))
        
        
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


"""
        self.close()
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
                    run_code(redis_key, self.r)
                if json_data['cmd'] == 'ping':
                    client_socket.sendall(json.dumps({
                        'cmd': 'pong'
                    }).encode())
                if json_data['cmd'] == 'exit':
                    break
            except Exception as e:
                print(e)
                time.sleep(1)
            
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())