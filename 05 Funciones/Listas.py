# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función 
#range. 
for numeros in range(1,101): # verificar a futuro jaj
    if numeros % 4 == 0: 
       print(numeros) 

#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el 
#penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el 
#indexing con números negativos! 
comida= ["pizza","empanadas","hamburguesa","pan","pastas"]
print(comida[-3])

#3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por 
#pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por 
#ejemplo: lista_vacia = [] 
lista_vacia= []
lista_vacia.append("casa")
lista_vacia.append("perro")
lista_vacia.append("automovil")
print(lista_vacia)

#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, 
#respectivamente.  Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra 
#en los videos o bien investigar cómo funciona el indexing con números negativos! 
#animales = ["perro", "gato", "conejo", "pez"] 
animales = ["perro", "gato", "conejo", "pez"]
animales[-3] = "loro"
animales[-1] = "oso"
print(animales)

#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza. 
numeros2=[8,15,3,22,7] # Crea una lista llamada numeros con los elementos 8,15,3,22,7
numeros2.remove(max(numeros2)) #Utilizamos el operador remove para eliminar el elemento con el valor maximo
print(numeros2) # Nos muestra por pantalla la lista sin el elementon con el valor maximo

#6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por 
#pantalla los dos primeros. 
numeros3=list(range(10,31,5))
print(numeros3[0:2])

#7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores 
#cualesquiera. 
#autos = ["sedan", "polo", "suran", "gol"] 
autos = ["sedan", "polo", "suran", "gol"] 
autos [1] = "up"
autos[2] = "fox"
print(autos)

#8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append 
#directamente. Imprimir la lista resultante por pantalla. 
dobles = []
dobles.append(10)
dobles.append(20)
dobles.append(30)
print(dobles)

#9) Dada la lista “compras”, cuyos elementos representan los productos comprados por 
#diferentes clientes: 
#compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], 
#["agua"]] 
#a) Agregar "jugo" a la lista del tercer cliente usando append. 
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente. 
#c) Eliminar "pan" de la lista del primer cliente.  
#d) Imprimir la lista resultante por pantalla 
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]] 
compras[2].append("jugo")
compras[1][1]= "tallarines"
compras[0].remove("pan")
print(compras) 

#10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos: 
#● Posición lista_anidada[0]: 15 
#● Posición lista_anidada[1]: True 
#● Posición lista_anidada[2][0]: 25.5 
#● Posición lista_anidada[2][1]: 57.9 
#● Posición lista_anidada[2][2]: 30.6 
#● Posición lista_anidada[3]: False 
#Imprimir la lista resultante por pantalla. 
lista_anidada= [15,True,[25.5,57.9,30.6],False]
print( lista_anidada)


