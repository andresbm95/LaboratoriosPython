#!/usr/bin/python3

print("carnet B81068")
iterador = int(input('ingrese altura de la piramide = '))
caracter = str(input('ingrese un caracter para hacer la piramide: '))
for k in range(iterador):
    print((" "+caracter+" ")*iterador)
    iterador-=1
