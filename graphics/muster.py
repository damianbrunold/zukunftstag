from graphics import *

vorbereiten()

# Lissajous-Figur

hoch()
duenn()
schwarz()

a = 0.02
b = 0.0
c = 0.0345
d = 0.0

for i in range(20000):
    gehezu(10 + 490 * (math.sin(i * a + b) + 1),
           10 + 490 * (math.sin(i * c + d) + 1))
    if i == 0: tief()
        
anzeigen()
