
class Factorial:
    def __init__(self, num=None):
        self.num = num

    def factorial(self, num):
        if num < 0:
            print(f"Factorial de un numero negativo no existe para {num}")
            return 0
        elif num == 0:
            return 1
        else:
            fact = 1
            while num > 1:
                fact *= num
                num -= 1
            return fact

    def run(self, min, max):
        factoriales = {}
        for i in range(min, max + 1):
            factoriales[i] = self.factorial(i)
        return factoriales


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        num = input("Debe dar un numero para calcular su factorial: ")
        while not num.replace("-", "").isdigit():
            num = input("Ingrese un numero entero: ")
        num = num.strip()
        factorial_calculador = Factorial()

        if '-' in num:
            if num.startswith('-'):
                num = num[1:]
                for i in range(1, int(num)+1):
                    print(f"Factorial de {i}: {factorial_calculador.factorial(i)}")
            else:
                limites = num.split("-")
                desde = int(limites[0])
                hasta = int(limites[1])
                print(factorial_calculador.run(desde, hasta))
        else:
            num = int(num)
            print(f"el valor del factorial de {num} es {factorial_calculador.factorial(num)}")
    else:
        num = sys.argv[1]
        factorial_calculador = Factorial()
        if '-' in num:
            if num.startswith('-'):
                num = num[1:]
                for i in range(1, int(num)+1):
                    print(f"Factorial de {i}: {factorial_calculador.factorial(i)}")
            else:
                limites = num.split("-")
                desde = int(limites[0])
                hasta = int(limites[1])
                print(factorial_calculador.run(desde, hasta))
        else:
            num = int(num)
            print(f"el valor del factorial de {num} es {factorial_calculador.factorial(num)}")
