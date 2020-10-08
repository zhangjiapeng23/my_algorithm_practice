import json
import socket
import struct

import os

base_dir = os.path.dirname(__file__)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8890))
while 1:
    cmd = input('>> ').encode('utf-8').strip()
    client.send(cmd)
    header = client.recv(4)
    header_len = struct.unpack('i', header)[0]
    header_json = client.recv(header_len)
    header_dic = json.loads(header_json)
    file_name = header_dic.get('file_name')
    total_size = header_dic.get('total_size')
    size = 0
    with open(os.path.join(base_dir, 'download', file_name), 'wb') as f:
        while size < total_size:
            data = client.recv(1024)
            size += len(data)
            f.write(data)
            os.system('cls')
            print('Download precent: {:.2%}\n Porcess: {}'.format(size/total_size, "*" *int(100*(size/total_size))))


client.close()


