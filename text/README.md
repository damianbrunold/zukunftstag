# Anleitung Text

Hier geht es um das Erzeugen von Briefen. Das ist unser Hauptgeschäft:
Grosse Firmen schicken uns Kunden- und Rechnungsdaten und wir machen daraus
Rechnungsbriefe und drucken die aus.

In unserem Beispiel haben wir eine Datei mit Daten, wie sie von der Firma
kommen könnte und wir müssen diese Daten aufbereiten und dann drucken.

Die Daten liegen als Textdatei `daten.txt` vor. Sie sehen so aus:

```
briefstart
sprache,deutsch
name,Fritz Fischer
adresse,Meisenhof 7
plzort,7788 Freihofen
anrede,Sehr geehrter Herr Fischer
text,Wir gratulieren ganz herzlich zum Geburtstag.
text,Alles Gute auf dem weiteren Lebensweg.
text,
text,Herzliche Grüsse
text,
text,SwissTelco AG
briefend
briefstart
sprache,englisch
name,Lucy Spacey
adresse,Friedhof 5
plzort,8000 Zürich
anrede,Dear Ms. Spacey
text,Congratulations on your birthday.
text,All the best.
text,
text,Best regards
text,
text,SwissTelco AG
briefend
briefstart
sprache,franzoesisch
name,Camille Bloch
adresse,Rue du pompieres 12
plzort,2345 Lully
anrede,Cher Camille
text,Félicitations pour votre anniversaire.
text,Heureux dans leur vie future.
text,
text,Cordialement
text,
text,SwissTelco SA
briefend
```

In `einlesen.py` werden diese Daten gelesen und als einzelne Briefobjekte
zur Verfügung gestellt. Das Beispielprogramm druckt die Daten der deutschen Briefe aus.
Kannst du das Programm ändern, sodass es die englischen Briefe ausgibt?

Das Programm `brief_anzeigen.py` nimmt nun eines der eingelesenen Briefobjekte
und rendert die Daten. Das heisst, stellt die Daten auf einem A4-Papier dar. Dazu müssen
die verschiedenen Briefelemente wie Adresse, Anrede und Textzeilen auf dem Blatt angeordnet
werden. Kannst du die Adresse nach ganz links schieben? Kannst du eine Absenderadresse
hinzufügen zuoberst auf der Seite?
