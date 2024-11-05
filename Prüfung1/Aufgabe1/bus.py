from transportmittel import Transportmittel

class Bus(Transportmittel):
    def vorbereiten(self):
        print("Bus wird beladen")
    def bewegen(self):
        print("Bus fährt")