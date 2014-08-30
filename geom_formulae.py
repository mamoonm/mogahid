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
    return pi*radius**2
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

print(triangle_area(2,4))

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
    return 4*pi*radius*radius*radius/3
print(sphere_volume(6))