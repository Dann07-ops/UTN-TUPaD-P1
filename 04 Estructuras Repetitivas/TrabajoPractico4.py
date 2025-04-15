'''1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
¡Claro! Aquí tienes un ejemplo de cómo puedes implementar ese programa en Python:
# Imprimir números del 0 al 100, uno por línea
for num_nat in range(0,101): # range(0,101) genera números de 0 a 100
    print(num_nat)

2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
dígitos que contiene. 

num=int(input("Ingrese un número entero: "))
i = 0
while num > 0:
    num = num // 10 
    i+=1
print(f"tiene {i} digitos ")

3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
dados por el usuario, excluyendo esos dos valores. 

# Solicitar al usuario dos valores enteros
valor1 = int(input("Ingrese el primer valor entero: "))
valor2 = int(input("Ingrese el segundo valor entero: "))

# Determinar el rango correcto: inicio y fin
inicio = min(valor1, valor2) + 1  # El menor valor + 1
fin = max(valor1, valor2)         # El mayor valor

# Inicializar la suma y el contador
suma = 0
contador = inicio

# Usar un bucle while para recorrer los números entre inicio y fin
while contador < fin:
    suma += contador  # Sumar el valor actual
    contador += 1     # Incrementar el contador

# Mostrar el resultado
print(f"La suma de los números entre {valor1} y {valor2}, excluyendo los extremos, es: {suma}")    

4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
un 0. 

n = int(input("Ingrese un numero:"))
suma_total = 0

while n != 0:
    suma_total += n
    n = int(input("Ingrese otro número: "))
print(f"La suma total de los números ingresados es de: {suma_total}")    

5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 

import random
num_aliatorio = random.randint(0,9)
intentos= 0
print("Bienvenido al juego de adivinanza ")
print("Adivina un numero en al azar entre 0 y 9 ")
while intentos != num_aliatorio:
    intentos = int(input("Ingresa un número: "))
    intentos = intentos +1 
    if intentos < num_aliatorio:
        print("El número secreto es mayor. Inténtalo de nuevo.")
    elif intentos > num_aliatorio:
        print("El número secreto es menor. Inténtalo de nuevo.")
print(f"El número de intentos fue de: {intentos}")  

6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
entre 0 y 100, en orden decreciente.

for x in range(100,-1,-2):
    print(x)


7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
número entero positivo indicado por el usuario. '''
suma = 0
num_bucle = 0

num_usuario = int(input("Ingrese un número natural: "))

for num_bucle in range(0,num_usuario +1):
    suma+= num_bucle
print(f"La suma de los números desde 0 hasta {num_usuario} es: {suma}")    







