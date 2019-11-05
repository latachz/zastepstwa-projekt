# Created by Kacper Latuszewski 2019 - ZSK Poznan 

import webbrowser
import time
import os
from ftplib import FTP_TLS
from pynput.keyboard import Key, Controller

keyboard = Controller()

i = 5

while True:
    keyboard.press(Key.f5)
    keyboard.release(Key.f5)
    while i <= 8:
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        time.sleep(2)
        
    while i <= 8:
        keyboard.press(Key.up)
        keyboard.release(Key.up)
        time.sleep(2)
        
    time.sleep(3)