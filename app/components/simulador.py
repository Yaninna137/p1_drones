'''
-Llamar math_ellipse para generar la elipse desde el RUT.
-Llamar graph_ellipse para graficar.
-Verificar colisiones.
-Simular diferentes escenarios.

Lógica de simulación
'''
# components/simulador.py
from core.Math_ellipse import generar_elipse_desde_rut
from core.Collision_ellipse import hay_colision

def procesar_ruts(ruts):
    """
    Intenta generar elipses desde RUTs dados. Devuelve dos listas: elipses válidas y errores.
    """
    elipses = []
    errores = []

    for rut in ruts:
        try:
            elipse = generar_elipse_desde_rut(rut)
            elipses.append(elipse)
        except Exception as e:
            errores.append(f"{rut}: {e}")
    
    return elipses, errores

def analizar_colisiones(elipses, ruts):
    """
    Devuelve una lista de resultados de colisión entre las elipses.
    """
    resultados = []
    total_colisiones = 0
    total_Sin_coliciones = 0

    for i in range(len(elipses)):
        for j in range(i + 1, len(elipses)):
            colisiona = hay_colision(elipses[i], elipses[j])
            resultado = {
                "rut1": ruts[i],
                "rut2": ruts[j],
                "colision": colisiona
            }
            if colisiona:
                total_colisiones += 1
            else:
                total_Sin_coliciones += 1
            resultados.append(resultado)
    
    return resultados, total_colisiones,total_Sin_coliciones
