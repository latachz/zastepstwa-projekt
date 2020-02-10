# Created by Kacper Latuszewski 2019 - ZSK Poznan 

import pysftp as sftp

def push_file_to_server():
    # `ssh-keygen` already outputs in pem format so we need just to add `.pem` extension
    private_key_location = 'key.pem'
    f = sftp.Connection(host='192.168.220.38', username='pi', private_key=private_key_location)
    local_path = "Zastępstwa.html"
    remote_path = "/home/pi/Desktop/zastepstwa-gui/Zastępstwa.html"

    f.put(local_path, remote_path)
    f.close()

push_file_to_server()
