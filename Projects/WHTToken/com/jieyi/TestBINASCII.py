import binascii

txt1 = '123456'
data1 = binascii.a2b_hex(txt1)
print(data1)

txt2 = binascii.b2a_hex(data1)
print(txt2)
print(txt2.decode())


send_msg = 'EJS02'
print(send_msg.encode('GBK'))
send_msg_byte = binascii.b2a_hex(send_msg.encode('GBK'))
print(send_msg_byte)
print(send_msg_byte.decode())
print(send_msg_byte.decode().encode())
