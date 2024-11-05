from waschmaschine import Waschmaschine
from staubsauger import Staubsauger

waschmaschine = Waschmaschine()
staubsauger = Staubsauger()

geraete = [waschmaschine,staubsauger]

for geraet in geraete:
    geraet.anschalten()
    geraet.verwenden()
