import random
import time

# Definición de las palabras y pistas
palabras = ["python", "programación", "computadora", "internet", "tecnología", "datos", "algoritmo"]
pistas = [
    "Lenguaje de programación poderoso y versátil.",
    "Actividad de escribir código para crear software.",
    "Dispositivo electrónico que procesa datos.",
    "Red global de interconexión de dispositivos.",
    "Estudio y aplicación de técnicas en la industria.",
    "Información procesada y utilizada por sistemas.",
    "Secuencia finita de instrucciones bien definidas."
]

# Función para jugar
def jugar_adivina_palabra():
    print("¡Bienvenido al juego Adivina la Palabra!")
    print("Tienes 15 segundos para adivinar la palabra a partir de la pista.")
    print("¡Que empiece el juego!\n")

    # Seleccionar una palabra y su pista aleatoriamente
    indice = random.randint(0, len(palabras) - 1)
    palabra_secreta = palabras[indice]
    pista = pistas[indice]

    # Mostrar la pista
    print("Pista:", pista)
    
    # Contador de tiempo
    tiempo_inicio = time.time()
    
    # Input del usuario
    intento = input("\nTu respuesta: ").strip().lower()
    
    # Calcular tiempo empleado
    tiempo_empleado = time.time() - tiempo_inicio
    
    # Verificar la respuesta
    if intento == palabra_secreta:
        print("\n¡Correcto! Has adivinado la palabra.")
    else:
        print("\n¡Incorrecto! La palabra correcta era:", palabra_secreta)
    
    # Mostrar tiempo empleado
    print("Tiempo empleado: {:.2f} segundos".format(tiempo_empleado))

# Ejecutar el juego
jugar_adivina_palabra()
