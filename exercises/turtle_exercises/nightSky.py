from turtle import *

bgcolor('purple4')

def draw_star(size, color):
    fillcolor("white")
    begin_fill()

    for side in range(5):
        forward(size)
        right(120)
        forward(size)
        right(72 - 120)
    end_fill()

draw_star(5, "white")

up()
goto(120,100)
down()

draw_star(5, "white")

up()
goto(20,110)
down()

draw_star(5, "white")

up()
goto(5,150)
down()

draw_star(5, "white")

up()
goto(30,50)
down()

draw_star(5, "white")

up()
goto(-150,50)
down()

draw_star(5, "white")

up()
goto(-160,-175)
down()

draw_star(5, "white")

up()
goto(-40,80)
down()

draw_star(5, "white")

up()
home()

mainloop()