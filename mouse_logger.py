# ##############################################################################
# # ATENCIÓN: DESCARGO DE RESPONSABILIDAD ÉTICO                             #
# ##############################################################################
# #
# # Este script se crea con fines educativos para demostrar cómo monitorear
# # eventos del ratón en un entorno controlado. El uso no autorizado para
# # espiar a un usuario es ilegal y no ético.
# #
# ##############################################################################

# --- IMPORTACIÓN DE LIBRERÍAS ---
# Importamos 'Listener' y 'Button' desde el módulo 'mouse' de pynput.
from pynput.mouse import Button, Listener

# --- CONFIGURACIÓN INICIAL ---
# Definimos el nombre del archivo donde se guardarán los clics.
log_file = "log_mouse.txt"

# --- DEFINICIÓN DE LA FUNCIÓN DE CALLBACK ---

# Esta función se ejecutará CADA VEZ que se haga clic con el ratón.
# Recibe las coordenadas (x, y), el botón presionado y el estado (pressed).
def on_click(x, y, button, pressed):
    """
    Gestiona el evento de clic del ratón y lo escribe en el archivo log.
    """
    # Solo registramos el evento cuando el botón es PRESIONADO.
    if pressed:
        # Abrimos el archivo en modo 'append' ('a') para añadir al final.
        with open(log_file, "a") as f:
            # Creamos una entrada de log legible.
            log_entry = f'Clic detectado con el botón {button} en la posición (X={x}, Y={y})\n'
            # Escribimos la entrada en el archivo.
            f.write(log_entry)
            # También la mostramos en la consola para feedback en tiempo real.
            print(log_entry.strip())


# --- INICIO DEL LISTENER DEL RATÓN ---

# Mensajes informativos para el usuario.
print("Detector de clics iniciado.")
# La siguiente línea es la que ha sido corregida.
print(f"Los clics se guardarán en el archivo: {log_file}") # <-- LÍNEA CORREGIDA
print("Cierra la ventana de la terminal para detener el script.")

# Creamos y gestionamos el Listener del ratón.
with Listener(on_click=on_click) as listener:
    # Mantenemos el script en ejecución para que siga escuchando.
    listener.join()