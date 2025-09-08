import tkinter as tk  # Biblioteca gráfica nativa de Python

def mostrar_interfaz():
    # Crear ventana principal
    ventana = tk.Tk()
    ventana.title("programa de angel")
    ventana.geometry("500x400")

    # Etiqueta principal
    etiqueta = tk.Label(
        ventana,
        text="¡Hola, sobrino! ¿selecciona?",
        font=("Arial", 14)
    )
    etiqueta.pack(pady=10)

    # Variable para guardar la opción seleccionada
    opcion_seleccionada = tk.StringVar(value="Ninguno")

    # Lista de opciones disponibles
    opciones = ["uno", "dos", "tres", "cinco"]

    # Crear botones de opción (Radiobutton) para cada animal
    botones_opcion = []
    for animal in opciones:
        rb = tk.Radiobutton(
            ventana,
            text=animal,
            variable=opcion_seleccionada,
            value=animal
        )
        rb.pack(anchor="w", padx=20)
        botones_opcion.append(rb)  # Guardamos referencia por si la necesitamos

    # Función para mostrar la opción elegida
    def mostrar_opcion():
        etiqueta.config(text=f"¡Elegiste: {opcion_seleccionada.get()}!")

    # Botón para confirmar la elección
    boton_confirmar = tk.Button(
        ventana,
        text="Confirmar elección",
        command=mostrar_opcion
    )
    boton_confirmar.pack(pady=10)

    # Función para saludar y reiniciar la selección
    def saludar_y_reiniciar():
        etiqueta.config(text="¡Hola otra vez!")
        opcion_seleccionada.set("Ninguno")  # Reinicia la selección

    # Botón para saludar y reiniciar
    boton_extra = tk.Button(
        ventana,
        text="reiniciar",
        command=saludar_y_reiniciar
    )
    boton_extra.pack(pady=10)

    # Iniciar el bucle principal de la interfaz
    ventana.mainloop()

# Ejecutar la interfaz si se corre directamente este archivo
if __name__ == "__main__":
    mostrar_interfaz()