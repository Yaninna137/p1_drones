# main.py
import streamlit as st
import matplotlib.pyplot as plt
import io
import base64
from core.elipse import generar_elipse_desde_rut
from components.estilo import estilo_add

# st.set_page_config(page_title="Simulador de entorno drones-RUT", layout="centered")
st.set_page_config(page_title="Simulador de entorno drones-RUT", layout="wide")

st.title("🌀 Generador de Elipses desde tu RUT")

rut = st.text_input("Ingresa tu RUT (sin puntos ni guión):")
estilo_add()  # Aplicar estilo CSS personalizado

def graficar_elipse_con_elementos(elipse, escala=0.5):
    puntos_elipse = elipse.calcular_puntos(n=200)
    puntos_etiquetados = elipse.puntos_con_etiquetas()

    fig, ax = plt.subplots(figsize=(6, 6))

    # Escalar puntos
    x_vals = [p[0] * escala for p in puntos_elipse]
    y_vals = [p[1] * escala for p in puntos_elipse]

    # Fondo oscuro elegante
    fig.patch.set_facecolor('#121212')  # Muy oscuro
    ax.set_facecolor('#121212')         # Azul oscuro grisáceo
    

    # Dibujar elipse con línea más suave y gradiente de color
    ax.plot(
        x_vals, y_vals,
        # label="Trayectoria de la elipse",
        color='#00ff00',  # Verde moderno y profesional
        linewidth=3,
        alpha=0.9,
        linestyle='-',
        marker='',
        zorder=2
    )

    # Marcar puntos característicos con círculos verdes neón
    for x, y, label in puntos_etiquetados:
        x_scaled, y_scaled = x * escala, y * escala
        etiqueta = f"{label} ({x:.1f}, {y:.1f})"
        ax.plot(x_scaled, y_scaled, 'o', color='#80ff72', markersize=8, markeredgecolor='white', markeredgewidth=0.8, zorder=3)
        ax.text(x_scaled + 0.12, y_scaled + 0.12, etiqueta, color='#a5d6a7', fontsize=11, fontweight='semibold', zorder=4)

    # Ejes limpios sin ticks
    ax.set_xticks([])
    ax.set_yticks([])

    # Bordes estilizados - solo línea inferior y lateral izquierda para dar marco sutil
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.spines['bottom'].set_visible(True)
    ax.spines['left'].set_visible(True)
    ax.spines['bottom'].set_color('#121212')
    ax.spines['left'].set_color('#4caf50')
    ax.spines['bottom'].set_linewidth(1.5)
    ax.spines['left'].set_linewidth(1.5)

    # Cuadrícula tenue en verde pálido
    ax.grid(True, color='#4caf50', alpha=0.15, linestyle='--', linewidth=0.8)

    # Mantener aspecto igual para no distorsionar la elipse
    ax.set_aspect('equal')

    # Leyenda clara y pequeña arriba a la derecha
    ax.legend(loc='upper right', fontsize=12, facecolor='#121212', edgecolor='#4caf50', framealpha=0.8)

    # st.pyplot(fig)  Comentado,para mostarlo mejor como imagen
    # Convertir gráfico a imagen base64 para el panel derecho
    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches='tight', dpi=100, facecolor=fig.get_facecolor())
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode()
    buf.close()
    return img_base64

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
            <p>Con el Rut Extrajimos los sig. datos y con ellos obtenemos nuevos datos.</p>
            <p>h = {elipse.h} k = {elipse.k} a = {elipse.a}  b = {elipse.b}</p>
            <div class="block">
                <div class="row-flex">
                    <div class="scroll-inner">
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
        
        # Crear columnas
        col1, col2 = st.columns([3, 2])

        with col1:
            st.markdown(f"#### Elipse del dron-RUT ({rut}")
            st.markdown('<div class="scroll-box">', unsafe_allow_html=True)
            Contenedor_Datos(elipse, rut)
            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            img_base64 = graficar_elipse_con_elementos(elipse)
            st.markdown(
                f"""
                <div style="text-align: center;">
                    <h4> Grafica 2D</h4>
                    <img src="data:image/png;base64,{img_base64}" width="400" height="400"/>
                </div>
                """,
                unsafe_allow_html=True
            )

    except ValueError as ve:
        st.warning(str(ve))
    except Exception as e:
        st.error(f"Error: {e}")

