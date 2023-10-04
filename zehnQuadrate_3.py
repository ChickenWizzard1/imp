from gpanel import *
makeGPanel(0, 200, 0, 200)

def zehnQuadrate(x, y):
    for i in range(10):
        move(10*i + x + 5, y)
        rectangle(10, 10)



zehnQuadrate(0, 50)
zehnQuadrate(30, 70)
zehnQuadrate(10, 80)