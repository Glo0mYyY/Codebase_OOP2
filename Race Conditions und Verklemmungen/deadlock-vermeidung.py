import threading

lock1 = threading.Lock()
lock2 = threading.Lock()


def thread1():
    with lock1:
        print("Thread 1 hat Lock 1 erworben")
        with lock2:
            print("Thread 1 hat Lock 2 erworben")


def thread2():
    with lock1:
        print("Thread 2 hat Lock 1 erworben")
        with lock2:
            print("Thread 2 hat Lock 2 erworben")


t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)

t1.start()
t2.start()

t1.join()
t2.join()
