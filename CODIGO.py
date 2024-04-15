## Un sistema procesará un conjunto de números en grupos de cuatro (4). En cada cuarteto se hará la suma del primero y el último, y el producto del segundo y el tercero. Se asumirá que la suma es el resultado de obtener el logaritmo del producto hallado, en una base logarítmica que no se conoce. Se conformará de este modo una Ecuación Logarítmica y se resolverá, mostrando el resultado. 
## Se deberá llevar un conteo de los casos en que se logró y en los cuales no se logró conformar una ecuación exponencial.  

import math

def factorial_iterativo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def factorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

def ordenar_numeros(numeros):
    for i in range(len(numeros)):
        for j in range(len(numeros) - i - 1):
            if numeros[j] > numeros[j + 1]:
                numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
    return numeros

def buscar_numero(numeros, numero_a_buscar):
    izquierda, derecha = 0, len(numeros) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if numeros[medio] == numero_a_buscar:
            return medio
        elif numeros[medio] < numero_a_buscar:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

def procesar_numeros(numeros):
    exitosos = 0
    fallidos = 0
    resultados = []

    numeros_ordenados = ordenar_numeros(numeros)

    for i in range(0, len(numeros_ordenados), 4):
        if i+3 < len(numeros_ordenados):
            factorial = factorial_iterativo(numeros_ordenados[i])
            producto = numeros_ordenados[i+1] * numeros_ordenados[i+2]

            if producto > 0 and factorial > 0:
                try:
                    base = math.exp(factorial / producto)
                    resultados.append(base)
                    exitosos += 1
                except:
                    fallidos += 1
            else:
                fallidos += 1
        else:
            fallidos += 1

    return resultados, exitosos, fallidos

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] 
numero_a_buscar = 4  

resultados, exitosos, fallidos = procesar_numeros(numeros)

print(f"Resultados: {resultados}")
print(f"Casos exitosos: {exitosos}")
print(f"Casos fallidos: {fallidos}")

indice = buscar_numero(numeros, numero_a_buscar)
if indice != -1:
    print(f"El número {numero_a_buscar} se encontró en el índice {indice}.")
else:
    print(f"El número {numero_a_buscar} no se encontró en la lista.")
