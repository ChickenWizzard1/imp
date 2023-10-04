from gpanel import * 

makeGPanel(0, 200, 0, 200)

for i in range(10):
    move(10*i+5, 50)
    rectangle(10, 10)
    
    move(10*i+5, 70)
    rectangle(10, 10)
    
    move(10*i+5, 80)
    rectangle(10, 10)

