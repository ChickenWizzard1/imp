from gpanel import *

makeGPanel(0, 80, 0, 80)


for i in range(1, 41):
   rectangle(40+i, 40+i, 40-i, 40-i)