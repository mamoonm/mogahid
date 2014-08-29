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






