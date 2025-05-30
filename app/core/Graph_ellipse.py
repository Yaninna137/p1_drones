# app/core/Graph_ellipse.py
from .Math_ellipse import Elipse
from .Items_ellipse import ElipseVisual
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import io
import base64

tick_color = ['#BBBBBB', '#888888', '#999999', '#AAAAAA'] 
colores = [
    "#4DD0E1",  # Azul cian suave
    "#9575CD",  # Violeta suave
    "#F06292",  # Rosa sandía
    "#FFB74D",  # Naranja suave
    "#81C784",  # Verde menta
    "#BA68C8",  # Violeta medio
    "#2A2A2A"   # Blanco (para último punto si se desea)
]

def formatear_numero(n):
    return int(n) if n == int(n) else round(n, 1)

# GRAFICO 2D - INDIVIDUAL ELIPSE =>

def grafico_2d_simple(elipse: Elipse, escala=1.0):
    puntos = elipse.calcular_puntos(n=200)
    
    if isinstance(elipse, ElipseVisual): # Asegurando de usar puntos con etiquetas desde ElipseVisual
        puntos_etiquetados = elipse.puntos_con_etiquetas()
    else:
        elipse_ext = ElipseVisual(**elipse.__dict__)
        puntos_etiquetados = elipse_ext.puntos_con_etiquetas()

    x_vals = [x * escala for x, _ in puntos]
    y_vals = [y * escala for _, y in puntos]

    fig, ax = plt.subplots(figsize=(6, 6))
    fig.patch.set_facecolor('#121212')
    ax.set_facecolor('#121212')
    ax.plot(x_vals, y_vals, color="#0080FF66", linewidth=1, label="Elipse")

    # Centro
    ax.scatter(elipse.h * escala, elipse.k * escala, color='red', zorder=5)
    ax.text(elipse.h * escala + 0.2, elipse.k * escala + 0.2, f"({elipse.h}, {elipse.k})", color='red')

    # Ejes cartesianos
    ax.axhline(0, color='gray', linewidth=1)
    ax.axvline(0, color='gray', linewidth=1)

    # Limites
    margen = max(elipse.a, elipse.b) * 1.5 * escala
    ax.set_xlim((elipse.h - margen) * escala, (elipse.h + margen) * escala)
    ax.set_ylim((elipse.k - margen) * escala, (elipse.k + margen) * escala)

    # Diseño para la Grafica
    info_labels = []
    for i, (x, y, label) in enumerate(puntos_etiquetados):
        x_scaled, y_scaled = x * escala, y * escala
        ax.plot(x_scaled, y_scaled, 'o', color=colores[i], markersize=8,
                markeredgecolor=colores[i], markeredgewidth=0.8, zorder=3)
        
        texto = f"{label} ({formatear_numero(x)}, {formatear_numero(y)})"
        info_labels.append((texto, colores[i]))

    # Personalizar leyenda 
    x_rel = 0.02
    y_rel_base = 0.02
    espaciado = 0.05  
    for idx, (texto, color) in enumerate(info_labels[:-1]):
        y_rel = y_rel_base + idx * espaciado
        ax.text(x_rel, y_rel, f"● {texto}",
                transform=ax.transAxes,
                fontsize=11, fontweight='bold',
                verticalalignment='bottom',
                color=color)
        
    ax.set_aspect('equal')  # CRUCIAL para que no se deforme la elipse
    ax.grid(True, linestyle='-', alpha=0.5, color='#3A3A3A')  # Color de linias graficas
    ax.set_title("Elipse centrada en ({}, {})".format(elipse.h, elipse.k),color="#FF4C4C", fontsize=14, fontweight='bold')

    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")

    ax.tick_params(axis='x', colors=tick_color[0]) # Color de los números de los ejes X
    ax.tick_params(axis='y', colors=tick_color[0]) # Color de los números de los ejes Y
    ax.xaxis.label.set_color(tick_color[0]) # Color de las etiquetas de los ejes
    ax.yaxis.label.set_color(tick_color[0]) # Color del título (opcional, para consistencia)


    # Guardar como imagen base64
    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches='tight')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode()
    buf.close()

    return img_base64

# GRAFICO 2D INTERACTIVO - MULTIPLE ELIPSE =>

def grafico_2d_interactivo(elipses: list, ruts_limpios: list, escala=1.0):
    fig = go.Figure()

    for idx, elipse in enumerate(elipses):
        puntos = elipse.calcular_puntos(n=200)
        x_vals = [x * escala for x, _ in puntos]
        y_vals = [y * escala for _, y in puntos]
        color = colores[idx % len(colores)]

        fig.add_trace(go.Scatter(
            x=x_vals,
            y=y_vals,
            mode='lines',
            name=f"Elipse {ruts_limpios[idx]}",
            line=dict(color=color, width=2.5),
            hoverinfo='name'
        ))

        # Punto central (opcional)
        fig.add_trace(go.Scatter(
            x=[elipse.h * escala],
            y=[elipse.k * escala],
            mode='markers+text',
            text=[f"({elipse.h}, {elipse.k})"],
            textposition="top right",
            marker=dict(color=color, size=6),
            showlegend=False
        ))

    fig.update_layout(
        # title="Visualización 2D de trayectorias",
        plot_bgcolor='#121212',
        paper_bgcolor='#121212',
        font=dict(color=tick_color[0], size=12),
        xaxis=dict(
            title="Eje X",
            color=tick_color[0],
            zeroline=True,
            showgrid=True,
            gridcolor="#2A2A2A",
        ),
        yaxis=dict(
            title="Eje Y",
            color=tick_color[0],
            zeroline=True,
            showgrid=True,
            gridcolor="#2A2A2A",
            scaleanchor="x",  # Relación 1:1
            scaleratio=1
        ),
        legend=dict(
            bgcolor='#121212',
            bordercolor=tick_color[3],
            borderwidth=1
        ),title="Visualización 2D de trayectorias"
    )

    return fig

# GRAFICO 3D INTERACTIVO - MULTIPLE ELIPSE =>

def Grafico_3D_multiple(elipses: list, ruts_limpios: list, escala=0.5):
    fig = go.Figure()

    colores = [
        "#4DD0E1", "#FFD54F", "#81C784",
        "#BA68C8", "#FF8A65", "#64B5F6", "#F06292"
    ]

    for idx, elipse in enumerate(elipses):
        puntos = elipse.calcular_puntos(n=100)
        x = [p[0] * escala for p in puntos]
        y = [p[1] * escala for p in puntos]
        z = [idx] * len(puntos)

        fig.add_trace(go.Scatter3d(
            x=x,
            y=y,
            z=z,
            mode='lines',
            line=dict(color=colores[idx % len(colores)], width=4),
            name=f"RUT {ruts_limpios[idx]}"
        ))

    fig.update_layout(
        margin=dict(l=0, r=0, b=0, t=40),
        paper_bgcolor='#121212',
        plot_bgcolor='#121212',
        font_color='white',
        scene=dict(
            xaxis=dict(title='X', backgroundcolor='#121212', gridcolor='#424242'),
            yaxis=dict(title='Y', backgroundcolor='#121212', gridcolor='#424242'),
            zaxis=dict(title='Z', backgroundcolor='#121212', gridcolor='#424242')
        ),
        title="Visualización 3D de trayectorias"
    )

    return fig
