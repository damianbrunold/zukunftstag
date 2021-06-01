# Anleitung Barcodes

Barcodes sind überall verbreitet. Fast jedes Produkt im Migros ist mit einem 
EAN Code bedruckt. Auch bei uns wird viel mit Barcodes gearbeitet. In diesem Projekt
geht es um das erzeugen und das analysieren von Barcodes.

Es gibt sehr viele verschiedene Barcodeformate. Wir behandeln nur einen davon, den Code `128 B`.

Das Programm `erzeugen.py` erstellt einen Barcode und zeigt ihn an.
Kannst du das Programm ändern sodass ein anderer Text verwendet wird? Kannst du den Code kleiner
machen?

Die Datei `raetsel.png` enthält einen Barcode. Kannst du herausfinden
was er beinhaltet? Du kannst entweder versuchen ihn mit einem Scanner zu scannen, oder du kannst
mit den Informationen in der Datei `infos.txt` versuchen herauszufinden was
der Code für einen Text beinhaltet. Hinweis: Der Code besteht aus schwarzen und weissen Linien,
wobei jeweils 11 davon einen Buchstaben darstellen. Der erste "Buchstabe" ist speziell, heisst
"Start B" und zeigt an, dass nun ein Barcode vom Typ B kommt (es gibt auch Typen A und C). Danach
folgen die Buchstaben, danach eine Checksumme, die du ignorieren kannst. Der abgebildete Lineal
hilft dir die Elfergruppen zu zählen. Falls du nicht weiterkommst, kannst du uns fragen.
