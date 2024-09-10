from abc import ABC, abstractmethod


class Fahrzeug(ABC):
    @abstractmethod
    def fahren(self):
        pass


class Auto(Fahrzeug):
    def fahren(self):
        print("Auto fährt")


class Fahrrad(Fahrzeug):
    def fahren(self):
        print("Fahrrad fährt")


try:
    fahrzeug = Fahrzeug()
    fahrzeug.fahren()
except TypeError as e:
    print(e)

auto = Auto()
fahrrad = Fahrrad()


auto.fahren()
fahrrad.fahren()

print("--------------------")


class KannSprechen(ABC):
    @abstractmethod
    def sprechen(self):
        pass


class Hund(KannSprechen):
    def sprechen(self):
        print("Wuff")


class Mensch(KannSprechen):
    def sprechen(self):
        print("Hallo")


try:
    sprechen = KannSprechen()
    sprechen.sprechen()
except TypeError as e:
    print(e)

hund = Hund()
mensch = Mensch()


hund.sprechen()
mensch.sprechen()
