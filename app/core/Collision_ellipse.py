
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

def hay_colision(e1: Elipse, e2: Elipse) -> bool:
    dx = e1.h - e2.h
    dy = e1.k - e2.k
    distancia_centros = (dx**2 + dy**2) ** 0.5

    # Aproximación: usa los semiejes mayores como radios
    radio1 = max(e1.a, e1.b)
    radio2 = max(e2.a, e2.b)

    return distancia_centros < (radio1 + radio2)

def tipo_colision(e1: Elipse, e2: Elipse) -> str:
    if hay_colision(e1, e2):
        return "⚠️ Posible colisión entre trayectorias"
    else:
        return "✅ Trayectorias seguras"
