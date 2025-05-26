# Detector de Color Azul con OpenCV

Este proyecto es una aplicación en Python que utiliza la cámara web para detectar objetos de color azul en tiempo real. Se basa en el uso de OpenCV y NumPy para el procesamiento de imágenes, y puede ser fácilmente ejecutado en entornos Linux (como Ubuntu).

---

## 🎥 Video Demostrativo

👉 Mira el funcionamiento del proyecto en el siguiente video:  
[![Ver en YouTube](https://img.youtube.com/vi/z3OpTpA2WMo/0.jpg)](https://youtu.be/z3OpTpA2WMo)

---

## 🧠 Descripción

El script captura imágenes en vivo desde la cámara, las convierte al espacio de color HSV y utiliza un rango específico para detectar el color azul. Una vez detectado, se resaltan las áreas azules con un rectángulo verde y se muestra un punto rojo en su centro, junto con las coordenadas en pantalla.

---

## 📦 Requisitos del entorno

Asegúrate de tener las siguientes tecnologías instaladas:

- Python 3.12.3
- OpenCV-Python 4.11.0.86
- NumPy (viene incluido con OpenCV en muchos entornos)
- Pytesseract 0.3.13 *(no utilizado en este código actual, pero mencionado en los requerimientos)*
- Tesseract-OCR (idioma español) *(no utilizado directamente, pero puede ser útil si planeas extender la funcionalidad a OCR)*
- Sistema operativo: Linux Ubuntu

---

## ⚙️ Instalación

1. **Clona el repositorio** (si aplica) o copia el script en tu entorno local.
2. **Instala los requisitos** ejecutando:

```bash
pip install opencv-python==4.11.0.86 pytesseract numpy

