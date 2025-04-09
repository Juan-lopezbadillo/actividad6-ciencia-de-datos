# Ejercicio 3
# Escribir un programa en Python que guarde la temperatura mínima y máxima de los
# últimos 5 días. El programa debe recibir la información, almacenarla y mostrar:
# ● La temperatura media de cada día
# ● Los días con menor temperatura
# ● Después de almacenar la información de los 5 días, el programa debe recinir una
# temperatura más por teclado y mostrar los días cuya temperatura máxima coincide
# con ella. si no existe ningún día se muestra un mensaje de información.


def pedir_temperatura(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("⚠️ Por favor ingresa un número entero válido.")

temperaturas = []

for i in range(1,6):
    print(f"\nDia {i}")
    min_temp = pedir_temperatura(f"Agrega la temperatura minima del dia {i}: ")
    max_temp = pedir_temperatura(f"Agrega la temperatura maxima del dia {i}: ")

    dia = {"dia": i, 
           "min": min_temp, 
           "max": max_temp
}
    temperaturas.append(dia)

last_temp = int(input("Agrega una ultima temperatura maxima:"))

# Imprimir la temperatura medio por dia 
for t in temperaturas: 
    media = (t["min"] + t["max"])/2
    print(f"Dia {t['dia']}: temperatura promedio = {media}")


temp_min_general = min(t["min"] for t in temperaturas)
dias_min_temp = [t["dia"] for t in temperaturas if t["min"] == temp_min_general]

#Imprimir lo(s) dia(s) con la minima temperatura
print("\nDia(s) con la menor temperatura:")
for dia in dias_min_temp:
    print(F"- Dia {dia}")


#identificando los dias que coinciden con la temp maxima 

temp_max_ = [t["dia"] for t in temperaturas if t["max"] == last_temp] 
if temp_max_:
    print("\nLa temperatura máxima ingresada coincide en los siguientes días:")
    for dia in temp_max_:
        print(f"- Día {dia}")
else:
    print("Ningun dia coincide con la 'maxima temperatura'.")