import threading
import time


def say_hello():
    print('hello world!')
    time.sleep(1)


if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=say_hello)
        t.start()