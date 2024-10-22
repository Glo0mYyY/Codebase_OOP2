# Wenn Modul und Klasse den gleichen Namen haben, wird die Klasse nicht gefunden.
from vogel123 import Vogel
from hund123 import Hund

vogel = Vogel()
hund = Hund()
vogel.bewege()
hund.bewege()
vogel.mache_geraeusch()
hund.mache_geraeusch()
