from bus import Bus
from roller import Roller

bus = Bus()
roller = Roller()

transportmittelList = [bus,roller]

for transportmittel in transportmittelList:
    transportmittel.vorbereiten()
    transportmittel.bewegen()