# Created by Kacper Latuszewski 2019 - ZSK Poznan 

import pysftp as sftp

def push_file_to_server():
    f = sftp.Connection(host='192.168.43.222', username='pi', password='qwerty1231')
    local_path = "zastepstwa.html"
    remote_path = "/home/pi/Desktop/zastepstwa-projekt/zastepstwa.html"

    f.put(local_path, remote_path)
    f.close()

push_file_to_server()