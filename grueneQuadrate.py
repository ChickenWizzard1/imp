from gpanel import *
makeGPanel(0, 800, 0, 800)
s =  40 # seitenlänge großes  quadrat
d = s/6 # abstand vom kleinen quadrat zum großen quadrat


setColor("black")
lineWidth(10)




def zeichneQuadrat(x, y,  gruen):
    if gruen == True:
        setColor("green")
    else:
        setColor("white")
    fillRectangle(x, y, x+s, y+s)
    if gruen == True:
        setColor("white")
    else: setColor("green")
    fillRectangle(x+d, y+d, x+s-d, y+s-d)


x = 0        
while x < 14:
    zeichneQuadrat(x*s, 0, True)
    x = x + 1
    zeichneQuadrat(x*s, 0, False)