'''
 # Tests para colisión

'''
from app.core.Math_ellipse import Elipse
from app.core.Collision_ellipse import elipses_colisionan

def test_colision_elipses():
    rut1 = "13.457.812-9"
    rut2 = "45.678.921-3"
    rut3 = "23.987.634-2"
    
    e1 = Elipse(0, 0, 3, 2, "horizontal")
    e2 = Elipse(2, 0, 3, 2, "horizontal")
    assert elipses_colisionan(e1, e2)

test_colision_elipses()