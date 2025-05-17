# Sistema de monitoreo de drones
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)

<div align="center">
  <img src="assets/dron.avif" alt="Logo de un dron" width="200"/>
  <br/>
  <i>Simular trayectoria de un dron a travez del rut ingresado</i>
</div>

## 📝 Contexto del proyecto 
En las instalaciones de la Universidad Católica de Temuco, se analizan trayectorias seguras para drones en entornos urbanos, como eventos masivos o inspecciones de estructuras civiles. 

Estas trayectorias se modelan mediante secciones cónicas (elipses), vinculadas al RUT de los operadores, con el objetivo de garantizar seguridad y eficiencia en misiones autónomas.

Los estudiantes de ingeniería civil informática serán responsables de diseñar, simular y validar estas trayectorias aplicando conceptos de geometría analítica, programación y modelado matem´atico. El enfoque
se divide en varias fases para integrar teoría práctica.

## 🔧 Trabajo a implementar
Para poder cumplir nuestra misión crearemos una apicación avanzada en estructura para entregar una interfaz amigable y funcional a nuestro usuarios y poder validar datos

### Herramientas actualizar(por ahora)
-**Backend**: Python 3
-**Librerias**: 
    - **streamlit**: Intefaz a utilizar por su web rápida y elegante.
    - **matplotlib**: Poder implemetar gráficos 2D.
    - **plotly**:Poder implementar gráficos 3D interactivos.
    - **pydantic**: Usar para validación robusta de datos (como entradas de RUT, parámetros, etc.)
    - **pytest**: Realizar testeo automático de tus funciones
    - **numpy**: Cálcular numéricos y vectores.
    - **scipy**: Cálculos de colisión y precisión m.
<svg width="300" height="200">
  <defs>
    <path id="curva" d="M 50,100 A 100,100 0 0,1 250,100" />
  </defs>
  <text font-size="20" fill="black">
    <textPath href="#curva">"Se usara primero la liberia numpy y scipy, pero luego se sacara para implementar los calculos sin depender de estas libreria(Demostrar manualmente su calculo)"</textPath>
  </text>
</svg>


## 👨‍💻 Desarrollo

Proyecto desarrollado para MAT1186 - Introducción al cálculo, implementando operaciones de elemento canonico sin depender de bibliotecas matemáticas externas, reforzando la comprensión de los conceptos matemáticos subyacentes.

---

<div align="center">
  <p>version 1.0 </p>
</div>
