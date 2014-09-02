__author__ = 'mamoon'
from pylab import *

from geom_formulae import *

v_trapezium_area = np.vectorize(trapezium_area)
#v__square_perimeter = np.vectorize(trapezium_perimeter)

H = np.linspace(0,10) # our side lengths

A = v_trapezium_area(4,5,H)  # the areas
#P = v_square_perimeter(S)  # the perimeters

plot(H, A, '-r', label="Area")
#plot(S, P, ':b', label="Perimeter")

xlabel('side length')
ylabel('geo values')
title('Square Geo Properties')
legend(loc='upper right')

show()
