from gpanel import *

makeGPanel(0, 200, 0, 200)

def zehnQuadrate(y):
    for i in range(10):
        move(10*i + 5,y)
        rectangle(10, 10)



zehnQuadrate(50)
zehnQuadrate(70)
zehnQuadrate(80)