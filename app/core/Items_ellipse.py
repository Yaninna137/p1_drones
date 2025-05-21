'''
Extender la elipse, este almacena la logica de visualización de datos
- Elementos de la elipse
- Puntos de a graficar
'''

# elipse_visual.py

from .Math_ellipse import Elipse

class ElipseVisual(Elipse):
    def obtener_elementos(self) -> dict:
        if self.a < self.b:
            return 0

        c = ((self.a**2) - (self.b**2)) ** 0.5
        focos = [(self.h + c, self.k), (self.h - c, self.k)] if self.orientacion == 'horizontal' else [(self.h, self.k + c), (self.h, self.k - c)]
        vertices_p = [(self.h + self.a, self.k), (self.h - self.a, self.k)] if self.orientacion == 'horizontal' else [(self.h, self.k + self.a), (self.h, self.k - self.a)]
        vertices_s = [(self.h, self.k - self.b), (self.h, self.k + self.b)] if self.orientacion == 'horizontal' else [(self.h + self.b, self.k), (self.h - self.b, self.k)]

        return {
            'c': c,
            'focos': focos,
            'vertices_principales': vertices_p,
            'vertices_secundarios': vertices_s,
            'eje_mayor': 2 * self.a,
            'eje_menor': 2 * self.b,
            'eje_focal': 2 * c,
            'orientacion': self.orientacion,
        }

    def puntos_con_etiquetas(self):
        """
        Devuelve una lista de tuplas (x, y, etiqueta) con los puntos característicos de la elipse.
        """
        elementos = self.obtener_elementos()
        puntos = []
        if elementos == 0:
            return puntos

        # Focos
        puntos.append((*elementos["focos"][0], "F"))
        puntos.append((*elementos["focos"][1], "F'"))

        # Vértices principales
        puntos.append((*elementos["vertices_principales"][0], "V"))
        puntos.append((*elementos["vertices_principales"][1], "V'"))

        # Vértices secundarios
        puntos.append((*elementos["vertices_secundarios"][0], "B"))
        puntos.append((*elementos["vertices_secundarios"][1], "B'"))

        # Centro
        puntos.append((self.h, self.k, "C"))

        return puntos
