from render import *
from einlesen import *

vorbereiten()

daten = lese_daten("daten.txt")

brief = daten[2]

text(12, 5, brief["name"])
text(12, 5.5, brief["adresse"])
text(12, 6, brief["plzort"])

text(2, 9, brief["anrede"])
for j, zeile in enumerate(brief["zeilen"]):
    text(2, 10 + 0.5 * j, zeile)

anzeigen()
