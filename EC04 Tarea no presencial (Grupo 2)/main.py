#Lee por teclado palabras y guárdalas en una lista, el proceso finaliza cuando metamos la palabra FIN.
#Muestra las palabras en orden alfabético, y posteriormente en orden de menos a más caracteres de longitud.
lista = []
salida = False
def por_len(i):
    return len(i)
print('Introduzca tantas palabras como quiera. Para terminar escriba "FIN"')
while salida != True:
    a = input()
    a = str(a)
    if a == 'FIN':
        salida = True
    else:
        lista.append(a)
print('Lista de palabras introducidas:')
print(lista)
lista.sort(key=lambda lista: lista[0])
print('Lista por orden alfabético')
print(lista)
print('Lista ordenada de menos a más caractéres de longitud')
print(lista.sort(key=por_len))
