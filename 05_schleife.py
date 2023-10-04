# 1) Betrachte zunächst nur den Programm-Code. Was macht das Programm? Überprüfe deine Vermutung.
# 2) Verändere das Programm so, dass die Radien der Kreise zunehmen, die Kreise sich aber weiter nicht berühren.

from gpanel import * 

makeGPanel(0, 120, 0, 120)

bgColor("gray")
setColor("red")
i = 1

repeat 10:
    fillCircle(i*i, i*i, i)
    i = i + 1 
    
# Vermutung: Kreis startet bei (1|1) und geht jedes mal 2-mal in x und y richtung nach oben.
    




