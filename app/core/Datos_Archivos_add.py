# -------------------------
# Archivos de codigo antiguo
# main.py
import streamlit as st
import matplotlib.pyplot as plt
import io
import base64
from core.elipse import generar_elipse_desde_rut
from components.estilo import estilo_add

st.set_page_config(page_title="Simulador de entorno drones-RUT", layout="centered") # Nombre del proyecto
st.title("🌀 Generador de Elipses desde tu RUT")
rut = st.text_input("Ingresa tu RUT (sin puntos ni guión):")
estilo_add() # Colcando estilo CSS 
# ------------------------------------------------------
# Datos del grafico, solo diseño, no usa aun los datos correspondiente
# --------------------------------------------------------
def Grafica_2d(): # Crear gráfico con fondo negro y línea verde, tamaño aumentado
    fig, ax = plt.subplots(figsize=(6, 5))  # más grande
    x = [-2, -1, 0, 1, 2]
    y = [i**2 for i in x]
    fig.patch.set_facecolor('#1e1e1e')  # fondo general
    ax.set_facecolor('#1e1e1e')         # fondo área gráfica
    ax.plot(x, y, marker='o', color='#00ff00', linewidth=2)
    # Quitar ticks y etiquetas
    ax.set_xticks([])
    ax.set_yticks([])
    # Bordes en verde
    for spine in ax.spines.values():
        spine.set_color('#00ff00')
    # Añadir letras para puntos
    labels = ['A', 'B', 'C', 'D', 'E']
    for i, (xx, yy) in enumerate(zip(x, y)):
        ax.text(xx, yy + 0.5, labels[i], color='#00ff00', fontsize=12, fontweight='bold', ha='center')
    ax.set_title("y = x²", color='#00ff00', fontsize=14, fontweight='bold')
    # Convertir gráfico a imagen base64
    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches='tight', dpi=100)
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode()
    buf.close()
    return img_base64
# ------------------------------------------------------
# if rut:
#     try:
#         elipse = generar_elipse_desde_rut(rut)
#     except Exception as e:
#         st.error(f"Error: {e}")
        
def Contenedor_Datos(elipse,img_base64,rut):
    e_canonica = elipse.ecuacion_canonica()
    e_general = elipse.ecuacion_general()
    elementos = elipse.Elementos()

    st.markdown(f'''
        <div class="block">
            <div class="row-flex">
                <div class="scroll-inner">
                    <p><b>Elipse del dron-RUT({rut})</b></p>
                    <p>h = {elipse.h} ; K = {elipse.k} ; a = {elipse.a}; b = {elipse.b} </p>
                    <ul>
                        <li><b>C(h,k)</b> = C( {elipse.h} , {elipse.k} )</li>
                        <li><b>Focos</b> = F1{elementos['focos'][0]} ; F2{elementos['focos'][1]}</li>
                        <li><b>Vertices P.</b> = V1{elementos['vertices_principales'][0]} ; V2{elementos['vertices_principales'][1]}</li>
                        <li><b>Vertices A.</b> = B1{elementos['vertices_secundarios'][0]} ; B2{elementos['vertices_secundarios'][1]}</li>

                        <li><b>c = √a² - b²</b> = {elementos['c']}</li>
                        <li><b>Eje mayor 2a</b> = {elementos['eje_mayor']}</li>
                        <li><b>Eje menor 2b</b> = {elementos['eje_menor']}</li>
                        <li><b>Eje focal 2c</b> = {elementos['eje_focal']}</li>
                        <li><b>Eje focal paralelo al eje {elementos['orientacion']}</b></li>

                        
                    </ul>
                </div>
                <img src="data:image/png;base64,{img_base64}" class="image-style" />
            </div>
        </div>
    ''', unsafe_allow_html=True)
    # Dato 2
    st.markdown(f'''
        <div class="block">
            <div>Ec.Canónica = $${e_canonica}$$</div>
        </div>
    ''', unsafe_allow_html=True)
    # Dato 3
    st.markdown(f'''
        <div class="block">
            <div>Ec.General = $${e_general}$$</div>
        </div>
    ''', unsafe_allow_html=True)

if rut:
    try:
        elipse = generar_elipse_desde_rut(rut)
        img_base64 = Grafica_2d()
        st.markdown('<div class="scroll-box">', unsafe_allow_html=True)  # Contenedor principal(por ahora)
        Contenedor_Datos(elipse, img_base64,rut)
        st.markdown('</div>', unsafe_allow_html=True) # Cierre del contenedor
    except Exception as e:
        st.error(f"Error: {e}")
# ...............................

# def generar_elipse_desde_rut(rut: str, grupo_impar=True) -> Elipse:
#     digitos = [int(c) for c in rut if c.isdigit()]
#     if len(digitos) < 8:
#         raise ValueError("El RUT debe tener al menos 8 dígitos.")

#     if grupo_impar:
#         h, k = digitos[0], digitos[1]
#         a = digitos[2] + digitos[3]
#         b = digitos[4] + digitos[5]
#         orientacion = "horizontal" if digitos[7] % 2 == 0 else "vertical"
#     else:
#         h, k = digitos[0], digitos[1]
#         a = digitos[5] + digitos[6]
#         b = digitos[7] + digitos[2]
#         orientacion = "horizontal" if digitos[3] % 2 == 0 else "vertical"

#     return Elipse(h, k, a, b, orientacion)