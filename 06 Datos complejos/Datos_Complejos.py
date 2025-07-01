#1) Dado el diccionario precios_frutas 
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
1450} 
'''Añadir las siguientes frutas con sus respectivos precios: 
● Naranja = 1200 
● Manzana = 1500 
● Pera = 2300 '''
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300
print(precios_frutas)

'''2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
● Banana = 1330 
● Manzana = 1700 
● Melón = 2800'''

precios_frutas['Banana']= 1330
precios_frutas['Manzana']= 1700
precios_frutas['Melón'] = 2800
print(precios_frutas)

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
#precios.

list_Frutas= ['Banana', 'Ananá', 'Melón', 'Uva', 'Naranja', 'Manzana', 'Pera'] 

print(list_Frutas)

#4) Escribí un programa que permita almacenar y consultar números telefónicos. 
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
#• Luego, pedí un nombre y mostrale el número asociado, si existe.
'''contactos={}

for i in range(5):
    nom=input(f"Ingrese los nombres de los contatos {i+1}: ") 
    num=input("Ingrese el numero de {nom}:")
    contactos[nom] = num
nom_busqueda= input("Ingrese el nombre que desea buscar: ")
if nom_busqueda in contactos:
    print(f"El número de {nom_busqueda} es: {contactos[nom_busqueda]}")  
else:
    print("El nombre que busca no esta entre los contactos ") '''

#5) Solicita al usuario una frase e imprime: 
#• Las palabras únicas (usando un set). 
#• Un diccionario con la cantidad de veces que aparece cada palabra.    

'''frase= input("Ingrese una frase: ")

palabras= frase.split()

palabras_unicas= set(palabras)

recuento={}

for palabra in palabras:
    if palabra in recuento:
        recuento[palabra]+=1
    else:
        recuento[palabra] = 1

print('Palabras unicas: ', palabras_unicas)
print('Recuento: ', recuento)'''

#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
#Luego, mostrá el promedio de cada alumno.

'''notas_alumnos= {}

for i in range(3):
     nom=input(f"Ingrese el nombre del alumno {i+1}: ") 
     notas=[]
     for j in range(3):
        nota=float(input(f"Ingrese la nota {j+1} de {nom}: "))
        notas.append(nota)
     notas_alumnos[nom]= tuple(notas)

print("\nPromedios de los alumnos:")
for nombre, notas in notas_alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}") '''

'''#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
#y Parcial 2: 
#• Mostrá los que aprobaron ambos parciales. 
#• Mostrá los que aprobaron solo uno de los dos. 
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir). 
 
lista_parcial1={"Daniel", "Manuel", "Marcos", "Pedro", "Juan"}
lista_parcial2={"Daniel","Julian", "Marcos", "Jennifer", "Ciro"}
#• Mostrá los que aprobaron ambos parciales.
ambos_parciales= lista_parcial1 & lista_parcial2    #Intersección

#• Mostrá los que aprobaron solo uno de los dos.
solo_uno= lista_parcial1 ^ lista_parcial2           #Diferencia simetrica

#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir). 
un_parcial= lista_parcial1 | lista_parcial2         #Union

print("Aprobaron ambos parciales:", ambos_parciales)
print("Aprobaron solo uno de los dos:", solo_uno)
print("Aprobaron al menos un parcial:",un_parcial)'''

'''8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
Permití al usuario: 
• Consultar el stock de un producto ingresado. 
• Agregar unidades al stock si el producto ya existe. 
• Agregar un nuevo producto si no existe.

stock_productos={"harina":50, "arroz":20, "azucar":15, "leche":30, "galletitas":60 }

seguir= True



while seguir:
     print("\n--- Menú de opciones ---")
     print("1. Consultar stock")
     print("2. Agregar stock")
     print("3. Salir")

     opcion=input("Elija una opcion del 1 al 3: ")

     if opcion == "1":
        producto = input("Ingresá el nombre del producto: ").strip().lower()
        if producto in stock_productos:
            print(f"Stock de {producto}: {stock_productos[producto]} unidades")
        else:
            print(f"{producto} no está registrado en el inventario.")

     elif opcion == "2":
        producto = input("Ingresá el nombre del producto: ").lower()
        cantidad = int(input(f"Ingresá la cantidad a agregar para {producto}: "))
        if producto in stock_productos:
            stock_productos[producto] += cantidad
            print(f"Nuevo stock de {producto}: {stock_productos[producto]}")
        else:
            stock_productos[producto] = cantidad
            print(f"{producto} agregado al inventario con {cantidad} unidades.")
     elif opcion == "3":
        print("¡Hasta luego!")
        seguir = False  

     else:
        print("Opción no válida. Por favor, ingresá 1, 2 o 3.")'''


#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. 
'''
agenda={("Lunes","10:00") : "Clase de Matematicas", ("Martes", "09:00"): "Running", ("Miercoles", "15:00"): "Andar en bicicleta ", 
        ("Jueves", "16:00"):"Reunion de consorcio",("Viernes", "14:00"): "Clase de pilates" }

dia=input("Ingresa un día de la semana:   ").strip().capitalize()
hora= input("Ingresa una hora:  " ).strip().lower()

clave=(dia, hora)

if clave in agenda:
    print(f"Tenés: {agenda[clave]}")
else:
    print("No hay ninguna actividad registrada para ese día y hora.")'''

#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
#diccionario donde: 
#• Las capitales sean las claves. 
#• Los países sean los valores. 


paises_a_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Francia": "París",
    "Italia": "Roma",
    "Japón": "Tokio"
}


capitales_a_paises = {}

for pais, capital in paises_a_capitales.items():
    capitales_a_paises[capital] = pais


print("Diccionario invertido (capital → país):")
for capital, pais in capitales_a_paises.items():
    print(f"{capital}: {pais}")







    
   
  
