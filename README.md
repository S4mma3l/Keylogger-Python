# Proyecto: Keylogger y Monitor de Clics Educativo 🐍

![Propósito](https://img.shields.io/badge/Propósito-Educativo-blue.svg)
![Lenguaje](https://img.shields.io/badge/Python-3.x-yellow.svg)
![Librería](https://img.shields.io/badge/Librería-pynput-red.svg)

Este repositorio contiene una colección de scripts en Python diseñados para demostrar el funcionamiento básico de un **keylogger** y un **monitor de clics de ratón** con fines puramente educativos. El código está extensamente comentado para facilitar el aprendizaje y la comprensión de los conceptos de ciberseguridad relacionados con la monitorización de entradas de usuario.

***

## ⚠️ Descargo de Responsabilidad Ético

**Este proyecto fue creado únicamente con fines académicos y de concienciación en ciberseguridad.**

El uso de estas herramientas para monitorear una computadora sin el consentimiento explícito y previo del propietario y de los usuarios es **ILEGAL** en la mayoría de las jurisdicciones y constituye una grave violación de la privacidad. El autor no se hace responsable del mal uso de la información y el código proporcionados aquí. **Úsalo de manera ética y responsable en entornos controlados y de tu propiedad.**

***

## 📋 Tabla de Contenidos

1.  [Características](#-características)
2.  [Requisitos Previos](#-requisitos-previos)
3.  [Instalación](#-instalación)
4.  [Modo de Uso](#-modo-de-uso)
5.  [Estructura de Archivos](#-estructura-del-proyecto)
6.  [Cómo Funciona](#-funcionamiento-interno)
7.  [Licencia](#-licencia)

***

## ✨ Características

* **Keylogger Básico (`keylogger.py`):** Captura las pulsaciones del teclado y las guarda en un archivo `log.txt` de forma legible, distinguiendo entre caracteres y teclas especiales (Enter, Espacio, Ctrl, etc.).
* **Monitor de Clics (`mouse_logger.py`):** Registra los clics del ratón, indicando qué botón se usó y las coordenadas (X, Y) del puntero en el momento del clic. Guarda el registro en `log_mouse.txt`.
* **Monitor Combinado (`combined_logger.py`):** Ejecuta ambos monitores de forma simultánea, guardando un registro cronológico de teclas y clics en un único archivo `log_completo.txt`.
* **Código Orientado al Aprendizaje:** Cada script está detalladamente comentado para explicar la lógica detrás de cada línea de código.

***

## 🔧 Requisitos Previos

Para ejecutar estos scripts, necesitarás tener instalado lo siguiente en tu sistema:

* **Python 3.x**
* **pip** (el gestor de paquetes de Python)

***

## 🚀 Instalación

Sigue estos pasos para poner en marcha el proyecto:

1.  **Clona o descarga el repositorio:**
    ```bash
    git clone [https://github.com/S4mma3l/Keylogger-Python](https://github.com/S4mma3l/Keylogger-Python)
    ```
    (O descarga el ZIP y extráelo).

2.  **Navega al directorio del proyecto:**
    ```bash
    cd tu-repositorio
    ```

3.  **Instala las dependencias:**
    El proyecto depende de la librería `pynput`. Puedes instalarla directamente usando el archivo `requirements.txt` incluido.
    ```bash
    pip install -r requirements.txt
    ```

***

## 💻 Modo de Uso

Cada script se ejecuta desde la terminal y se detiene cerrando la ventana de la terminal (o presionando `Ctrl + C`).

### Para registrar solo pulsaciones de teclado:

```bash
python keylogger.py