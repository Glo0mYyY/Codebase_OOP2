import threading
import time
# Ressourcen
lock1 = threading.Lock()
lock2 = threading.Lock()


def thread1():
    print("Thread 1: Warte auf Lock 1")
    with lock1:
        print("Thread 1: Lock 1 erhalten")
    time.sleep(1)
    print("Thread 1: Warte auf Lock 2")
    with lock2:
        print("Thread 1: Lock 2 erhalten")


def thread2():
    print("Thread 2: Warte auf Lock 2")
    with lock2:
        print("Thread 2: Lock 2 erhalten")
    time.sleep(1)
    print("Thread 2: Warte auf Lock 1")
    with lock1:
        print("Thread 2: Lock 1 erhalten")


t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)
t1.start()
t2.start()
t1.join()
t2.join()
