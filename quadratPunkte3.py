from gpanel import * 

s = 40 # Seitenlänge eines Quadrates
d = s/6
r= 4
def zeichneQuadrat(x, y, schwarz, links): # Funktion erzeugt ein Quadrat mit zwei Punkten 
    if schwarz == True: # Farbauswahl Quadrat
        setColor("black")
    else:
        setColor("white")
    fillRectangle(x, y, x + s, y + s)
    
    if schwarz == True: 
        setColor("White")
    else:
        setColor("black")
    if links == True:
        fillCircle(x+d, y +d, r)
        fillCircle(x +d, y+s-d,r)
    else:
        fillCircle(x+s-d, y+d, r)
        fillCircle(x+s-d, y+s-d, r)


def quadratreihe(x, y, startSchwarz, links):
    schwarz = startSchwarz    
    for i in range(8):
        for j in range(4):
            zeichneQuadrat(x+i*s, j*y+s, schwarz, links)
            
        if schwarz == True:
            schwarz = False
        else:
            schwarz = True
        
    

makeGPanel(0, 500, 0, 500) # Zeichenfenster
bgColor("gray")
quadratreihe(10, 10, False, True)
#quadratreihe(10, 10+s, False, True)