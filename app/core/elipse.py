# core/elipse.py
from dataclasses import dataclass

@dataclass
class Elipse:
    h: int
    k: int
    a: int
    b: int
    orientacion: str  # 'horizontal' o 'vertical'
    
    # EC. CÁNONICA =>
    def ecuacion_canonica(self):
        if self.orientacion == "horizontal":
            return f"\\frac{{(x - {self.h})^2}}{{{self.a ** 2}}} + \\frac{{(y - {self.k})^2}}{{{self.b ** 2}}} = 1"  # Formato latex

        else:
            return f"\\frac{{(x - {self.h})^2}}{{{self.b ** 2}}} + \\frac{{(y - {self.k})^2}}{{{self.a ** 2}}} = 1"  # Formato latex
        
    # EC. GENERAL =>
    def ecuacion_general(self):
        a2 = self.a ** 2
        b2 = self.b ** 2

        if self.orientacion == "horizontal":
            A = b2
            C = a2
        else:
            A = a2
            C = b2

        D = -2 * A * self.h
        E = -2 * C * self.k
        F = A * self.h**2 + C * self.k**2 - a2 * b2

        # Armar la ecuación
        partes = []
        if A != 0: partes.append(f"{A}x²")
        if C != 0: partes.append(f"{C}y²")
        if D != 0: partes.append(f"{'+' if D > 0 else '-'} {abs(D)}x")
        if E != 0: partes.append(f"{'+' if E > 0 else '-'} {abs(E)}y")
        if F != 0: partes.append(f"{'+' if F > 0 else '-'} {abs(F)}")

        return " ".join(partes) + " = 0"

    # SACAR LOS PUNTOS 
    def calcular_puntos(self, n=100,pi=3.141592653589793):
        puntos = []
        for i in range(n):
            t = 2 * pi * i / n
            x = self.h + (self.a * self.seno(t) if self.orientacion == "horizontal" else self.b * self.coseno(t))
            y = self.k + (self.b * self.coseno(t) if self.orientacion == "horizontal" else self.a * self.seno(t))
            puntos.append((x, y))
        return puntos
    
    # SACAR LOS ELEMENTOS
    def Elementos(self):
        if self.a < self.b:
            return 0 # #####
        c = ((self.a**2) - (self.b**2)) ** 0.5  # Formula de c = √a² - b²

        Focos = [(self.h + c, self.k), (self.h - c, self.k)] if self.orientacion == 'horizontal' else [(self.h, self.k + c), (self.h, self.k - c)]  # Lista que almacena la cordenada de focos
        Vertices_p = [(self.h + self.a, self.k), (self.h - self.a, self.k)] if self.orientacion == 'horizontal' else [(self.h, self.k + self.a), (self.h, self.k - self.a)]# Lista que almacena la cordenada de vertice principal
        Vertices_s = [(self.h, self.k - self.b), (self.h, self.k + self.b)] if self.orientacion == 'horizontal' else [(self.h + self.b, self.k), (self.h - self.b, self.k)]# Lista que almacena la cordenada de vertice auxiliar o secundario
        e_mayor = 2*self.a
        e_menor = 2*self.b
        e_focal = 2*c
        orientacion = self.orientacion

        return {
        'c':c,
        'focos': Focos,
        'vertices_principales': Vertices_p,
        'vertices_secundarios': Vertices_s,
        'eje_mayor': e_mayor,
        'eje_menor': e_menor,
        'eje_focal': e_focal,
        'orientacion': orientacion
    }
    
    # FORMULAS MATEMATICAS - MANUALES : factoria,normalizar r, seno, coseno.
    def factorial(self,n):
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    def normalize_radians(self,x):
        pi = 3.141592653589793
        while x > pi:
            x -= 2 * pi
        while x < -pi:
            x += 2 * pi
        return x
    
    def seno(self,x, terms=10):
        x = self.normalize_radians(x)
        result = 0
        for n in range(terms):
            sign = (-1)**n
            term = (x**(2 * n + 1)) / self.factorial(2 * n + 1)
            result += sign * term
        return result
    
    def coseno(self,x, terms=10):
        x = self.normalize_radians(x)
        result = 0
        for n in range(terms):
            sign = (-1)**n
            term = (x**(2 * n)) / self.factorial(2 * n)
            result += sign * term
        return result
    def puntos_con_etiquetas(self):
        """
        Devuelve una lista de tuplas (x, y, etiqueta) con los puntos característicos de la elipse.
        """
        elementos = self.Elementos()
        puntos = []

        if elementos == 0:
            return puntos  # En caso de error de parámetros

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

def generar_elipse_desde_rut(rut: str, grupo_impar=True) -> Elipse:
    digitos = [int(c) for c in rut if c.isdigit()]
    if len(digitos) < 8:
        raise ValueError("El RUT debe tener al menos 8 dígitos.")

    h, k = digitos[0], digitos[1] # Centro de la elipse (h,k) = (d1,d2).

    if grupo_impar:
        a_raw = digitos[2] + digitos[3]   # a = d3 +d4
        b_raw = digitos[4] + digitos[5]   # b = d5 +d6.
        orientacion = "horizontal" if digitos[7] % 2 == 0 else "vertical" # Eje focal horizontal si d8 es par, vertical si es impar.
    else:
        a_raw = digitos[5] + digitos[6]   # a = d6 +d7
        b_raw = digitos[7] + digitos[2]   # b = d8 +d3
        orientacion = "horizontal" if digitos[3] % 2 == 0 else "vertical"

    # Asegurar que a sea mayor o igual que b
    a, b = sorted([a_raw, b_raw], reverse=True)

    return Elipse(h, k, a, b, orientacion)