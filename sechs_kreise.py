from gpanel import *

s = 40 # Seitenlänge eines Quadrates
a = 10 # Abstand zwischen den Quadraten
radius = a/2

def siebenQuadrate(x, y):
    setColor("black")
    for i in range(7):
        fillRectangle(i*(s+a) + x, y, i*(s+a) +x+ s, y+s)
        
def sechsKreise(X, Y)    
    
        
makeGPanel(0, 500, 0, 500)
bgColor("deepSkyBlue")
for j in range(7):
    siebenQuadrate(10, 5 + j*(s+a))