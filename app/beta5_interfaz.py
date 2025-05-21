'''
Interfaz casi completa version 2.0
Hay que separar los componentes para que el codigo sea legible y no tan desordenado, 
pero este es el diseño que se piensa utilizar (80% de estos)
Contiene todo lo trabajado
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


st.markdown(
    """
    <div style='text-align: center; margin-bottom: 30px;'>
        <h1 style='margin-bottom: 0; color: white;'>STD-RUT</h1>
        <p style='font-size: 18px; color: gray;'>Simulador de Trayectorias de Drones a partir del RUT</p>
    </div>
    """,
    unsafe_allow_html=True
)
# Columnas
col_izq, col_der = st.columns([2, 2], gap="large")

# Tarjeta izquierda con borde animado de colores cálidos
with col_izq:
    st.markdown("""
    <div style="
        padding: 2px;
        border-radius: 12px;
        position: relative;
        background: linear-gradient(270deg, #ff4b4b, #ffa500, #ffd700, #ffa500, #ff4b4b);
        background-size: 1000% 1000%;
        animation: animateBorder 8s linear infinite;
    ">
        <div style="
            border-radius: 10px;
            background-color: #0F111A;
            padding: 20px;
            color: white;
            font-size: 14px;
            line-height: 1.6;
        ">
            <h4 style="margin-top: 0; color: #FF4B4B;">STDR</h4>
            <p>La app STDR permite simular trayectorias elipsoidales para drones. Incluye:</p>
            <ul>
                <li>Generación de elipses a partir del RUT</li>
                <li>Visualización 2D y 3D</li>
                <li>Detección de colisiones</li>
                <li>Herramientas de análisis y verificación</li>
            </ul>
        </div>
    </div>

    <style>
    @keyframes animateBorder {
        0% { background-position: 0% 50%; }
        100% { background-position: 100% 50%; }
    }
    </style>
    """, unsafe_allow_html=True)

# Entrada y botones a la derecha
with col_der:
    # Estilos personalizados para el textarea y el label
    st.markdown("""
    <style>
    /* Oculta el label del text_area */
    .css-1kyxreq.effi0qh3 {
        display: none;
    }
    /* Estilo para el campo de texto */
    textarea {
        background-color: #1b1f2a !important;
        color: white !important;
        border-radius: 8px !important;
        border: 1px solid #444 !important;
    }
    </style>
    <p style="color: #ff6f61; font-weight: bold; margin-bottom: 0.2em;">Ingresar RUTs:</p>
    """, unsafe_allow_html=True)

    ruts_input = st.text_area(
        "",
        value=st.session_state.get("ruts_input", ""),
        height=120,
        placeholder="Ej: 12.345.678-5\n9.876.543-2"
    )


    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 2])
    with col_btn2:
        if st.button("RUT aleatorio"):
            ruts_generados = generar_varios_ruts(3)
            st.session_state.ruts_input = "\n".join(ruts_generados)
            st.rerun()
    with col_btn3:
        simular = st.button("Simular elipse")

# Procesar RUTs si existen
ruts_limpios = [
    rut.strip() for rut in ruts_input.replace(",", "\n").splitlines()
    if rut.strip()
]
st.markdown("---")

def Contenedor_Datos(elipse, rut):
    try:
        e_canonica = elipse.ecuacion_canonica()
        e_general = elipse.ecuacion_general()
        datos = ElipseVisual(**elipse.__dict__)  # Crear instancia en una clase de herencia
        elementos = datos.obtener_elementos()

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
            <h4 style="color: #ff6f61" >Elipse del dron-RUT ({rut})</h4>
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
        tab1, tab2 = st.tabs(["Datos de elipses", "Gráficos y Colisiones"])

        with tab1:
            st.markdown(
            """
            <div style='background-color: #1b1f2a; padding: 15px; border-radius: 8px; margin-bottom: 20px;'>
            <h2 style='margin-bottom: 5px; color: white; text-align: center;'>Datos de las elipses</h2>
            <p style='font-size: 18px; color: gray; text-align: center;'>
                En esta sección encontrarás los detalles técnicos de cada elipse generada, incluyendo vértices, focos y parámetros calculados a partir del RUT del dron.
            </p>
            </div>
            """,unsafe_allow_html=True)
            for idx, elipse in enumerate(elipses):
                col1, col2 = st.columns([2, 3])

                with col2:
                    st.markdown('<div class="scroll-box">', unsafe_allow_html=True)
                    Contenedor_Datos(elipse, ruts_limpios[idx])
                    st.markdown('</div>', unsafe_allow_html=True)
                with col1:
                    img_base64 = Grafico_2D(elipse)
                    st.markdown(
                        f"""
                        <div style="text-align: center;">
                            <img src="data:image/png;base64,{img_base64}" width="400", height=400"/>
                            <span style='font-size: 18px; color: gray; display: block; margin-top: 8px;'>Gráfica 2D</span>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

        with tab2:
            st.markdown(
            """
            <div style='background-color: #1b1f2a; padding: 15px; border-radius: 8px; margin-bottom: 20px;'>
            <h2 style='margin-bottom: 5px; color: white; text-align: center;'>Comparación visual y detección de colisiones</h2>
            <p style='font-size: 18px; color: gray; text-align: center;'>
                Sección visual de grafica 2D, 3D, colision(si existe)
            </p>
            </div>
            """,unsafe_allow_html=True)

            col1, col2 = st.columns([2, 2])
            with col1:
                img_global = Grafico_2D_multiple(elipses, ruts_limpios)
                st.markdown(
                        f"""
                        <div style="text-align: center;">
                            <h6> Visualización 2D de la trayectoria</h6>
                            <img src="data:image/png;base64,{img_global}" width="400", height=400"/>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
            with col2:
                # st.info("🌐 Gráfico 3D más adelante...")
                fig3d = Grafico_3D_multiple(elipses, ruts_limpios)
                st.plotly_chart(fig3d, use_container_width=True)

            st.markdown("---")
            st.markdown("""<h4 style="color: #ff6f61" >Resultados de colisión</h4>""", unsafe_allow_html=True)

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
