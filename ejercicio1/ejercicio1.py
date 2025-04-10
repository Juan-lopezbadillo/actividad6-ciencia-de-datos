# Ejercicio 1
# Escribir un programa en Python que declare una lista y la vaya llenando de números hasta
# que introduzcamos un número negativo. Entonces se debe imprimir el vector (sólo los
# valores introducidos).


lista = []

while True: 
    try:
        numero = float(input("escribe un numero positivo para agregar a la lista o un numero negativo para terminar: "))
        if numero >= 0:
            lista.append(numero)
        else:
            lista.append(numero)
            print(lista)
            break
    except ValueError:
        print("Agrega un numero")

