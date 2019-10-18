# Created by Kacper Latuszewski 2019 - ZSK Poznan 

import webbrowser
import time
import os
from ftplib import FTP_TLS
from pynput.keyboard import Key, Controller

keyboard = Controller()

while True:
    webbrowser.open_new_tab('zastepstwa.html')
    keyboard.press(Key.f5)
    keyboard.release(Key.f5)
    time.sleep(14400) #every 4h

