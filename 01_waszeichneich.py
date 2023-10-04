# 1) Überlege dir, was die Anweisungen auslösen. Führe das Programm erst dann aus.
# 2) Verändere die Werte. Was passiert? 
# 3) Lege ein Vokabelheft mit gpanel-Befehlen an, z.B. line(px, py, qx, qy):  Zeichnet eine Strecke vom Punkt P(px|py) zum Punkt Q(qx|qy). 

from gpanel import * # Lädt das Grafik-Paket gpanel

makeGPanel(0, 40, 0, 40) # Erzeugt ein Grafik-Fenster
line(10, 5, 20, 10)
rectangle(5, 30, 35, 10)
triangle(0, 0, 5, 10, 9, 9)
setColor(255, 0, 0)
fillCircle(20, 20, 5)
# setColor(255, 0, 0)
text(0, 0, "Hurrah!")
