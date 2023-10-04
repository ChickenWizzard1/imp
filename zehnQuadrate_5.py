from gpanel import *
makeGPanel(0, 200, 0, 200)

def zehnQuadrate(x, y):
    for i in range(10):
        move(10*i + x + 5, y + 5)
        rectangle(10, 10)


for i in range(0, 10):
    zehnQuadrate(i*10, i*10)