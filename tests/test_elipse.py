'''
# Tests unitarios para elipse 
'''
from app.core.Math_ellipse import Elipse

def test_area():
    e = Elipse(0, 0, 3, 2, "horizontal")
    assert abs(e.area() - (3.1416 * 3 * 2)) < 0.01
