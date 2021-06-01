# Anleitung Graphik

Bei diesem Thema geht es darum mit dem Computer etwas zu zeichnen.
Dazu musst du dem Computer genau sagen, was er machen soll. Dies geschieht,
indem du ein Programm schreibst.

Es gibt folgende Befehle:

- `blau()` Schaltet auf blaue Farbe um
- `schwarz()` Schaltet auf schwarze Farbe um
- `weiss()` Schaltet auf weisse Farbe um
- `duenn()` Schaltet auf einen dünnen Stift um
- `mittel()` Schaltet auf einen mitteldicken Stift um
- `dick()` Schaltet auf einen dicken Stift um
- `hoch()` Hebt den Stift vom Papier ab, ab jetzt wird nicht gezeichnet
- `tief()` Senkt den Stift aufs Papier, sodass er ab jetzt zeichnet
- `gehezu(x, y)` Bewegt den Stift zum Punkt x, y
- `geherichtung(grad, laenge)` Bewegt den Stift in die Himmelsrichtung grad um laenge Einheiten.
- `mitte()` Positioniert den Stift in der Mitte des Blattes

Das Blatt ist 1000 mal 1000 Einheiten (Pixel) gross. Links oben ist 0, 0. Rechts unten ist 1000, 1000.

Es gibt drei Beispiele, die du anschauen und ausprobieren kannst:

`namen.py` schreibt die Initialen D B. Kannst Du deine eigenen Initialen schreiben? Es hilft 
vielleicht, eine Skizze auf einem Papier zu machen um kein Durcheinander zu kriegen.

`spriale.py` zeichnet eine einfache Spirale. Kannst du sie verändern? Zum Beispiel die Farbe?
jedes Stück der Spirale mit einer anderen Farbe?

`muster.py` zeichnet schöne Muster. Du kannst die Variablen a, b, c, d verändern und beobachten
was passiert.
