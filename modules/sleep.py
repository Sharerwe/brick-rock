
import time
import random

def run(**args):
    upper = 4
    lower = 8
    sleep_time = random.randint(lower, upper)
    print('[!] Sleep:', sleep_time)
    time.sleep(sleep_time)
    return sleep_time
                    
