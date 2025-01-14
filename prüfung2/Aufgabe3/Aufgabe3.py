from itertools import count
import threading

# Gemeinsame Ressource
counter = 0
# Lock-Objekt
counter_lock = threading.Lock()

wordList = ["test","wort","hallo","hahaha"]


global word_length
global results

def worker(words, start_index, end_index, results):  # Berechnet die Längen der Wörter im angegebenen Abschnitt
    for i in range(start_index, end_index):
        results[i] = word_length(words[i]) #=> Diese Funktion soll pro Thread ausgeführt werden. Es reichen zwei Threads, dann wäre die Aufgabe erledigt.


thread1 = threading.Thread(target=worker)
thread2 = threading.Thread(target=worker,args=wordList)
thread1.start()
thread2.start()
