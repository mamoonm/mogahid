__author__='mogahid'
import math
from numbers import Number
from numpy import *

def circle_area(radius: Number) ->Number:
    """
    Calculates the area of a circle given the radius
    :param radius: radius of the circle
    :return: area of the circle(in units of radius)

    """
    return math.pi*radius**2
print(circle_area(7))

def triangle_area(base, height):
    """
    calculate are of a triangle
    :param base: base of a triangle
    :param heigh: heigh of a triangle
    :return:area of atringle
    >>> triangle_area(4, 5)
    """
    return 0.5*base*height

print(triangle_area(4,5))

def rectangle_area(length,width):
    """
    calculates the area of rectangle
    :param length: length of a rectangle
    :param width: width of a rectangle
    :return:area of a rectangle
    >>> rectangle_area(4, 2)
    8
    """
    return length*width
print(rectangle_area(4, 2))

def sphere_volume(radius):
    """
    calculate the area of sphere
    :param radius: radius of sphere
    :return:the volume of the sphere(in cubic units of the radius)
    >>> sphere _volume
        1436.7550402417319
    """
    return 4*math.pi*radius*radius*radius/3
print(sphere_volume(7))

def cone_volume(radius, height):
    """
    calculate the volume of cone.
    :param radius: radius of cone
    :param height: height of cone
    :return:the volume  of the cone
    """

    return 4*radius*radius*height*0.333
print(cone_volume(3,4))

def cylinder_area(radius, height):
    """
    calculate the area of cylinder
    :param radius: radius of a cylinder
    :param height: height of a cylinder
    :return:the area of the cylinder
    """
    return 2*math.pi*(radius**2)*height


if __name__ == "__main__":
    sampleradius = 4
    sampleheight = 7
    print("the area is :", cylinder_area(sampleradius, sampleheight))

def trapezium_area(b1,b2,height):
    """

    :param b1: upper side of trapezium
    :param b2: lower side of trapezium
    :param height: height of trapezium
    :return:area (units^2 from height,b1 or b2)
    >>> trapezium_area(2,3,5)
    12.5
    """
    return 0.5*(b1+b2)*height
print(trapezium_area(2,3,5))

def equal_area(might,side):
    """
    calcluate the area of equal
    :param might: might of a equal
    :param side: side of a equal
    :return:the area of equal
    """
    return (might+side)*2
print(equal_area(3,4))

def pentagon_area(side,height):
    """

    :param side: side of a pentagon
    :param height: height a pentagon
    :return:the area of pentagon(unit^2 from side or height)
    """
    return 0.5*side*height*5
print(pentagon_area(4,6))

def cube_area(side):
    """

    :param side:side of a cube
    :return:the area of a cube
    """
    return side*6
print(cube_area(3))