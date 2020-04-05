import pynput
from pynput.keyboard import Key, Listener
import time
import os
#CatHook 0.1 - Unit 221B - stop cats from messing up your computer - Lance James
print("CatHook 0.1 - Unit 221B, LLC")
suspend = 'pmset displaysleepnow'
freq = []
key_col = []
def on_press(key):
    global freq
    global key_col
    print(str(key))
    current_milli_time = lambda: int(round(time.time() * 1000))
    print(current_milli_time())
    freq.append(current_milli_time())
    if len(freq) > 1:
        two_keys = freq[1] - freq[0]
        freq = []
        if two_keys == 84: #long press in ms
            key_col.append(two_keys)
            if len(key_col) == 15: #up the sensitivity here if you hold down the backspace a lot
                print("you are not human", two_keys)
                os.system(suspend) #hacky but it will work on Mac!
                key_col =[]
        if two_keys < 10:
            key_col.append(two_keys)
            if len(key_col) == 4:
                if key_col[0] + key_col[1] + key_col[2] + key_col[3] < 40:
                    print("you are not human", key_col[0]+key_col[1]+key_col[2]+key_col[3])
                    os.system(suspend)
                    key_col=[]
with Listener(on_press=on_press) as listener:
    listener.join()
