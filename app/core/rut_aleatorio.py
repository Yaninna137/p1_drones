import random

def calcular_dv(rut_sin_dv):
    """Calcula el dígito verificador de un RUT chileno."""
    reversed_digits = map(int, reversed(str(rut_sin_dv)))
    factors = [2, 3, 4, 5, 6, 7]
    total = sum(d * factors[i % len(factors)] for i, d in enumerate(reversed_digits))
    remainder = 11 - (total % 11)
    if remainder == 11:
        return "0"
    elif remainder == 10:
        return "K"
    else:
        return str(remainder)

def generar_rut():
    """Genera un RUT chileno válido y formateado."""
    numero = random.randint(1000000, 25000000)
    dv = calcular_dv(numero)
    rut_str = f"{numero:,}".replace(",", ".") + "-" + dv
    return rut_str

def generar_varios_ruts(n=3):
    """Genera una lista de RUTs válidos."""
    return [generar_rut() for _ in range(n)]
