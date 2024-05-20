import time

def slow_print(text, delay=0.2):
    for char in text:
        print(char, end='')
        time.sleep(delay)