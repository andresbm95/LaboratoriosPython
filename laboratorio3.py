#!/usr/bin/python3

""" Autor : Mario Benavides Masis
Carnet B81068
El programa es para hacer
recursivamente
una función de fibonacci

:int se recibe un entero para calcular el fibonacci
"""
import time
import argparse
timeinit = time.time()

def fun_fibo(numero):
    if  numero < 2:
        #compara el numero ingresado (0 y 1 para dar un 1 )
        solucion = 1
    else:
        #si es mayor igual a 2 se calcula recursivamente
        solucion = (fun_fibo(numero - 1) + fun_fibo(numero - 2))
    return solucion #retorna la solucion de la funcion
def comp_fibo(n):
    for x in range(n):
        print(fun_fibo(x))



# ArgumentParser
parser = argparse.ArgumentParser()

parser.add_argument(
    'numero',
    help='Posicion en la secuencia de Fibonacci que debe ser calculado.'
)
parser.add_argument(
    '--tiempo',
    '-t',
    action="store_true",
    help='Imprime el tiempo transcurrido para finalizar el cálculo.'
)
parser.add_argument(
    '--completa',
    '-c',
    action="store_true",
    help='Imprime la secuencia completa.'
)
args = parser.parse_args()

#if  args.numero:
#    x = fun_fibo(args.numero)
#    print(x)
#if args.numero and args.tiempo:
#    print(fun_fibo(args.numero))
    #print(timeinit-timefin)
    #    timefin = time.time()
#if args.numero and args.tiempo and args.completa:
#    print(fun_fibo(args.numero))
#    timefin = time.time()
#    print(timeinit-timefin)
var = args.numero
print(comp_fibo(var))
