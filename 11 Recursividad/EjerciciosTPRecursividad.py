'''1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario

def factorial_numero(num):
    if num == 0:
        return 1
    else: 
        return num * factorial_numero(num -1)
num = int(input("Ingrese un numero entero positivo: "))    
for i in range(1, num + 1):
    print(f"El factorial de {i} es {factorial_numero(i)}")'''

'''2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
especifique.

def fibonacci_recursivo(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci_recursivo(posicion-1) + fibonacci_recursivo(posicion-2)
num=int(input("Ingrese un numero para calcular su valor en la serie de fibonacci:")) 
for i in range(num +1):    
    print(fibonacci_recursivo(i)) ''' 

'''3) Crea una función recursiva que calcule la potencia de un número base elevado a un
exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un
algoritmo general.

def potencia_num(n, m):
    if m == 0:
        return 1
    else: 
        return n * potencia_num(n, m-1)
num= int(input("Ingrese un numero entero poitivo:"))
poten= int(input("Ingrese un numero para colocar de potencia:"))    

print(f"{num} elevado a {poten} es: {potencia_num(num, poten)}") '''

'''4) Crear una función recursiva en Python que reciba un número entero positivo en base 
decimal y devuelva su representación en binario como una cadena de texto. 

def decimal_a_binario(num):
    if num == 0:
        return ""
    else: 
        return decimal_a_binario(num // 2) + str(num % 2)
#n=int(input("Ingrese un numero entero positivo: "))  # Lo usamos en casos de pedir al usuario que ingrese un numero entero positivo
n1= 13                                              # Lo usamos para ingresar un numero entero positivo manualmente
binario= decimal_a_binario(n1)

print(binario if binario else "0") #Usamos la condición print(binario if binario else "0") para asegurarnos de que 0 se represente correctamente.'''

'''5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no 
lo es. 
     Requisitos: 
La solución debe ser recursiva. 
No se debe usar [::-1] ni la función reversed(). 

def es_palindromo(palabra):
    palabra = palabra.replace(" ", "") #Este ordenamiento hace que el texto no tenga espacio
    palabra = palabra.replace("á", "a") # Con este ordenamiento sacamos las tildes
    palabra = palabra.replace("é","e")  # Con este ordenamiento sacamos las tildes
    palabra = palabra.replace("í", "i") # Con este ordenamiento sacamos las tildes
    palabra = palabra.replace("ó", "o") # Con este ordenamiento sacamos las tildes
    palabra = palabra.replace("ú", "u") # Con este ordenamiento sacamos las tildes

    a = 0
    b=len(palabra) - 1  

    for i in range(0, len(palabra)):
       if palabra[a] == palabra [b]:
          a += 1
          b -= 1
       else:
         return False  
    return True

palabra= input("Ingrese una palabra o una frase:")
print(es_palindromo(palabra))'''

'''6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
número entero positivo y devuelva la suma de todos sus dígitos. 

def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + suma_digitos(n//10)
num= int(input("Ingrese un numero entero positivo: "))
print(suma_digitos(num))  '''

'''7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n 
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al 
último nivel con un solo bloque. 
 
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el 
nivel más bajo y devuelva el total de bloques que necesita para construir toda la 
pirámide.

def  contar_bloques(n):
    if n == 0:
        return 0
    else: 
        return n + contar_bloques(n-1)
num= int(input("Ingrese el numero de bloques: "))    
print(contar_bloques(num)) '''

'''8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
aparece ese dígito dentro del número. '''

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    if numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)
n= int(input("Ingrese un número entero positivo: ")) 
d= int(input("Ingrese un numero para el digito entre 0 y 9: ") )  
print(contar_digito(n, d))    
      





    
    

