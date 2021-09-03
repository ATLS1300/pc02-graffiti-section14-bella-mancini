#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
turtle.clear()
turtle.up()
turtle.setpos(-71,60)
turtle.down()
turtle.color(192,192,192)
turtle.pensize(3)
turtle.circle(-20)
turtle.up()
turtle.setpos(-48,118)
turtle.pendown()
turtle.color(0,0,0)
turtle.pensize(6)
turtle.begin_fill()
turtle.forward(50)
turtle.right(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(20)
turtle.end_fill()
turtle.up()
turtle.setpos(70,120)
turtle.down()
turtle.begin_fill()
turtle.left(90)
turtle.forward(45)
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(45)
turtle.left(90)
turtle.forward(20)
turtle.end_fill()
turtle.up()
turtle.setpos(2,108)
turtle.down()
turtle.right(90)
turtle.forward(25)
turtle.up()
turtle.setpos(-48,108)
turtle.down()
turtle.right(180)
turtle.setpos(-74,112)
turtle.up()
turtle.setpos(100,-80)
turtle.down()
turtle.color(100,0,0)
turtle.pensize(1)
turtle.begin_fill()
turtle.left(90)
turtle.forward(14)
turtle.left(90)
turtle.forward(15)
turtle.left(45)
turtle.forward(10)
turtle.left(90)
turtle.forward(10)
turtle.left(45)
turtle.forward(15)
turtle.end_fill()
















#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
# turtle.done()
