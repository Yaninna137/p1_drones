# Sistema de Monitoreo de Drones
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)

<div align="center">
  <img src="assets/dron.avif" alt="Logo de un dron" width="200"/>
  <br/>
  <i>Simula la trayectoria de un dron a través del RUT ingresado</i>
</div>

## 📝 Contexto del proyecto 
En la Universidad Católica de Temuco, se investigan trayectorias seguras para drones en entornos urbanos como eventos masivos o inspecciones de estructuras civiles.

Estas trayectorias se modelan mediante secciones cónicas (elipses), asociadas al RUT del operador, con el fin de garantizar seguridad y eficiencia en misiones autónomas.

El proyecto está a cargo de estudiantes de Ingeniería Civil Informática, quienes deben diseñar, simular y validar dichas trayectorias, aplicando geometría analítica, programación y modelado matemático. El desarrollo se organiza por fases, integrando teoría y práctica.

## 👷 ¿Qué tiene ahora? (Avance)

Actualmente se ha desarrollado la funcionalidad de cálculo de una elipse a partir de un RUT en `app/core/elipse.py`.

Se implementa programación orientada a objetos (POO), separando la lógica de operaciones de la visualización.

En esta versión 1.0, la aplicación permite:
- Ingresar un RUT y generar una elipse asociada.
- Mostrar los elementos derivados de esa elipse.
- Realizar todos los cálculos manualmente (sin utilizar librerías como `math`).  
  → Ver más en [`docs/elipse.md`](docs/elipse.md)
- Mostrar gráfica 2D con los puntos.
- Mostrar gráfica 2D y3D de más elipse.
- Detectar Colisiones entre elipse.
- Mejorar visualización.
- Ingresar más rut (máximo de soporte 5).
- Rut aleatorio.
- Separación, organización de archivos y nuevos archivos `test`, `core`.


> **Nota:** Hemos hecho una última actualización versión 2.0 : (Implementación de gráfica 3D, ingresar más rut, detección de colisión, mejora y más elementos de interfaz).

> **Rut Aleatorio** Corregir un error el 40% entregara un rut invalido en aleatorio, hay que corregir.

> **Panel** Se debe cambiar el panel de descripción.

<div align="center">
  <img src="assets/campo2.png" alt="Ingresar RUT" />
  <br/>
  <i>Ingreso de RUT (De 1 a 5 max)</i>
</div>
<div align="center">
  <img src="assets/pest1.png" alt="Diseño del contenedor"/>
  <br/>
  <i>Pestañas disponibles</i>
</div>

<div align="center">
  <img src="assets/pesta1.png" alt="Diseño del contenedor"/>
  <br/>
  <i>Pestaña 1: Datos de elipses</i>
</div>
<div align="center">
  <img src="assets/past21.png" alt="2D y 3D multiple elipses"/>
  <img src="assets/past22.png" alt="colisiones"/>
  <br/>
  <i>Pestaña 2: Gráficos y colisiones</i>
</div>

## 🔧 Trabajo a implementar

Se proyecta desarrollar una aplicación con estructura avanzada, que ofrezca una interfaz amigable y funcional para los usuarios, permitiendo validar los datos de forma clara y segura.

## 🧰 Herramientas utilizadas (por ahora)

**Backend:** Python 3.8+

**Librerías:**
- **Streamlit**: Interfaz web rápida y elegante.
- **Matplotlib**: Gráficos 2D.
- **Plotly**: Gráficos 3D interactivos.
- **Pydantic**: Validación robusta de datos (como entradas de RUT, parámetros, etc.).
- **Pytest**: Pruebas automáticas de funciones.
- **Numpy**: Cálculos numéricos y manejo de vectores.
- **Scipy**: Cálculos de colisión y precisión matemática.

> **Nota:** Inicialmente se utilizarán Numpy y Scipy para facilitar validaciones, pero en etapas posteriores se eliminarán para implementar los cálculos manualmente y reforzar la comprensión matemática.

## 👨‍💻 MAT1186

Proyecto desarrollado para la asignatura **MAT1186 - Introducción al Cálculo**, implementando operaciones de elementos canónicos sin depender de bibliotecas matemáticas externas, con el objetivo de reforzar los conceptos teóricos mediante su aplicación práctica.

---

<div align="center">
  <p><strong>Versión 1.1</strong> - Primer prototipo funcional</p>
</div>
