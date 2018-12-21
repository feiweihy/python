# 导入 socket、sys 模块
import socket

# 创建 socket 对象
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = '10.20.0.99'

# 设置端口号
port = 8018

# 连接服务，指定主机和端口
client.connect((host, port))

# EJS01
# s.sendall('EJS01')
#client.sendall(b'454A533031')
client.send(b'\x00\x05EJS02')

# 接收小于 1024 字节的数据
recvmsg = client.recv(1024)

print (recvmsg)

client.close()

