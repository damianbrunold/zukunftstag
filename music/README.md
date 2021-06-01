# Anleitung Musik

Bei diesem Thema geht es darum mit Tönen und Musik zu experimentieren.
Dazu musst du dem Computer genau sagen, was er machen soll. Dies geschieht,
indem du ein Programm schreibst.

Du kannst im folgenden mit verschiedenen Programmen experimentieren. Ich gebe dir hier
aber noch ein bisschen Hintergrund über Musik und Töne. Was passiert eigentlich wenn ein
Lautsprecher einen Ton abspielt? Der Lautsprecher besteht im wesentlichen aus einem Karton,
der sich hin und her bewegen kann. Man macht dies typischerweise mit einem Elektromagneten.
Damit kann man über einen Strom steuern, wie stark der Karton nach vorne oder hinten gezogen
wird.

Wenn man den Karton nun 440 mal pro Sekunde nach vorne und hinten zieht, wird die Luft
gedrückt und gezogen und diese Druckveränderungen erreichen unser Ohr. Das Ohr erkennt
dann aufgrund der 440 Schwingungen, dass es sich um den Ton a' handelt.

Im Computer drücken wir das nach vorne und nach hinten ziehen des Kartons mit Zahlen
aus: 1 heisst, dass der Karton ganz nach vorne gezogen ist, -1 heisst, dass er ganz nach
hinten gedrückt ist. 0 heisst, dass er in der Mitte ist und Zahlen zwischen -1 bis 1 sind
für entsprechend starke Teilauslenkungen.

Wir können nun Töne programmieren, indem wir dem Computer eine lange Liste mit Zahlenwerten
geben, die die Auslenkungen des Kartons angeben. Der Computer erzeugt daraus dann einen Strom,
der den Lautsprecher exakt so lenkt und damit den Ton erzeugt.

Im folgenden haben wir eine Serie von Beispielprogrammen, die von einfachen Tönen
bis zu einem komplexen Song reichen. Du kannst mit all diesen Beispielprogrammen spielen,
sie verändern und erweitern.

`ein_ton.py` erzeugt einen einzelnen Ton. Du kannst die Tonhöhe oder Tondauer 
verändern und auch den Klang des Tones.

`tonleiter.py` erzeugt eine Tonleiter. So siehst du, wie man mehrere Töne nacheinander
erzeugt. Verändere die Tonleiter oder mache sie schneller oder langsamer.

`sirene.py` erzeugt ein Geräusch ähnlich einer Polizeisirene (Tatüü).

`wuuu.py` Lässt den Klang zwischen zwei Tonhöhen hin- und herwandern.

`akkord.py` Lässt drei Töne gleichzeitig erklingen (ein Akkord). Kannst du einen anderen
Akkord erzeugen indem du die Tonhöhen änderst?

`dancetrack.py` Dieses Programm führt alle Techniken zusammen und erzeugt einen
Track/Song, der aus Schlagzeug, Bass und Orgelakkorde besteht. Du kannst zum Beispiel den Bassrythmus
verändern oder die Orgelakkorde ändern. Oder du führst eine weitere Stimme ein. Oder du machst das
Schlagzeug komplexer. Es gibt unendlich viele Möglichkeiten.

`klang_anzeigen.py` ist ein Programm, das vier Töne spielt und dann deren Schwingungen
am Bildschirm anzeigt.

Es gibt folgende Befehle:

- `stille(dauer)` erzeugt eine Stille (also keinen Ton) für die angegebene Dauer
- `rauschen(dauer)` Erzeugt ein Rauschen
- `ton(frequenz, dauer)` Erzeugt einen normalen Ton (also mit Obertönen)
- `ton_sinus(frequenz, dauer)` Erzeugt einen reinen Ton der nur eine Frequenz enthält
- `ton_saege(frequenz, dauer)` Erzeugt einen sogenannten Sägezahnton, der scherbelig tönt
- `bereich_sinus(freq1, freq2, dauer)` Erzeugt einen Tonübergang von der ersten zur zweiten Tonhöhe (Frequenz)
- `bereich_saege(freq1, freq2, dauer)` Erzeugt einen Tonübergang von der ersten zur zweiten Tonhöhe (Frequenz)
- `bumm(dauer)` Erzeugt einen Bassdrum-Ton
- `mix2(a, b)` Mischt die Töne a und b zu einem neuen Ton
- `mix3(a, b, c)` Mischt die Töne a, b und c zu einem neuen Ton
- `mix4(a, b, c, d)` Mischt die Töne a, b, c und d zu einem neuen Ton
- `abspielen(a)` Spielt die mit den anderen Befehlen erzeugte Musik a ab.

Die Befehle sind in der Datei `music.py` definiert. Wenn du Lust hast, kannst du
schauen, wie sie programmiert sind. Bei Fragen helfe ich gerne weiter.

Wenn ein Befehl eine Tonhöhe resp. Frequenz benötigt, kannst du entweder direkt eine Zahl angeben
(zum Beispiel 440) oder du gibst vordefinierte Tonhöhen an. Die definierten Höhen sind in der Datei
`toene.py` zu sehen. Grundsätzlich kannst du die normalen Tonnamen (c, d, e, f, fis, ges, ...)
mit 0, 1 oder 2 angehängt verwenden. Also beispielsweise dis2 für ein hohes dis.
