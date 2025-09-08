import time
import utils.angel  # Importamos todo el módulo angel.py desde la carpeta utils

def main():
    while True:
        print("\n--- Ciclo principal ejecutándose ---")
        
        # Llama a la función que imprime un saludo
        # utils.angel.saludar()

        # Llama a la función que cuenta del 1 al 10
        # utils.angel.contar_hasta_diez()

        # Llama a la función que verifica si un número es igual a 10
        # Puedes cambiar el número para probar diferentes casos
        # utils.angel.verificar_numero(10)
        # utils.angel.verificar_numero(7)

        # Espera 5 segundos antes de repetir el ciclo
        time.sleep(5)

if __name__ == "__main__":
    main()
