#!/usr/bin/python3

""" Autor : Mario Benavides Masis
Carnet B81068
El programa es para hacer
recursivamente
una función de fibonacci
"""

def fun_fibo(numero):
    if (numero < 2):
        solucion = 1
    else:
        solucion = (fun_fibo(numero - 1) + fun_fibo(numero - 2))
    return solucion
num1= int(input("digite indice fibonacci: "))
print(fun_fibo(num1))
