'''1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
# Solicitar edad
edad= int(input("Igrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")

2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
mensaje “Desaprobado”.
# Solicitar nota
nota= int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")   

3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
operador de módulo (%) en Python para evaluar si un número es par o impar
# Solicitar el ingreso de un número Par
num_par= int(input("Ingrese un número par: "))  
if num_par % 2 == 0 : 
    print("Ha ingresado un número par")
else:
    print("Por favor,ingrese un número par: ") 

4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
siguientes categorías pertenece:
● Niño/a: menor de 12 años.
● Adolescente: mayor o igual que 12 años y menor que 18 años.
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
● Adulto/a: mayor o igual que 30 años.
# Solicitar edad
edad= int(input("Ingrese su edad: "))
if edad < 12:
    print("La categoria a la que pertenece es: Niño/a ")
elif edad >= 12 and edad < 18:
    print("La categoria a la que pertenece es: Adolescente ")    
elif edad >= 18 and edad < 30:
    print("La categoria a la que pertenece es: Adulto/a joven ")
else:
    print("La categoria a la que pertenece es: Adulto")  

5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
como una lista o un string.
# Solicitar la contraseña
contraseña= input("Ingrese su contraseña:")
#Evaluar la longitud de la contraseña
if 8 <= len(contraseña) <= 14 :
    print("Ha ingresado una contraseña correcta")
else: 
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres") 

TECNICATURA UNIVERSITARIA
EN PROGRAMACIÓN
A DISTANCIA
5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
como una lista o un string.
6)    escribir un programa que tome la lista
numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
from statistics import mode, median, mean

# Lista de números aleatorios
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular moda, mediana y media
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

# Determinar el tipo de sesgo
if media > mediana:
    sesgo = "positivo"
elif media < mediana:
    sesgo = "negativo"
else:
    sesgo = "no hay sesgo"

# Imprimir resultados
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media:.2f}")
print(f"Tipo de sesgo: {sesgo}")

7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
pantalla.
# Solicito frase o palabra
frase_palabra= input("Ingrese una frase o palabra, por favor: ")
#Verifico si el último carácter es una vocal
if frase_palabra [-1].lower() in "aeiou" :
    print(f"{frase_palabra}!")
else:
     print(f"{frase_palabra}")

8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
dependiendo de la opción que desee:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
lower() y title() de Python para convertir entre mayúsculas y minúsculas.
#Solicitar el nombre 
nombre= input("Ingrese su nombre: ")
# Solicitar la opcion 1,2 o 3
print("1. Si quiere su nombre en mayúsculas")
print("2. Si quiere su nombre en minúsculas")
print("3. Si quiere su nombre con la primera letra mayúscula")
opcion= int(input("Ingrese el número de la opción (1, 2 o 3):"))
# Procesar según la opción seleccionada
if opcion == 1:
    print(f"Tu nombre en mayúsculas es: {nombre.upper()}") 
elif opcion == 2:
    print(f"Tu nombre en minúsculas es: {nombre.lower()}")  
elif opcion == 3:
    print(f"Tu nombre con la primera letra en mayúscula es: {nombre.title()}")   
else:
     print("Opción inválida, por favor seleccione 1, 2 o 3") 

9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
por pantalla:
● Menor que 3: "Muy leve" (imperceptible).
● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
generalmente no causa daños).
● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
débiles).
● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala)
# Solicitar magnitud de terremoto
magnitud= float(input("Ingrese la magnitud del terremoto: "))
#Procesar segun la magnitud
if magnitud < 3:
    print("Muy leve (imperceptible).") 
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible).") 
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos).")
elif magnitud >= 7:
    print("Extremo (puede causar graves daños a gran escala)") 

10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
Periodo del año Estación en el
hemisferio norte
Estación en el
hemisferio sur
Desde el 21 de diciembre hasta el 20 de
marzo (incluidos) Invierno Verano
Desde el 21 de marzo hasta el 20 de junio
(incluidos) Primavera Otoño
Desde el 21 de junio hasta el 20 de
septiembre (incluidos) Verano Invierno
Desde el 21 de septiembre hasta el 20 de
diciembre (incluidos) Otoño Primavera
Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
si el usuario se encuentra en otoño, invierno, primavera o verano '''  
# Solicitar información al usuario
hemisferio = input("Ingrese el hemisferio en el que se encuentra (N para Norte, S para Sur): ").strip().upper()
mes = input("Ingrese el mes del año (por ejemplo, enero, febrero, etc.): ").strip().lower()
dia = int(input("Ingrese el día del mes (número): "))

# Clasificar estaciones según el hemisferio
if hemisferio == "N":
    if (mes == "diciembre" and dia >= 21) or mes in ["enero", "febrero"] or (mes == "marzo" and dia <= 20):
        estacion = "Invierno"
    elif (mes == "marzo" and dia >= 21) or mes in ["abril", "mayo"] or (mes == "junio" and dia <= 20):
        estacion = "Primavera"
    elif (mes == "junio" and dia >= 21) or mes in ["julio", "agosto"] or (mes == "septiembre" and dia <= 20):
        estacion = "Verano"
    elif (mes == "septiembre" and dia >= 21) or mes in ["octubre", "noviembre"] or (mes == "diciembre" and dia <= 20):
        estacion = "Otoño"
elif hemisferio == "S":
    if (mes == "diciembre" and dia >= 21) or mes in ["enero", "febrero"] or (mes == "marzo" and dia <= 20):
        estacion = "Verano"
    elif (mes == "marzo" and dia >= 21) or mes in ["abril", "mayo"] or (mes == "junio" and dia <= 20):
        estacion = "Otoño"
    elif (mes == "junio" and dia >= 21) or mes in ["julio", "agosto"] or (mes == "septiembre" and dia <= 20):
        estacion = "Invierno"
    elif (mes == "septiembre" and dia >= 21) or mes in ["octubre", "noviembre"] or (mes == "diciembre" and dia <= 20):
        estacion = "Primavera"
else:
    estacion = "Hemisferio inválido"

# Imprimir resultado
if estacion != "Hemisferio inválido":
    print(f"Actualmente te encuentras en la estación: {estacion}")
else:
    print("Por favor, ingresa un hemisferio válido (N o S).")

    
       



