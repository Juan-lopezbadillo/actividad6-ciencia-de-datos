# Ejercicio 4
# Crea un programa en Python que permita adivinar un número. La aplicación genera un
# número aleatorio del 1 al 100. A continuación, va pidiendo números y va respondiendo si
# el número a adivinar es mayor o menor que el introducido, así como el número de intentos
# que quedan, se contarán con 10 intentos para adivinar el número). El programa termina
# cuando se acierta el número y debe indicar en que intento fue acertado, si se llega al límite
# de intentos, el programa debe mostrar que se había generado


import random

numero_secreto = random.randint(1,100)
intentos = 10

print("Estamos listo para jugar")
print("debes adivinar el numero secreto (un numero entre 1, 100). Tienes maximo 10 intentos\n")

for intento in range(1, intentos + 1):
    try:
        while True:
            try:
                adivinar = int(input(f"Intento {intento}: Ingresa un numero entre 1 y 100: "))
                if 1 <= adivinar <= 100:
                    break
                else:
                    print("😒Debes adivinar el numero de 1 al 100😒\n")
            except ValueError:
                print("😒 Debes inggresar un numero entero entre 1 y 100")

        if adivinar == numero_secreto: 
            print(f"🥳 ¡Correcto! Adivinaste el numero en el intento {intento}.")
            break

        elif adivinar < numero_secreto:
            print("⬆️ El numero secreto es mayor, intenta con un numero mas alto.")
        else:
            print("⬇️ El numero seccreto es menor, intenta con un numero mas bajo.")

        print(f"Te quedan {intentos - intento} intento(s).\n")
    
    except ValueError:
        print("😒 Debes inggresar un numero entero entre 1 y 100")

else: 
    print(f"Se acabaron los intentos. el numero secreto es: {numero_secreto}")