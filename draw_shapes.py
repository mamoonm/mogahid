__author__ = 'mamoon'
import turtle

def draw_circle(radius):
    turtle.circle(100)
    turtle.done()

def draw_rectangle_area(side,width):
     i = 0
     while (i<4):
         turtle.forward(side)
         turtle.left(90)
         i = i+1
     turtle.done()

def draw_trapezim_ ( height, side):
    turtle.forward(150)
    turtle.left(80)
    turtle.forward(60)
    turtle.left(100)
    turtle.forward(55)
    turtle.left(100)
    turtle.home()
    turtle.done()

if __name__ == "__main__":
    draw_circle(100)
    draw_trapezim_(50, 50)
    draw_rectangle_area(100, 50)

def draw_square(side):
    i=0
    while (i<4):
        turtle.forward(side)
        turtle.left(90)
        i = i+1
    turtle.done()
draw_square(60)

import turtle
def draw_triangle(side):
       turtle.forward(100)
       turtle.left(120)
       turtle.forward(80)
       turtle.home()
       turtle.done()
#if __name__ =="__main__":
draw_triangle(100)

def draw_parallelogram(length,width):
       turtle.forward(length)
       turtle.left(60)
       turtle.forward(width)
       turtle.left(120)
       turtle.forward(length)
       turtle.left(60)
       turtle.home()
       turtle.done()
draw_parallelogram(100,70)

def drow_pentagon(side):
    i = 0
    while (i < 5):
        side=50
        turtle.forward(side)
        turtle.left(72)
        i = i+1
        turtle.done
