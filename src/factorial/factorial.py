#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*


import sys

def factorial(num): 
    if num < 0:
        print("Factorial de un numero negativo no existe")
        return 0
    elif num == 0:
        return 1
    else:
        fact = 1
        while(num > 1):
            fact *= num
            num -= 1
        return fact 

def calcular_factoriales_en_rango(desde, hasta):
    factoriales = {}
    for i in range(desde, hasta + 1):
        factoriales[i] = factorial(i)
    return factoriales

if len(sys.argv) < 2:
    num = input("Debe proporcionar un numero para calcular su factorial: ")
    while not num.replace("-", "").isdigit():
        num = input("Entrada no valida, ingrese un numero entero: ")
    num = num.strip()
    if '-' in num:
        if num.startswith('-'):
            num = num[1:]
            for i in range(1, int(num)+1):
                print(f"Factorial de {i}: {factorial(i)}")
        else:
            limites = num.split("-")
            desde = int(limites[0])
            hasta = int(limites[1])
            print(calcular_factoriales_en_rango(desde, hasta))
    else:
        num = int(num)
        print(f"el valor del factorial de {num} es {factorial(num)}")
else:
    num = int(sys.argv[1])
    print(f"el valor del factorial de {num} es {factorial(num)}")



# Comentario de prueba
