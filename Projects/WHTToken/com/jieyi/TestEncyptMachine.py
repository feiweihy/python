import socket,binascii

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 8018
client.connect((host, port))

# 字符串形式的命令转化为要发送的byte数组
def asc2byte_strmsg(send_msg):
    send_msg_len = len(send_msg)
    send_msg_byte = binascii.b2a_hex(send_msg.encode())
    send_msg_bytehex = send_msg_byte.decode()
    send_msg_bytehex = str(send_msg_len).zfill(4) + send_msg_bytehex
    return binascii.a2b_hex(send_msg_bytehex)

# send_msg = 'EJS02'
# send_msg_len = len(send_msg)
#
# send_msg_byte = binascii.b2a_hex(send_msg.encode())
# send_msg_bytehex = send_msg_byte.decode()
#
# send_msg_bytehex = str(send_msg_len).zfill(4)+send_msg_bytehex
#
# print(send_msg_bytehex)
# print(binascii.a2b_hex(send_msg_bytehex))

client.send(asc2byte_strmsg('EJS02'))

recvmsg = client.recv(1024)

print (recvmsg)

client.close()

