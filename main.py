import time
import utils.angel  # Importa todo el módulo

def main():
    while True:
        utils.angel.saludar()  # Llama a la función usando el nombre del módulo
        time.sleep(2)

if __name__ == "__main__":
    main()
