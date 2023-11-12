from gpanel import * 

# s ist der abstand
s = 40
        #    0    1  2    3  4   5    6   7   8   9
abstaende = [10, 20, 30, 20, 10, 20, 30, 20, 10, 20]

def parallelen():
    for i in range(10):
        setColor("gray")
        #Erzeugt mit einen abstand von s graue Linien. I ist die Anzahl der Linien.
        line(0, 5 + i*s, 640, 5 + i*s)
    
def achtQuadrate(x, y):
    for i in range(8):
        setColor("black")
        fillRectangle(x + 2*i*s, y, x + 2*i*s + s, y+s)
        
makeGPanel(0, 640, 0, 640)
parallelen()

for j in range(9):
    #for x in range(9):
    achtQuadrate(abstaende[j], 5+j*s)
    
