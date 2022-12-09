import turtle 
import math

turtle.shape("turtle")
turtle.bgcolor("dark red")
turtle.speed(1)
def reg_polygon(start_pos, number_of_angles, side):
    interior_angle = (180 * (number_of_angles - 2)) / number_of_angles
    turtle.setheading(180 - interior_angle//2)

    for i in range(number_of_angles):
        turtle.pencolor("yellow")
        turtle.width(1.5)
        turtle.forward(side)
        turtle.left(180 - interior_angle)
    
def reset_start_point():
    global start_pos, startx, starty, initial_size, number_of_angles, side
    startx += 8
    starty -= 0
    initial_size += 8
    number_of_angles += 1
    side = 2 * initial_size * math.sin(math.radians(180/number_of_angles))
    start_pos = startx, starty
    turtle.penup()
    turtle.goto((startx, starty))
    turtle.pendown()
    
start_pos = startx, starty = 0, 0
number_of_angles = 2
initial_size = 15  # radius
side = 0

while number_of_angles < 12:
    reset_start_point()
    reg_polygon(start_pos, number_of_angles, side)
    
turtle.done()