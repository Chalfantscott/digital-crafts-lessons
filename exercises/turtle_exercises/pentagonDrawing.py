from turtle import *

begin_fill()
fillcolor('purple')

def drawPentagon(size):
    
    for i in range(5):
        forward(size)
        left(72)
    
drawPentagon(100)

end_fill()

mainloop()