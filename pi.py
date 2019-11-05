# Created by Kacper Latuszewski 2019 - ZSK Poznan 

import webbrowser
import time
import os
from ftplib import FTP_TLS
from pynput.keyboard import Key, Controller

keyboard = Controller()

i = 0
n = 60 

while True:
    #keyboard.press(Key.f5)
    #keyboard.release(Key.f5)
    while i <= n + 1:
        if i <= n/2:
            keyboard.press(Key.down)
            keyboard.release(Key.down)
            print(i)
            i += 1;
        elif i <= n and i > n/2:
            keyboard.press(Key.up)
            keyboard.release(Key.up)
            print(i)
            i += 1;
        else:
            i = 0
        time.sleep(1)

    time.sleep(10)