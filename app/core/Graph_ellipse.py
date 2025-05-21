# app/core/Graph_ellipse.py
# from Math_ellipse import Elipse
from .Math_ellipse import Elipse
from .Items_ellipse import ElipseVisual
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import io
import base64

def Grafico_2D(elipse: Elipse, escala=0.5):
    puntos_elipse = elipse.calcular_puntos(n=200)

    # Asegurando de usar puntos con etiquetas desde ElipseVisual
    if isinstance(elipse, ElipseVisual):
        puntos_etiquetados = elipse.puntos_con_etiquetas()
    else:
        elipse_ext = ElipseVisual(**elipse.__dict__)
        puntos_etiquetados = elipse_ext.puntos_con_etiquetas()

    fig, ax = plt.subplots(figsize=(6, 6))
    x_vals = [p[0] * escala for p in puntos_elipse]
    y_vals = [p[1] * escala for p in puntos_elipse]

    # Fondo y estilo visual elegante
    fig.patch.set_facecolor('#121212')
    ax.set_facecolor('#121212')
    ax.plot(x_vals, y_vals, color='#00ff00', linewidth=3, alpha=0.9, linestyle='-', zorder=2)

    for x, y, label in puntos_etiquetados:
        x_scaled, y_scaled = x * escala, y * escala
        etiqueta = f"{label} ({x:.1f}, {y:.1f})"
        ax.plot(x_scaled, y_scaled, 'o', color='#80ff72', markersize=8, markeredgecolor='white', markeredgewidth=0.8, zorder=3)
        ax.text(x_scaled + 0.12, y_scaled + 0.12, etiqueta, color='#a5d6a7', fontsize=11, fontweight='semibold', zorder=4)

    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.spines['bottom'].set_visible(True)
    ax.spines['left'].set_visible(True)
    ax.spines['bottom'].set_color('#121212')
    ax.spines['left'].set_color('#4caf50')
    ax.spines['bottom'].set_linewidth(1.5)
    ax.spines['left'].set_linewidth(1.5)
    ax.grid(True, color='#4caf50', alpha=0.15, linestyle='--', linewidth=0.8)
    ax.set_aspect('equal')

    # Conversión a base64
    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches='tight', dpi=100, facecolor=fig.get_facecolor())
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode()
    buf.close()
    return img_base64

def Grafico_2D_multiple(elipses: list,ruts_limpios, escala=0.5):
    import matplotlib.pyplot as plt
    import io
    import base64

    colores = ['#00ff00', '#ff4081', '#40c4ff', '#ffd740', '#b388ff']
    
    fig, ax = plt.subplots(figsize=(7, 7))
    fig.patch.set_facecolor('#121212')
    ax.set_facecolor('#121212')

    for idx, elipse in enumerate(elipses):
        puntos = elipse.calcular_puntos(n=200)
        x_vals = [x * escala for x, _ in puntos]
        y_vals = [y * escala for _, y in puntos]
        color = colores[idx % len(colores)]

        ax.plot(
            x_vals, y_vals,
            label=f"Elipse {ruts_limpios[idx]}",
            color=color,
            linewidth=2.5,
            alpha=0.85,
            zorder=2
        )

    # Estilo general
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect("equal")
    ax.grid(True, color='#4caf50', alpha=0.15, linestyle='--', linewidth=0.8)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.spines['bottom'].set_visible(True)
    ax.spines['left'].set_visible(True)
    ax.spines['bottom'].set_color('#121212')
    ax.spines['left'].set_color('#4caf50')
    ax.spines['bottom'].set_linewidth(1.5)
    ax.spines['left'].set_linewidth(1.5)

    ax.legend(loc='upper right', fontsize=11, facecolor='#121212', edgecolor='#4caf50', framealpha=0.8)

    # Conversión a imagen base64
    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches='tight', dpi=100, facecolor=fig.get_facecolor())
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode()
    buf.close()
    return img_base64

def Grafico_3D_multiple(elipses: list, ruts_limpios: list, escala=0.5):
    fig = go.Figure()
    colores = ['#00ff00', '#ff4081', '#40c4ff', '#ffd740', '#b388ff']

    for idx, elipse in enumerate(elipses):
        puntos = elipse.calcular_puntos(n=100)
        x = [p[0] * escala for p in puntos]
        y = [p[1] * escala for p in puntos]
        z = [idx] * len(puntos)  # Cada elipse en una "altura" distinta

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
            xaxis=dict(title='X', backgroundcolor='#121212', gridcolor='#4caf50'),
            yaxis=dict(title='Y', backgroundcolor='#121212', gridcolor='#4caf50'),
            zaxis=dict(title='Z', backgroundcolor='#121212', gridcolor='#4caf50')
        ),
        title="Visualización 3D de trayectorias"
    )

    return fig
