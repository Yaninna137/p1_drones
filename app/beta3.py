# main.py
import streamlit as st
import matplotlib.pyplot as plt
import io
import base64
from core.elipse import generar_elipse_desde_rut
from components.estilo import estilo_add

st.set_page_config(page_title="Simulador de entorno drones-RUT", layout="centered")
st.title("🌀 Generador de Elipses desde tu RUT")

rut = st.text_input("Ingresa tu RUT (sin puntos ni guión):")
estilo_add()  # Aplicar estilo CSS personalizado

def Contenedor_Datos(elipse, rut):
    try:
        e_canonica = elipse.ecuacion_canonica()
        e_general = elipse.ecuacion_general()
        elementos = elipse.Elementos()

        if not isinstance(elementos, dict):
            st.error("No se puede calcular la elipse porque 'a' es menor que 'b'.")
            return

        focos = elementos.get('focos', [])
        if (
            isinstance(focos, (list, tuple)) and len(focos) == 2
            and all(isinstance(f, tuple) and len(f) == 2 for f in focos)
        ):
            f1, f2 = focos
            f1_str = f"({f1[0]:.2f}, {f1[1]:.2f})"
            f2_str = f"({f2[0]:.2f}, {f2[1]:.2f})"
        else:
            f1_str = f2_str = "(no disponible)"

        st.markdown(f'''
            <div class="block">
                <div class="row-flex">
                    <div class="scroll-inner">
                        <p><b>Elipse del dron-RUT ({rut})</b></p>
                        <p>h = {elipse.h} ; k = {elipse.k} ; a = {elipse.a} ; b = {elipse.b}</p>
                        <ul>
                            <li><b>C(h,k)</b> = C({elipse.h}, {elipse.k})</li>
                            <li><b>Focos</b> = F1: {f1_str} ; F2: {f2_str}</li>
                            <li><b>Vertices P.</b> = V1{elementos['vertices_principales'][0]} ; V2{elementos['vertices_principales'][1]}</li>
                            <li><b>Vertices A.</b> = B1{elementos['vertices_secundarios'][0]} ; B2{elementos['vertices_secundarios'][1]}</li>
                            <li><b>c = √a² - b²</b> = {elementos['c']}</li>
                            <li><b>Eje mayor 2a</b> = {elementos['eje_mayor']}</li>
                            <li><b>Eje menor 2b</b> = {elementos['eje_menor']}</li>
                            <li><b>Eje focal 2c</b> = {elementos['eje_focal']}</li>
                            <li><b>Eje focal paralelo al eje {elementos['orientacion']}</b></li>
                        </ul>
                    </div>
                </div>
            </div>
        ''', unsafe_allow_html=True)

        st.markdown("Ec. Canónica:")
        st.latex(e_canonica)

        st.markdown("Ec. General:")
        st.latex(e_general)

    except Exception as e:
        st.error(f"Error al procesar los datos de la elipse: {e}")


if rut:
    try:
        elipse = generar_elipse_desde_rut(rut)
        st.markdown('<div class="scroll-box">', unsafe_allow_html=True)
        Contenedor_Datos(elipse, rut)
        st.markdown('</div>', unsafe_allow_html=True)
    except ValueError as ve:
        st.warning(str(ve))
    except Exception as e:
        st.error(f"Error: {e}")
