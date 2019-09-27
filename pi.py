# Created by Kacper Latuszewski 2019 - ZSK Poznan 

import webbrowser
import time
import os
from ftplib import FTP_TLS
from pynput.keyboard import Key, Controller

keyboard = Controller()

while True:
    webbrowser.open_new_tab('zastepstwa.html')
    time.sleep(5) #open html
    keyboard.press(Key.f11)
    keyboard.release(Key.f11)
    time.sleep(14400) #every 4h
    os.system("killall -KILL chromium-browse") #close chrome