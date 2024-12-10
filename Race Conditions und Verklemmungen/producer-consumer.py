import threading
import time

lock = threading.Lock()
data_ready = threading.Event()
shared_data = None


def producer():
    global shared_data
    with lock:
        shared_data = 42
        print("Producer hat den Wert produziert:", shared_data)
        data_ready.set()  # Signal an Consumer


def consumer():
    data_ready.wait()  # Warten, bis Producer fertig ist
    with lock:
        print("Consumer verarbeitet den Wert:", shared_data)


t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

t1.start()
t2.start()

t1.join()
t2.join()
