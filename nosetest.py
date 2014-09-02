__author__ = 'mamoon'
from geom_formulae import *
from nose.tools import *

"""
def test_square_area_int():
    assert square_area(1) == 1
    assert square_area(4) == 16
    s = 5
    assert square_area(s*2) == 4*square_area(s)


eps = 1e-6
def test_square_area_double():
    assert 25/4 - eps < square_area(2.5) < 25/4 + eps



def test_fail_square_perimeter():
    assert square_perimeter(4) == 20
"""


def test_circle_area_int():
    assert circle_area(1) == 1 * pi
    assert circle_area(7) == 49 * pi



eps = 1e-6
def test_circle_area_double():
    assert (4/9 * pi) - eps < circle_area(2/3) < (4/9 * pi) + eps



def test_triangle_area_int():
    assert triangle_area(4, 1) == 2
    assert triangle_area(2, 2) == 2


def test_rectangle_area_int():
    assert rectangle_area(1, 4) == 4
    assert rectangle_area(4, 6) == 24


#def test_fail_rectangle_perimeter():
 #   assert rectangle_perimeter(4) == 20






def test_sphere_area_double():
    assert sphere_area(0) == 0
    assert sphere_area(1) == 4*pi
    s = 5
    assert sphere_area(s*2) == 4*sphere_area(s)


eps = 1e-6
def test_spheree_area_double():
    assert 25/4 - eps < sphere_area(2.5) < 25/4 + eps

#def test_fail_sphere_perimeter():
 #   assert sphere_perimeter(4) == 20



def test_cone_volume_int():
    assert cone_volume(1) == 1
    assert cone_volume(4) == 64


eps = 1e-6
def test_cone_volume_double():
    assert 25/4 - eps <  cone_volume(2.5) < 25/4 + eps

#def test_fail_cone_volume():
 #   assert  cone_volume(4) == 20







