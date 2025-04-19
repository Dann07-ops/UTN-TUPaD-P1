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
bas funciones para mostrar los resultados.'''


