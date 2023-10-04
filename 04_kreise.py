from gpanel import *

makeGPanel(0, 20, 0, 20)


r1 = int(input("Radius des hinteren Kreises: "))
r2 = int(input("Radius des forderen Kreises: "))



setColor("red")
fillCircle(10, 10, r1)
setColor("blue")
fillCircle(10, 10, r2)

