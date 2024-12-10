import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()


def process1():
    with lock1:
        print("Process 1 hat Lock 1 erworben")
        time.sleep(1)
        print("Process 1 versucht Lock 2 zu erwerben...")
        with lock2:
            print("Process 1 hat Lock 2 erworben")


def process2():
    with lock2:
        print("Process 2 hat Lock 2 erworben")
        time.sleep(1)
        print("Process 2 versucht Lock 1 zu erwerben...")
        with lock1:
            print("Process 2 hat Lock 1 erworben")


t1 = threading.Thread(target=process1)
t2 = threading.Thread(target=process2)

t1.start()
t2.start()

t1.join()
t2.join()
