__author__ = 'mamoon'
from pylab import *

from geom_formulae import *

v_cube_area = np.vectorize(cube_area)
#v__square_perimeter = np.vectorize(cube_perimeter)

S = np.linspace(0,10) # our side lengths

A = v_cube_area(S)  # the areas
#P = v_square_perimeter(S)  # the perimeters

plot(S, A, '-r', label="Area")
#plot(S, P, ':b', label="Perimeter")

xlabel('side length')
ylabel('geo values')
title('Square Geo Properties')
legend(loc='upper right')

show()