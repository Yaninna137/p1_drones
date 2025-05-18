# app/main_elipse.py 
'''
Interfaz basica 0.1, mostrar los datos actuales

Adevertencia: Ah quedado absolote por cambios, app actualizado 
app/beta3.py
'''

from core.elipse import generar_elipse_desde_rut

def mostrar_datos_elipse(elipse):
    print("\n📐 Ecuación Canónica:")
    print(elipse.ecuacion_canonica())

    print("\n🧮 Ecuación General:")
    print(elipse.ecuacion_general())

    print("\n📍 Algunos puntos (x, y) sobre la elipse:")
    puntos = elipse.calcular_puntos(n=8)  # Solo mostramos 8 para que no sea largo
    for i, punto in enumerate(puntos, start=1):
        print(f"{i:02d}: x = {punto[0]:.2f}, y = {punto[1]:.2f}")

def main():
    print("==== GENERADOR DE ELIPSES DESDE RUT ====")
    rut = input("📝 Ingresa tu RUT (sin puntos ni guion): ")

    try:
        elipse = generar_elipse_desde_rut(rut)
        mostrar_datos_elipse(elipse)
    except ValueError as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
