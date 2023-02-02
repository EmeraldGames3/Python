"""
A
Zwei algorithmen kann man nach ihren komplexitat vergleichen. Sowohl die komplexitat im Bezug des Laufzeites
als auch die Komplexitat im Bezug des benutzten des Speichers

Die Laufzeit eines Algorithmus kann man in mehreren Arten definieren durch die Asimptotische komplexitat
Die asimptotische komplexitat bezieht sich auf die Asymptoten des Graphen gebildet aus der Laufzeit des Algorithmus
und die Anzahl der Operationen. Man bezeichnet mit O(f(n)) den Schlechtesten moglichen Fall eines Algorithmus
bezuglich der Laufzeitkomplexitat und mit omega den besten moglichen Fall, also diese sind die Zwei Asymptoten die
den Funktion beschranken. Man kann einen Algorithmus auch nach seinem mittleren laufzeit Komplexitat analysieren

Zum Beispiel, die Bubble sort hat einen O(n^2) Komplexitat im schlechtesten Fall, ein O(n^2) im mittleren Fall
und eine Komplexitat von O(n) im besten Fall.
Selection sort hat immer eine Komplexitat von O(n^2) im allen Fallen.

B
List comperhension ist eine Methode neue listen zu erzeugen aus existierende iterablen in Python.
Man nutzt solche Ausdrucke meistens um neue Listen zu erzeugen.
"""

x = [1,2,3]
y = "123"

x1 = [i*3 for i in x]
y1 = [i*2 for i in y]

print(x1)
print(y1)