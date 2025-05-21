'''
 # Tests para colisión

'''
from app.core.Math_ellipse import Elipse
from app.core.Collision_ellipse import elipses_colisionan

def test_colision_elipses():
    e1 = Elipse(0, 0, 3, 2, "horizontal")
    e2 = Elipse(2, 0, 3, 2, "horizontal")
    assert elipses_colisionan(e1, e2)