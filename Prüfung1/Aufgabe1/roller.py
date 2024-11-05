from transportmittel import Transportmittel

class Roller(Transportmittel):
    def vorbereiten(self):
        print("Roller benötigt keine besondere Vorbereitung")
    def bewegen(self):
        print("Der Roller rollt los")