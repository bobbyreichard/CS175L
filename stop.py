#Start
import math
import turtle
#named constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 45
TEXT_X = -5
TEXT_Y = -10
#Size Window
turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
s = 100
x = s / math.sqrt(2)
diameter = s + (2 * x)
#Draw Using Turtle
turtle.up()
turtle.setpos(-50,100)
turtle.down()
for x in range(8):
    turtle.forward(100)
    turtle.right(45)
turtle.up()
turtle.setposition(-10,-25)
turtle.down()
turtle.write('STOP')
#End
