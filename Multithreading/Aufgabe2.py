import threading
import time

def text1():
    for i in range(5):
        print("Hallo")
        time.sleep(1)

def text2():
    for i in range(5):
        print("Tschüss")
        time.sleep(.8)


thread1 = threading.Thread(target=text1)
thread2 = threading.Thread(target=text2)
thread1.start()
thread2.start()
