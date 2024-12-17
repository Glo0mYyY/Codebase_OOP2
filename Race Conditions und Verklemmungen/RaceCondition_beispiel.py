import threading
counter = 0
lock = threading.Lock()


def increment():
    global counter
    for _ in range(100000):
        with lock:  # Kommentiere diesen Lock aus, um eine Race Condition zu sehen
            counter += 1


def decrement():
    global counter
    for _ in range(100000):
        with lock:  # Kommentiere diesen Lock aus, um eine Race Condition zu sehen
            counter -= 1


t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=decrement)
t1.start()
t2.start()
t1.join()
t2.join()
