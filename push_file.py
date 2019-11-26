# Created by Kacper Latuszewski 2019 - ZSK Poznan 

import pysftp as sftp

def push_file_to_server():
    cnopts = sftp.CnOpts()
    cnopts.hostkeys = None 
    f = sftp.Connection(host='192.168.0.10', username='pi', password='qwerty1231', cnopts=cnopts)
    local_path = "zastepstwa.html"
    remote_path = "/home/pi/Desktop/zastepstwa-gui/zastepstwa.html"

    f.put(local_path, remote_path)
    f.close()

push_file_to_server()
