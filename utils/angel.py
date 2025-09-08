import time
# Este módulo contiene funciones simples para practicar programación en Python.

# Función que imprime un saludo en pantalla.
def saludar():
    print("Hola desde la función 'saludar' en angel.py")

# Función que cuenta del 1 al 10 usando un bucle for.
def contar_hasta_diez():
    print("Contando del 1 al 10:")
    for i in range(1, 11):
        time.sleep(1)
        print(i)

# Función que recibe un número y verifica si es igual a 10.
# Si el número es 10, imprime un mensaje especial.
def verificar_numero(numero):
    print(f"Has ingresado el número: {numero}")
    if numero == 10:
        print("¡El número es 10!")
    else:
        print("Este número no es 10.")
