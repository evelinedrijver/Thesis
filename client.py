import socket
import struct

HEADER = 64
PORT = 16540
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())  #"127.0.0.1"
print(SERVER)
ADDR = (SERVER, PORT)

hoi = (2).to_bytes(1, byteorder='big')
hoi2 = int.from_bytes(hoi, 'big')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

data = client.recv(6)
print(data)
value = struct.unpack('ccHcc', bytearray(data))

version_info = int.from_bytes(value[0], 'big')
package_num = int.from_bytes(value[1], 'big')
msg_length = value[2]
command = int.from_bytes(value[3], 'big')
actual_data = int.from_bytes(value[4], 'big')

print(version_info, package_num, msg_length, command, actual_data)

def send(msg):
    #message = [bytes(2), bytes(0), 6, bytes(70), bytes(msg)]
    #message = msg.encode(FORMAT)
    # msg_length = len(message)
    # send_length = str(msg_length).encode(FORMAT)
    # send_length += b' ' * (HEADER - len(send_length))
    # client.send(send_length)
    # client.send(message)
    # print(client.recv(2048).decode(FORMAT))
    d = struct.pack('ccHcc', (2).to_bytes(1, byteorder='big'), (0).to_bytes(1, byteorder='big'), 6, (70).to_bytes(1, byteorder='big'), (msg).to_bytes(1, byteorder='big'))
    print(d)
    #d = struct.pack('c c H c c', 2, 0, 6, 70, msg )
    client.sendall(d)


send(2)
#input()
#send("Hello Everyone!")
#input()
#send("Hello Tim!")
#input()

#send(DISCONNECT_MESSAGE)