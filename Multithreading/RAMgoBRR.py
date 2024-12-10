import threading

counter = 0


def increaseCounter(threadName):
    for i in range(100):
        global counter
        counter += 1
        print(counter, threadName)



threads = []

for i in range(10000000):
    thread = threading.Thread(target=increaseCounter, args=(f"Thread{i+1}",))
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()


print("fertig")