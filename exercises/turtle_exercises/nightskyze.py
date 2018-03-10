import turtle

tina=turtle.Turtle()

#This makes the background color black to represent the night sky
myscreen = turtle.Screen()
myscreen.bgcolor("black")
tina.speed(8)

#Getting into place to draw the hills
tina.penup()
tina.right(90)
tina.forward(200)
tina.right(90)
tina.forward(200)
tina.right(90)

#This is where we draw the hills with some semicircles
tina.pendown()
tina_color = raw_input("What color do you want the hills to be?")
tina.color(tina_color)
tina.fill(True)
for x in range(180):
    tina.forward(1)
    tina.right(1)
tina.right(180)
for x in range(180):
    tina.forward(1)
    tina.right(1)
tina.right(180)
for x in range(180):
    tina.forward(1)
    tina.right(1)
tina.right(180)
for x in range(180):
    tina.forward(1)
    tina.right(1)
tina.fill(False)

#Getting into position to draw some stars
tina.right(180)
tina.penup()
tina.forward(400)
tina.pendown()

#Time to draw some stars
def draw_star(size, color):
    angle = 120
    tina.fillcolor(color)
    tina.begin_fill()

    for side in range(5):
        tina.forward(size)
        tina.right(angle)
        tina.forward(size)
        tina.right(72 - angle)
    tina.end_fill()
    return

draw_star(25, "yellow")

tina.penup()
tina.goto(150,100)
tina.pendown()

draw_star(25, "yellow")

tina.penup()
tina.goto(5,150)
tina.pendown()

draw_star(25, "yellow")

tina.penup()
tina.goto(30,50)
tina.pendown()

draw_star(25, "yellow")

tina.penup()
tina.goto(-150,50)
tina.pendown()

draw_star(25, "yellow")

tina.penup()
tina.goto(-100,-75)
tina.pendown()

draw_star(25, "yellow")

#Time for some final words
tina.right(90)
tina.penup()
tina.forward(150)
tina.pendown()
tina.write("Wish upon a star...", None, "center", "16pt bold")
