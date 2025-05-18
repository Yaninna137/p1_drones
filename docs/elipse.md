# Generador de Elipses a partir del RUT

## 📌 Objetivo

Este módulo tiene como objetivo convertir un número de RUT en los parámetros de una elipse, para luego mostrar:

- Su **ecuación canónica**
- Su **ecuación general**
- Una lista de **puntos sobre la elipse**, calculados sin usar librerías externas como `math`.

---

## 📐 Fundamento Matemático

### 🔸 Ecuación Canónica de la Elipse

Una elipse con centro en (h, k), semiejes `a` y `b`, se expresa como:

- Si es **horizontal**:  
  \[
  \frac{(x - h)^2}{a^2} + \frac{(y - k)^2}{b^2} = 1
  \]

- Si es **vertical**:  
  \[
  \frac{(x - h)^2}{b^2} + \frac{(y - k)^2}{a^2} = 1
  \]

### 🔸 Ecuación General (sin rotación)

A partir de la forma canónica, se puede expandir y obtener la forma general:

\[
Ax^2 + By^2 + Dx + Ey + F = 0
\]
---

## 🔢 Parámetros desde el RUT

Se toma el RUT (sin puntos ni guion) y se extraen los dígitos numéricos. Luego:

- h = dígito 1
- k = dígito 2
- a = suma de dígitos 3 y 4
- b = suma de dígitos 5 y 6
- La orientación se define por si el dígito 8 es par o impar

---

## ⚙️ Implementación

### 🔧 Clase `Elipse`

Incluye:

- Métodos para retornar la **ecuación canónica** y **general**
- Un método `calcular_puntos()` que genera puntos de la forma:

  \[
  x(t) = h + a \cdot \cos(t), \quad y(t) = k + b \cdot \sin(t)
  \]

- Métodos `seno`, `coseno` y `factorial` definidos manualmente con series de Taylor

---

## 🖥️ Uso desde Consola

Ejecutar el archivo desde terminal:

```bash
python app/main_elipse.py
```