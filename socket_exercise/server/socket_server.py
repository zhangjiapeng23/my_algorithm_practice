import json
import socket
import struct
import time
import os


base_dir = os.path.dirname(__file__)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8890))
server.listen(5)
print("Server start .....")
while 1:
    conn, addr = server.accept()
    print("have be connected ...", addr)
    while 1:
        try:
            cmd = conn.recv(1024)
            if not cmd: break
            cmds = cmd.decode('utf-8').split()
            file_name = cmds[1]
            header_dic = {
                'file_name': file_name,
                'date': time.time(),
                'total_size': os.path.getsize(os.path.join(base_dir, 'share', file_name))
            }
            header_json = json.dumps(header_dic).encode('utf-8')

            header = struct.pack('i', len(header_json))
            conn.send(header)
            conn.send(header_json)
            with open(os.path.join(base_dir, 'share', file_name), 'rb') as f:
                for line in f:
                    conn.send(line)

        except ConnectionResetError:
            print("Disconnect .......")
            break

    conn.close()

server.close()

