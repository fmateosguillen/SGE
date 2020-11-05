# cadena = input('Introduzca una frase:')
# lista = cadena.split()
# dict1 = {}
# for palabra in lista:
#     if palabra in dict1:
#         dict1[palabra]+=1
#     else:
#         dict1[palabra]=1
#
# for campo, valor in dict1.items():
#     print(f'{campo} --> {valor}')

########################################################################################################################
#
# cadena = input('Introduce una palabra para pasarla a MORSE:')
# codigo_morse = {
#     'A': '.-',     'B': '-...',    'C': '-.-.',
#     'D': '-..',    'E': '.',       'F': '..-.',
#     'G': '--.',    'H': '....',    'I': '..',
#     'J': '.---',   'K': '-.-',     'L': '.-..',
#     'M': '--',     'N': '-.',      'O': '---',
#     'P': '.--.',   'Q': '--.-',    'R': '.-.',
#     'S': '...',    'T': '-',       'U': '..-',
#     'V': '...-',   'W': '.--',     'X': '-..-',
#     'Y': '-.--',   'Z': '--..',    '1': '.----',
#     '2': '..---',  '3': '...--',   '4': '....-',
#     '5': '.....',  '6': '-....',   '7': '--...',
#     '8': '---..',  '9': '----.',   '0': '-----',
#     '.': '.-.-.-', ',': '--..--',  ':': '---...',
#     ';': '-.-.-.', '?': '..--..',  '!': '-.-.--',
#     '"': '.-..-.', "'": '.----.',  '+': '.-.-.',
#     '-': '-....-', '/': '-..-.',   '=': '-...-',
#     '_': '..--.-', '$': '...-..-', '@': '.--.-.',
#     '&': '.-...',  '(': '-.--.',   ')': '-.--.-'
# }
# lista = []
# for caracter in cadena:
#     if caracter.islower():
#         caracter = caracter.upper()
#     elif caracter == ' ':
#         caracter = '.'
#     lista.append(codigo_morse[caracter])
# print(" ".join(lista))

########################################################################################################################
#
# codigo_morse = {
#     'A': '.-',     'B': '-...',    'C': '-.-.',
#     'D': '-..',    'E': '.',       'F': '..-.',
#     'G': '--.',    'H': '....',    'I': '..',
#     'J': '.---',   'K': '-.-',     'L': '.-..',
#     'M': '--',     'N': '-.',      'O': '---',
#     'P': '.--.',   'Q': '--.-',    'R': '.-.',
#     'S': '...',    'T': '-',       'U': '..-',
#     'V': '...-',   'W': '.--',     'X': '-..-',
#     'Y': '-.--',   'Z': '--..',    '1': '.----',
#     '2': '..---',  '3': '...--',   '4': '....-',
#     '5': '.....',  '6': '-....',   '7': '--...',
#     '8': '---..',  '9': '----.',   '0': '-----',
#     '.': '.-.-.-', ',': '--..--',  ':': '---...',
#     ';': '-.-.-.', '?': '..--..',  '!': '-.-.--',
#     '"': '.-..-.', "'": '.----.',  '+': '.-.-.',
#     '-': '-....-', '/': '-..-.',   '=': '-...-',
#     '_': '..--.-', '$': '...-..-', '@': '.--.-.',
#     '&': '.-...',  '(': '-.--.',   ')': '-.--.-'
# }
# cadena = input('Introduce un código MORSE para convertirlo en una palabra: ')
# lista = cadena.split(' ')
# palabra = ''
# for cod in lista:
#     for key, valor in codigo_morse.items():
#         if valor == cod:
#             letra = key
#     palabra+=letra
# print(palabra)
########################################################################################################################
#
# gustos = {}
# nombre = input('Indique el nombre de una persona: ')
# while nombre!='.':
#     gusto = input('Indique uno de sus gutos: ')
#     lista_gustos = gustos.setdefault(nombre,[gusto])
#     if lista_gustos != [gusto]:
#         gustos[nombre].append(gusto)
#     nombre = input('Indique el nombre de una persona: ')
# print(gustos)

########################################################################################################################
#Codifica un programa en python que nos permita guardar los nombres de los alumnos de una clase y las notas que han
#obtenido. Cada alumno puede tener distinta cantidad de notas. Guarda la información en un diccionario cuya claves
#serán los nombres de los alumnos y los valores serán listas con las notas de cada alumno.
#El programa no debe pedir el número de alumnos que vamos a introducir (hay que pensar en un mecanismo para poder
#indicar que queremos agregar uno  nuevo, o un mecanismo de parada); pedirá el nombre de un alumno e irá pidiendo sus
#notas hasta que introduzcamos un número negativo. Al final el programa nos mostrará la lista de alumnos y la nota media
#obtenida por cada uno de ellos. Nota: si se introduce el nombre de un alumno que ya existe el programa nos dará un error.
# alumnos = {}
# nombre = ''
# while nombre != '.':
#     nota = 1
#     nombre = input('Indique el nombre del alumno (Para terminar introduzca "."): ')
#     if nombre in alumnos.keys():
#         print('Ese alumno ya ha sido introducido, por favor introduzca otro')
#     elif nombre == '.':
#         for nombre, notas in alumnos.items():
#             suma = 0
#             for nota in notas :
#                 suma += nota
#                 media = suma/len(notas)
#             print(f'Alumno: {nombre} --> Nota Media: {media}')
#         nombre = '.'
#     else:
#         print('Indique sus notas para calcular la media (Para terminar introduzca un número negativo): ')
#         while nota > 0:
#             nota = input()
#             nota = int(nota)
#             if nota > 0:
#                 lista_notas = alumnos.setdefault(nombre,[nota])
#                 if lista_notas != [nota]:
#                     alumnos[nombre].append(nota)
