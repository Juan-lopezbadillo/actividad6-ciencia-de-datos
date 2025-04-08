# Ejercicio 2
# Escribir un programa en Python que declare tres listas ‘lista1’, ‘lista2’ y ‘lista3’ de cinco
# enteros cada uno, pida valores para ‘lista1’ y ‘lista2’ y calcule lista3=lista1+lista2.

lista_1 = []
lista_2 = []
lista_3 = []

while True:
    try:
        if len(lista_1) < 5:
            numero = int(input("Agregue un numero entero: "))
            lista_1.append(numero)
        elif len(lista_2) < 5:
            numero = int(input("Agregue un numero entero: "))
            lista_2.append(numero) 
        else:
            for i in range(len(lista_1)):
                lista_3.append(lista_1[i] + lista_2[i])
            print(f"lista uno:{lista_1},\nlista dos:{lista_2},\nlista tres:{lista_3}")
            break
    except: 
        print("agrega un numero entero")
