# 1) Betrachte zunächst nur den Programm-Code. Was macht das Programm? Überprüfe deine Vermutung.
# 2) Verändere das Programm so, dass die Radien der Kreise zunehmen, die Kreise sich aber weiter nicht berühren.

from gpanel import * 

makeGPanel(0, 20, 0, 20)

bgColor("gray")
setColor("red")
i = 1
x = 1
y =  1
for i in range(1, 22, 2):
    fillCircle(y, y, x)
    x = x + 0.2
    y = y + x + 1
    