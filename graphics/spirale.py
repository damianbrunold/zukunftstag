from graphics import *

vorbereiten()

# Spirale

hoch()
mitte()

tief()
rot()
mittel()

richtung = 0
laenge = 5

for i in range(100):
    geherichtung(richtung, laenge + i)
    richtung += 33

    
anzeigen()
