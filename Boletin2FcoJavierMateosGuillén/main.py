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
# import random
#
# salir = False
# while salir != True:
#     print('¿Cómo va a querer rellenar la lista?')
#     print('1. Números aleatorios del 1 al 10 (Diferenciando Pares e Impares)')
#     print('2. Números aleatorios del 1 al 10 (Sumando números con posiciones que son múltiplos de 3)')
#     print('3. Con los primeros 15 valores de la sucesión de Fibonacci')
#     print('4. Valores introducidos por usted y devolviéndolos del revés')
#     print('5. Valores introducidos por usted (solo valores entre 1 y 10)')
#     print('6. Valores introducidos por usted (en orden creciente)')
#     print('7. Valores introducidos por usted (sin repetidos)')
#     print('0. SALIR')
#     respuesta = input()
#     respuesta = int(respuesta)
#     contador = 15
#     if respuesta == 1:
#         lista = []
#         lista_pares = []
#         lista_impares = []
#         while contador > 0:
#             lista.append(random.randint(1, 10))
#             contador -= 1
#         print(f'La lista es: {lista}')
#         for i in lista:
#             if i%2 == 0:
#                 lista_pares.append(i)
#             else:
#                 lista_impares.append(i)
#         print(f'Los números pares de la lista son: {lista_pares}')
#         print(f'Los números impares de la lista son: {lista_impares} \n')
#
#     elif respuesta == 2:
#         lista = []
#         suma = 0
#         while contador > 0:
#             lista.append(random.randint(1, 10))
#             contador -= 1
#         print(f'La lista es: {lista}')
#         for i in lista[0::3]:
#             suma = suma + i
#         print(f'La suma de los elementos en posiciones que son múltiplo de 3 es: {suma}\n')
#
#     elif respuesta == 3:
#         lista = []
#         a = 0
#         b = 1
#         aux = 0
#         while aux < 15:
#             lista.append(a)
#             a, b = b, a+b
#             aux += 1
#         print(f'La lista es: {lista}\n')
#
#     elif respuesta == 4:
#         lista = []
#         aux = 15
#         print('Introduzca los valores')
#         while aux > 0:
#             valor = input()
#             valor = int(valor)
#             lista.append(valor)
#             aux -= 1
#         print(f'La lista introducida es: {lista}')
#         lista.reverse()
#         print(f'La lista inversa es: {lista}\n')
#
#     elif respuesta == 5:
#         lista = []
#         aux = 15
#         print('Introduzca los valores')
#         while aux > 0:
#             valor = input()
#             valor = int(valor)
#             if valor <= 10 and valor >= 1:
#                 lista.append(valor)
#             else:
#                 print('El valor introducido no se encuentra entre 1 y 10. Inténtelo de nuevo')
#             aux -= 1
#         print(f'La lista introducida es: {lista}\n')
#
#     elif respuesta == 6:
#         lista = []
#         lista_creciente = []
#         aux = 15
#         print('Introduzca los valores')
#         while aux > 0:
#             valor = input()
#             valor = int(valor)
#             lista.append(valor)
#             aux -= 1
#         print(f'La lista introducida es: {lista}')
#         lista.sort()
#         print(print(f'La lista ordenada es: {lista}\n'))
#
#     elif respuesta == 7:
#         lista = []
#         aux = 15
#         print('Introduzca los valores')
#         while aux > 0:
#             valor = input()
#             valor = int(valor)
#             if valor in lista:
#                 print('Ese valor ya ha sido introducido, introduzca otro diferente')
#             else:
#                 lista.append(valor)
#                 aux -= 1
#         print(f'La lista es: {lista}\n')
#
#     elif respuesta == 0:
#         salir = True
#
#     else:
#         print('Número incorrecto')
#########################################################################################################
#Ejercicio 8
#Crea un programa que almacene en una lista la nota de los alumnos de un grupo de SGE, y posteriormente calcule y
#visualice el número de notas que aparecen dentro de los siguientes intervalos:
# [0 , 5) Insuficiente
# [5 , 6) Aprobado
# [6, 7) Bien
# [7 , 9) Notable
# [9 , 10] Sobresaliente
# import random
#
# lista = []
# contador = 15
#
# while contador > 0:
#     lista.append(random.randint(1, 10))
#     contador -= 1
# print(f'Las notas son: {lista}')
# for i in lista:
#     if i in range(0, 5):
#         print(f'{i} --> Insuficiente')
#     elif i in range(5, 6):
#         print(f'{i} --> Aprobado')
#     elif i in range (6, 7):
#         print(f'{i} --> Bien')
#     elif i in range (7, 9):
#         print(f'{i} --> Notable')
#     elif i in range (9, 11):
#         print(f'{i} --> Sobresaliente')
#     else:
#         print('Número fuera de rango')

#########################################################################################################
#Ejercicio 9
#Crea un programa que dado una lista de 50 elementos enteros, lo descomponga en dos, una formado por
#los valores pares y otra formado por los valores impares. En las dos listas resultantes los valores
#se incluirán los números consecutivamente, uno detrás del otro, sin huecos.
# import random
# lista = []
# contador = 50
# lista_pares = []
# lista_impares = []
# while contador > 0:
#     lista.append(random.randint(1, 100))
#     contador -= 1
# for i in lista:
#     if i%2 == 0:
#         lista_pares.append(i)
#     else:
#         lista_impares.append(i)
#
# print(f'La lista original es: {lista}')
# print(f'La lista de impares es: {lista_impares}')
# print(f'La lista de números{lista_pares}')

#########################################################################################################
#Ejercicio 10
#Crea un programa en el que el usuario introduzca una frase y el programa calcule el número de palabras de dicha frase.
#Pista grande: para contar palabras podemos contar las veces que pasamos de un carácter que no es del alfabeto a uno
#que sí lo es. Para saber si un carácter es una letra, en Python tenemos la función string.isalpha().
contador = 0
print('Introduce una frase')
frase = input()
frase = str(frase)
for i in frase:
    if i == frase.isalpha():
        contador += 1
print(contador)


