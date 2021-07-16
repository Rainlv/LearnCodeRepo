import socket


def main():
    # 1. 创建对象
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2. 连接服务器
    tcp_client_socket.connect(('192.168.0.104', 7890))
    # 3. 发送接收数据
    tcp_client_socket.send('发送信息'.encode('utf-8'))
    data = tcp_client_socket.recv(1024)
    print(data.decode())
    # 4. 关闭socket
    tcp_client_socket.close()


if __name__ == '__main__':
    main()