import socket

def main():
    # 1. 创建socket对象
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 第二个参数表示TCP传输
    # 2. 绑定端口
    tcp_server_socket.bind(('', 7890))
    # 3. 监听连接
    tcp_server_socket.listen(128)
    # 4. 等待连接到来（阻塞式等待）
    new_server_socket, client_addr = tcp_server_socket.accept()
    print('连接成功，客户端为：%s:%d' % (client_addr[0], client_addr[1]))
    # 5. 接收客户端的消息
    while True:
        data = new_server_socket.recv(1024)  # 只返回数据
        if data:
            print(data.decode())
        # 6. 返回信息给客户端
            new_server_socket.send('回送消息'.encode('utf-8'))
        # 7. 关闭socket
        else:
            tcp_server_socket.close()
    new_server_socket.close()


if __name__ == '__main__':
    main()
