from gpanel import * 

# s ist der abstand
s = 40

def parallelen():
    for i in range(10):
        setColor("gray")
        #Erzeugt mit einen abstand von s graue Linien. I ist die Anzahl der Linien.
        line(0, 5 + i*s, 640, 5 + i*s)
    
def achtQuadrate(x, y):
    for i in range(1, 22, 2):
        setColor("black")
        move(x + i*s, y)
        rectangle(0, y+s)
        
makeGPanel(0, 640, 0, 640)
parallelen()
achtQuadrate(10, 5)

