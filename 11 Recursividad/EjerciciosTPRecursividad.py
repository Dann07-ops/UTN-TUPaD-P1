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
algoritmo general.'''

def potencia_num(n, m):
    if m == 0:
        return 1
    else: 
        return n * potencia_num(n, m-1)
num= int(input("Ingrese un numero entero poitivo:"))
poten= int(input("Ingrese un numero para colocar de potencia:"))    

print(f"{num} elevado a {poten} es: {potencia_num(num, poten)}")
    
    

