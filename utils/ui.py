import tkinter as tk  # Importamos la biblioteca gráfica nativa de Python

def mostrar_interfaz():
    # Creamos la ventana principal
    ventana = tk.Tk()
    ventana.title("Aprendiendo con Python")  # Título de la ventana
    ventana.geometry("500x400")  # Tamaño de la ventana en píxeles

    # Creamos una etiqueta de texto para mostrar un mensaje inicial
    etiqueta = tk.Label(
        ventana,
        text="¡Hola, angel! ¿Cuál es tu animal favorito?",
        font=("Arial", 14)
    )
    etiqueta.pack(pady=10)  # Mostramos la etiqueta con espacio vertical

    # Creamos una variable para guardar la opción seleccionada
    opcion_seleccionada = tk.StringVar(value="Ninguno")

    # Lista de opciones que el usuario puede elegir
    opciones = ["uno", "dos", "tres", "cinco"]

    # Creamos un botón de opción (Radiobutton) para cada animal
    for animal in opciones:
        rb = tk.Radiobutton(
            ventana,
            text=animal,  # Texto que se muestra
            variable=opcion_seleccionada,  # Variable compartida
            value=animal  # Valor que se asigna si se selecciona
        )
        rb.pack(anchor="w", padx=20)  # Alineamos a la izquierda con margen

    # Función que actualiza el texto de la etiqueta según la opción elegida
    def mostrar_opcion():
        etiqueta.config(text=f"¡Elegiste: {opcion_seleccionada.get()}!")

    # Botón para confirmar la elección del animal
    boton_confirmar = tk.Button(
        ventana,
        text="Confirmar elección",
        command=mostrar_opcion  # Llama a la función cuando se hace clic
    )
    boton_confirmar.pack(pady=10)

    # Botón adicional para saludar de nuevo
    boton_extra = tk.Button(
        ventana,
        text="Haz clic para saludar",
        command=lambda: etiqueta.config(text="¡Hola otra vez!")
    )
    boton_extra.pack(pady=10)

    # Iniciamos el bucle principal de la interfaz gráfica
    ventana.mainloop()

# Si ejecutamos este archivo directamente, mostramos la interfaz
if __name__ == "__main__":
    mostrar_interfaz()