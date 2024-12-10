import threading

counter = 0


def increment_without_lock():
    global counter
    for _ in range(1000000):
        counter += 1


# Debuggen ohne Lock
counter = 0
t1 = threading.Thread(target=increment_without_lock)
t2 = threading.Thread(target=increment_without_lock)

t1.start()
t2.start()
t1.join()
t2.join()

print("Ohne Lock:", counter)

# Mit Lock behoben
lock = threading.Lock()


def increment_with_lock():
    global counter
    for _ in range(1000000):
        with lock:
            counter += 1


counter = 0
t1 = threading.Thread(target=increment_with_lock)
t2 = threading.Thread(target=increment_with_lock)

t1.start()
t2.start()
t1.join()
t2.join()

print("Mit Lock:", counter)
