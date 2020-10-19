#Ejercicio 1
#Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
# def max_de_tres():
#     lista = []
#     contador = 3
#     print('Introduzca tres números enteros:')
#     while contador > 0:
#         a = input()
#         a = int(a)
#         lista.append(a)
#         contador = contador-1
#     mayor=lista[0]
#     for i in lista:
#         if i > mayor:
#             mayor = i
#     print(f'El mayor número introducido es: {mayor}')
# max_de_tres()

#########################################################################################################
#Ejercicio 2
#Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene
#la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.
# lista = []
# salir = False
# def long_cadena(cadena):
#     contador = 0
#
#     for i in cadena:
#         contador += 1
#         print(f'La palabra "{cadena}" tiene {contador} caracteres')
#
# print('Introduzca una o varias cadenas de caracteres (Para terminar escriba "FIN")')
# while salir != True:
#     palabra = input()
#     palabra = str(palabra)
#     if palabra == 'FIN':
#         salir = True
#     else:
#         lista.append(palabra)
# c = 0
#
# for i in lista:
#     long_cadena(i)
#     c += 1
#
# print(f'Ha escrito {c} palabras')

#########################################################################################################
#Ejercicio 3
#Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
#
# def comprobar_vocal():
#     vocal = False
#     caracter = input()
#     caracter = str(caracter)
#     while len(caracter) > 1:
#         print('No ha introducido una sola letra, por favor inténtelo de nuevo')
#         caracter = input()
#         caracter = str(caracter)
#     if caracter == 'a' or caracter == 'e' or caracter == 'i' or caracter == 'o' or caracter == 'u':
#         vocal = True
#         return vocal
#     else:
#         return vocal
#
# print('Introduzca una letra para saber si es una vocal')
# if comprobar_vocal() == True:
#     print('Es una vocal')
# else:
#     print('No es una vocal')

#########################################################################################################
#Ejercicio 4
#Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente
#todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4])
#debería devolver 24.
# lista = []
# salir = False
# def sum(lista):
#     suma = 0
#     for i in lista:
#         suma = suma + i
#     return suma
#
# def multip(lista):
#     producto = 1
#     for i in lista:
#         producto = producto * i
#     return producto
#
# print('Introduzca tantos números como quiera en la lista para sumarlos y multiplicarlos. '
#       '\n(Para terminar introduzca "00")')
# while salir != True:
#     numero = input()
#     numero = int(numero)
#     if numero == 00:
#         salir = True
#     else:
#         lista.append(numero)
#
# print(f'Los números introducidos son: {lista}')
# print(f'La suma de todos los números de la lista es: {sum(lista)}')
# print(f'El producto de todos los números de la lista es: {multip(lista)}')

#########################################################################################################
#Ejercicio 5
#Definir una función inversa() que calcule la inversión de una cadena.
#Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
# def inversa(cadena):
#     cadena_inversa=""
#     for caracter in cadena:
#         cadena_inversa= caracter + cadena_inversa
#     return cadena_inversa
# print('Introduzca una cadena de caracteres para obtener su inversa')
# cadena = input()
# cadena = str(cadena)
# print(f'La inversa de "{cadena}" es "{inversa(cadena)}"')

#########################################################################################################
#Ejercicio 6
#Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo
#aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.
# def es_palindromo(cadena):
#     cadena = cadena.upper()
#     palindromo = False
#     cadena_inversa=""
#     for caracter in cadena:
#         cadena_inversa= caracter + cadena_inversa
#     if cadena == cadena_inversa:
#         palindromo = True
#         return palindromo
#     else:
#         return palindromo
# print('Introduzca una palabra para comprobar si es un palíndromo')
# cadena = input()
# cadena = str(cadena)
# if es_palindromo(cadena):
#     print(f'"{cadena}" es un palíndromo')
# else:
#     print(f'"{cadena}" no es un palíndromo')

#########################################################################################################
#Ejercicio 7
#Crea un programa en python para rellenar una lista de 15 número enteros:
# -Con valores aleatorios entre 1 y 10, y a continuación diga cuantos pares e impares hay.
# -Con valores aleatorios entre 1 y 10, y a continuación sume los que estén en posiciones que
#  son múltiplos de 3.
# -Con los primeros valores de la serie de Fibonacci.
# -Con valores introducidos por el usuario, y a continuación que los imprima al revés.
# -Con valores introducidos por el usuario, donde cada valor se debe pedir de nuevo hasta que esté entre 1 o 10.
# -Con valores introducidos por el usuario, que deben formar una secuencia creciente.
# -Con valores introducidos por el usuario, que no deben estar repetidos.
import random
print('¿Cómo va a querer rellenar la lista?')
print('1. Números aleatorios del 1 al 10 (Diferenciando Pares e Impares)')
print('2. Números aleatorios del 1 al 10 (Sumando números con posiciones que son múltiplos de 3)')
print('3. Con los primeros 15 valores de la sucesión de Fibonacci')
print('4. Valores introducidos por usted y devolviéndolos del revés')
print('5. Valores introducidos por usted (solo valores entre 1 y 10)')
print('6. Valores introducidos por usted (en orden creciente)')
print('7. Valores introducidos por usted (sin repetidos)')
respuesta = input()
respuesta = int(respuesta)
salir = False
while salir != True:
    lista = []
    contador = 15
    if respuesta == 1:
        lista_pares = []
        lista_impares = []
        while contador > 0:
            lista.append(random.randint(1, 10))
            contador -= 1
        print(f'La lista es: {lista}')
        for i in lista:
            if i%2 == 0:
                lista_pares.append(i)
            else:
                lista_impares.append(i)
        print(f'Los números pares de la lista son: {lista_pares}')
        print(f'Los números impares de la lista son: {lista_impares}')
    elif respuesta == 2:
        print()



