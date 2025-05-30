
'''
Ubicación: app/core/Collision.py
Propósito: Detectar si dos elipses se intersectan o están demasiado cerca (potencial colisión).
- Calcular distancia entre centros.
- Comparar con la suma de radios (aproximados).
- Usaremos semiejes mayores como radios de influencia.

Esta es una aproximación adecuada para el contexto del proyecto.

'''
# core/Collision.py

from .Math_ellipse import Elipse

def punto_en_elipse(x, y, elipse: Elipse) -> bool:
    """
    Verifica si un punto (x, y) está dentro de la elipse.
    Usamos su ecuación canónica.
    """
    dx = x - elipse.h
    dy = y - elipse.k

    if elipse.orientacion == "horizontal":
        valor = (dx**2) / (elipse.a**2) + (dy**2) / (elipse.b**2)
    else:
        valor = (dx**2) / (elipse.b**2) + (dy**2) / (elipse.a**2)

    return valor <= 1  # Si está dentro o sobre la elipse

def hay_colision(e1: Elipse, e2: Elipse) -> bool:
    """
    Verifica si hay colisión entre dos elipses.
    Evalúa si algún punto de e1 está dentro de e2 o viceversa.
    """
    puntos1 = e1.calcular_puntos(100)
    puntos2 = e2.calcular_puntos(100)

    for x, y in puntos1:
        if punto_en_elipse(x, y, e2):
            return True

    for x, y in puntos2:
        if punto_en_elipse(x, y, e1):
            return True

    return False

def tipo_colision(e1: Elipse, e2: Elipse) -> str:
    if hay_colision(e1, e2):
        return "⚠️ Posible colisión entre trayectorias"
    else:
        return "✅ Trayectorias seguras"
