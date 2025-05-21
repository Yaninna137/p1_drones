'''
Interfaz de prueba 1.2 , esquema de como tener los elementos
'''

import streamlit as st
import matplotlib.pyplot as plt
from core.Math_ellipse import generar_elipse_desde_rut
from core.Items_ellipse import ElipseVisual
from core.Graph_ellipse import Grafico_2D, Grafico_2D_multiple
from core.Collision_ellipse import hay_colision
from components.estilo import estilo_add
from core.Graph_ellipse import Grafico_3D_multiple
from core.rut_aleatorio import generar_rut, generar_varios_ruts

# Configuración inicial
st.set_page_config(page_title="Simulador de Trayectorias Dron - RUT", layout="wide")
estilo_add()
st.title("🌀 Simulador de Trayectorias de Drones a partir del RUT")

# Entrada de RUTs
col1, col2 = st.columns([4, 1])
with col1:
    ruts_input = st.text_area("✍️ Ingresar uno o más RUTs separados por comas o saltos de línea:",
                              value=st.session_state.get("ruts_input", ""))
with col2:
    if st.button("🎲 RUT aleatorio"):
        ruts_generados = generar_varios_ruts(3)  # Cambia el número si quieres más RUTs
        st.session_state.ruts_input = "\n".join(ruts_generados)
        st.rerun()

ruts_limpios = [rut.strip() for rut in ruts_input.replace(",", "\n").splitlines() if rut.strip()]
with col2:
    simular = st.button("🚀 Simular")

st.markdown("---")

if simular and ruts_limpios:
    elipses = []
    errores = []
    for rut in ruts_limpios:
        try:
            elipse = generar_elipse_desde_rut(rut)
            elipses.append(elipse)
        except Exception as e:
            errores.append(f"{rut}: {e}")

    if errores:
        st.error("⚠️ Algunos RUTs no pudieron procesarse:")
        for err in errores:
            st.markdown(f"- {err}")
    else:
        st.success("✅ Elipses generadas correctamente")

        # Tabs
        tab1, tab2 = st.tabs(["📋 Datos de elipses", "📈 Gráficos y Colisiones"])

        with tab1:
            st.markdown("### 📌 Información detallada de cada elipse")
            for idx, e in enumerate(elipses):
                datos = ElipseVisual(**e.__dict__)
                elementos = datos.obtener_elementos()
                col1, col2 = st.columns([2, 2])

                with col1:
                    st.markdown(f"**RUT:** {ruts_limpios[idx]}")
                    st.markdown(f"- h = {e.h}, k = {e.k}, a = {e.a}, b = {e.b}")
                    st.markdown(f"- Focos: {elementos['focos']}")
                    st.markdown(f"- Vértices principales: {elementos['vertices_principales']}")
                    st.markdown(f"- Vértices secundarios: {elementos['vertices_secundarios']}")
                    st.markdown(f"- Eje mayor: {elementos['eje_mayor']}")
                    st.markdown(f"- Eje menor: {elementos['eje_menor']}")
                    st.markdown(f"- Eje focal: {elementos['eje_focal']}")
                    st.markdown(f"- Orientación: {elementos['orientacion']}")

                with col2:
                    img_ind = Grafico_2D(e)
                    st.image(f"data:image/png;base64,{img_ind}", width=320)

        with tab2:
            st.markdown("### 🎯 Comparación visual y detección de colisiones")

            col1, col2 = st.columns([2, 2])
            with col1:
                img_global = Grafico_2D_multiple(elipses, ruts_limpios)
                st.image(f"data:image/png;base64,{img_global}", width=420)
            with col2:
                st.info("🌐 Gráfico 3D más adelante...")
                fig3d = Grafico_3D_multiple(elipses, ruts_limpios)
                st.plotly_chart(fig3d, use_container_width=True)

            st.markdown("---")
            st.markdown("### 📊 Resultados de colisión")

            total = 0
            for i in range(len(elipses)):
                for j in range(i + 1, len(elipses)):
                    if hay_colision(elipses[i], elipses[j]):
                        st.error(f"❌ Colisión entre RUT {ruts_limpios[i]} y {ruts_limpios[j]}")
                        total += 1
                    else:
                        st.success(f"✅ Sin colisión entre RUT {ruts_limpios[i]} y {ruts_limpios[j]}")

            total_posibles = len(elipses) * (len(elipses) - 1) // 2
            st.markdown(f"🔴 **Total de colisiones:** {total}")
            st.markdown(f"🟢 **Sin colisión:** {total_posibles - total}")
