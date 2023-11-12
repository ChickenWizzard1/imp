from gpanel import * 

s = 40 # Seitenlänge eines Quadrates
d = s/6 #Abstand der kreismittelpunkte vom Rand des Quadrats
r = 4 # Radius der kreise

def zeichneQuadrat(x, y, schwarz, links): # Funktion erzeugt ein Quadrat mit zwei Punkten 
    if schwarz == True:
        setColor("black")
        move(x, y)
        fillRectangle(s, s)
        if links == False:
            setColor("white")
            fillCircle(s-x-d, s-y-d, r)
            fillCircle(s-x-d, y-d, r)
        else:
            setColor("white")
            fillCircle(d, s-y-d, r)
            fillCircle(d, y-d, r)
           
    
    else:
        setColor("white")
        move(x, y)
        fillRectangle(s, s)
        if links == False:
            setColor("black")
            fillCircle(s-x-d, s-y-d, r)
            fillCircle(s-x-d, y-d, r)
        else:
            setColor("black")
            fillCircle(d, s-y-d, r)
            fillCircle(d, y-d, r)
        



            
makeGPanel(0, 500, 0, 500) # Zeichenfenster
bgColor("gray")
zeichneQuadrat(10, 10, False, True)