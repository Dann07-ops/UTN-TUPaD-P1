'''1. Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal.
#Definir funciones:
def imprimir_hola_mundo():
    print("Hola Mundo!")
#Programa principal:
imprimir_hola_mundo()

2. Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de-
volver: “Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario.
#Defirnir funciones:
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

#Programa principal:
nombre = input("Ingrese un nombre: ")
saludar_usuario(nombre)

3. Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe-
dir los datos al usuario y llamar a esta función con los valores in-
gresados.

#Definir Funciones:
def informacion_personal(nombre,apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#Programa Principal:
nombre= input("Ingrese su nombre: ")
apellido= input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su dirrección:") 
informacion_personal(nombre,apellido, edad, residencia)

 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
dio como parámetro y devuelva el área del círculo. calcular_peri
metro_circulo(radio) que reciba el radio como parámetro y devuel
va el perímetro del círculo. Solicitar el radio al usuario y llamar am
bas funciones para mostrar los resultados.
import math  # Importa el módulo math para acceder a la constante pi
# Definir Funciones:
def calcular_area_circulo(radio):
    return math.pi * radio**2  # Fórmula para calcular el área
def calcular_perimetro_circulo(radio):
    return 2* math.pi * radio # Fórmula para calcular el perímetro
# Programa principal:
radio= float(input("Ingrese un número para el radio:"))
area = calcular_area_circulo(radio)
perímetro = calcular_perimetro_circulo(radio)
print(f"El area es {area} y el perímetro es {perímetro}")

 5. Crear una función llamada segundos_a_horas(segundos) que reciba
 una cantidad de segundos como parámetro y devuelva la cantidad
 de horas correspondientes. Solicitar al usuario los segundos y mos
trar el resultado usando esta función

# Definir funciones:
def segundos_a_horas(segundos):
    return segundos / 3600 # Formula para comvertir segundos a horas

# Programa principal:
segundos= int(input("Ingrese segundos: ")) # Solicita los segundos al usuario
horas = segundos_a_horas(segundos) # Convierte los segundos a horas
# Imprime la salida con dos decimales 
print(f"{horas:.2f} hs")

6. Crear una función llamada tabla_multiplicar(numero) que reciba un
 número como parámetro y imprima la tabla de multiplicar de ese
 número del 1 al 10. Pedir al usuario el número y llamar a la fun
ción.
# Definir funcines:
def tabla_multiplicar(numero):
    for i in range(1,11): # Itera 1 al 10
        print(f"{i} * 1 = {i * 1}")# Imprime la multiplicación
    

# Programa principal:
num = int(input("Ingrese un número: "))
tabla_multiplicar(num) # Llama a la función

7. Crear una función llamada operaciones_basicas(a, b) que reciba
 dos números como parámetros y devuelva una tupla con el resulta
do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re
sultados de forma clara.
#Definir funciones:
def operaciones_basicas(a, b):
    suma = a + b 
    resta = a - b
    multiplicacion = a * b
    # Evitar dividir por cero
    if b != 0:
        division = a / b
    else:
        print("No se puede realizar division") 
        input("Ingrese otro numero: ")  
    return (suma, resta, multiplicacion , division)     
  
#Programa principal:
num1= int(input("Ingrese un Primer numero: "))
num2= int(input("Ingrese un segundo numero: "))
resultado = operaciones_basicas(num1, num2)
# Mostar resultados de forma clara:

print(f"Suma: {resultado[0]}")
print(f"resta: {resultado[1]}")
print(f"Multiplicacion: {resultado[2]}")
print(f"Division: {resultado[3]}")

 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
 peso en kilogramos y la altura en metros, y devuelva el índice de
 masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun
ción para mostrar el resultado con dos decimales.
#Definir funciones:
def calcular_imc(peso, altura):
   imc = peso/altura **2 
   return imc

     
#Programa principal:
peso= float(input("Ingrese su peso en Kg: "))
altura= float(input("Ingrese su altura Metros: "))
imc= calcular_imc(peso, altura)
print(f"Su imc es {imc:.2f}")


 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
 una temperatura en grados Celsius y devuelva su equivalente en
 Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
 resultado usando la función.
#Definir funciones:
def celsius_a_fahrenheit(celsius):
     resultado =  9/5 * celsius + 32 #convertir celsus a fahrenheit
     return resultado
#Programa principal:
temp = float(input("Ingrese una temperatura en grados celsius: "))
fahrenheit = celsius_a_fahrenheit(temp)
print(f"Su temperatura ingresada {temp} °C es equivalente a: {fahrenheit} °F ")

 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
 tres números como parámetros y devuelva el promedio de ellos.
 Solicitar los números al usuario y mostrar el resultado usando esta
 función
#Definir funciones:
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio
#Programa principal:
num_1 = float(input("Ingrese un número: ")) 
num_2 = float(input("Ingrese un segundo número: ")) 
num_3 = float(input("Ingrese un tercer número: ")) 
prom = calcular_promedio(num_1,num_2,num_3)
print(f"El promedio es de: {prom}")'''
















