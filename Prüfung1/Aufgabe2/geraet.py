from abc import ABC, abstractmethod

class Haushaltsgeraet():
    @abstractmethod
    def anschalten(self):
        pass
    def verwenden(self):
        pass