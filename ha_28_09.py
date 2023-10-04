from gpanel import *
makeGPanel(0, 80, 0, 80)
for i in range(1, 81):
    line(2*i, 0, 2*i, 80)
    #line(i, 0, 80-i, 80)
    #line(i, 0, 80, i)