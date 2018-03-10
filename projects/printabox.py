width = 10
height = 5

for row in range(height):
    if row == 0 or row == height - 1:
        print "*" * width
    else: 
        spaces = width - 2
        print "*" + " " * spaces + "*"