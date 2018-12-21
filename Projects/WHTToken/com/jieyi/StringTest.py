
print('31'.encode("GBK"))

str1 = 'you 你'
bs = b'\xc4\xe3'

print('utf-8 encode:', str1.encode('utf-8'))
print('gbk encode:', str1.encode('gbk'))
print('gb2312 encode:', str1.encode('gb2312'))

print(bs.decode('gb2312'))


# x = '53216A'
# print(x)
# y = bytearray.fromhex(x)
# print(y)
# z = str(y)
# print(z)

x = '53216A'
print('x:', end=" " )
print(x)
y = bytearray.fromhex(x)
print('y:', end=" " )
print(y)
z = str(y)
print('z:', end=" " )
print(z)