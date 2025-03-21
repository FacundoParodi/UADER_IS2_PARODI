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
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 



if len(sys.argv) < 2:
    num = input("Debe proporcionar un número para calcular su factorial: ")
    while not num.isdigit():
        num = input("Entrada no válida. Ingrese un número entero: ")
    num = int(num)
else:
    num = int(sys.argv[1])


print("el valor del factorial de",num, "es",factorial(num))
    
   
    



