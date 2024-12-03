import threading
import time

lock = threading.Lock()

counter = 0


def increaseCounter(threadName):
    for i in range(100):
        lock.acquire()
        global counter
        counter += 1
        print(counter, threadName)
        lock.release()
        time.sleep(0.01)


thread1 = threading.Thread(target=increaseCounter, args=("Thread1",))
thread2 = threading.Thread(target=increaseCounter, args=("Thread2",))
thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("fertig")