'''
Este manejará:
-Validación del RUT.
-Extracción de d1 a d8.
-Generación aleatoria.
-Chequeos.
Validación y generación de RUT
'''

import re
from core.rut_aleatorio import generar_varios_ruts

def limpiar_ruts(texto):
    """
    Limpia el texto y devuelve una lista de RUTs bien formateados (sin espacios, sin puntos).
    """
    ruts = texto.replace(",", "\n").splitlines()
    return [rut.strip().replace(".", "").upper() for rut in ruts if rut.strip()]

def es_rut_valido(rut):
    """
    Valida sintácticamente un RUT chileno (formato y dígito verificador).
    """
    rut = rut.upper().replace("-", "").replace(".", "")
    if not rut[:-1].isdigit():
        return False

    cuerpo = rut[:-1]
    dv = rut[-1]

    suma = 0
    multiplo = 2
    for d in reversed(cuerpo):
        suma += int(d) * multiplo
        multiplo = 9 if multiplo == 7 else multiplo + 1

    resto = 11 - (suma % 11)
    dv_calc = 'K' if resto == 10 else '0' if resto == 11 else str(resto)
    return dv == dv_calc

def generar_ruts_validos(n=3):
    return generar_varios_ruts(n)
