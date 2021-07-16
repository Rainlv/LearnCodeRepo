import socket  # 导入 socket 模块
import threading

# 1. 创建socket对象
udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # 参数：第一个指定为ipv4网络，第二个指定udp传输

# 绑定端口
udp_socket.bind(('192.168.0.104', 12345))

dist_ip = input('输入目标ip: ').strip()
dist_port = int(input('输入目标端口: ').strip())

if len(dist_ip) == 0:
    dist_ip = '192.168.0.104'


def send_(udp_socket, dist_ip, dist_port):
    while True:
        send_data = input('输入发送信息：')
        udp_socket.sendto(send_data.encode('utf-8'), (dist_ip, dist_port))


def recv_(udp_socket):
    while True:
        data, ip_port = udp_socket.recvfrom(1024)  # 参数指定收到的信息的最大字节数
        print(data.decode(), ip_port)


t_send = threading.Thread(target=send_, args=(udp_socket, dist_ip, dist_port))
t_recv = threading.Thread(target=recv_, args=(udp_socket,))
t_send.start()
t_send.join()
t_recv.start()
t_recv.join()

# 3. 关闭socket
udp_socket.close()
