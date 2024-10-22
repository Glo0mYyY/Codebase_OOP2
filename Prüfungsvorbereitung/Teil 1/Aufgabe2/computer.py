import geraet


class Computer(geraet.ElekronischesGeraet):
    def einschalten(self):
        print("Schalten sie den Computer mit dem Knopf ein")

    def verwende(self):
        print("Verweden sie den Computer mit Maus und Tastatur")
