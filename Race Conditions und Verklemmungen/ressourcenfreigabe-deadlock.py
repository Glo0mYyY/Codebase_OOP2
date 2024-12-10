import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()


def process1():
    while True:
        acquired_lock1 = lock1.acquire(timeout=1)
        if acquired_lock1:
            print("Process 1 hat Lock 1 erworben")
            time.sleep(1)
            acquired_lock2 = lock2.acquire(timeout=1)
            if acquired_lock2:
                print("Process 1 hat Lock 2 erworben")
                lock2.release()
                break
            else:
                print("Process 1 konnte Lock 2 nicht erwerben, gibt Lock 1 frei")
                lock1.release()
        else:
            print("Process 1 konnte Lock 1 nicht erwerben")
        time.sleep(0.5)


def process2():
    while True:
        acquired_lock2 = lock2.acquire(timeout=1)
        if acquired_lock2:
            print("Process 2 hat Lock 2 erworben")
            time.sleep(1)
            acquired_lock1 = lock1.acquire(timeout=1)
            if acquired_lock1:
                print("Process 2 hat Lock 1 erworben")
                lock1.release()
                break
            else:
                print("Process 2 konnte Lock 1 nicht erwerben, gibt Lock 2 frei")
                lock2.release()
        else:
            print("Process 2 konnte Lock 2 nicht erwerben")
        time.sleep(0.5)


t1 = threading.Thread(target=process1)
t2 = threading.Thread(target=process2)

t1.start()
t2.start()

t1.join()
t2.join()
