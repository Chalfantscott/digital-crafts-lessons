def drawTriangle(height):
    base = height * 2 - 1
    for row in range(1, height + 1):
        spaces = height - row
        print " " * spaces + "*" * (row * 2 - 1)

def drawBox(width, height):
    for row in range(height):
        if row == 0:
            print "*" * width
        elif row == height - 1:
            print "*" * width
        else:
            spaces = width - 2
            print "*" + " " * spaces + "*"

shapeToPrint = raw_input("Pick a shape to print: triangle, box, or square. ")

if shapeToPrint == "triangle":
    height = int(raw_input("What is the height? "))
    drawTriangle(height)
if shapeToPrint == "box":
    height = int(raw_input("What is the height? "))
    width = int(raw_input("What is the width? "))
    drawBox(width, height)



