from abc import ABC, abstractmethod

class Transportmittel:
    @abstractmethod
    def vorbereiten(self):
        pass
    def bewegen(self):
        pass
