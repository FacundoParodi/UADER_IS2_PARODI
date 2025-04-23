class FactorialCalculator:
    _instance = None  # Variable de clase para almacenar la única instancia

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FactorialCalculator, cls).__new__(cls)
        return cls._instance

    def factorial(self, n):
        if n < 0:
            raise ValueError("El numero no debe negativo")
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


if __name__ == "__main__":
    # Se prueban dos instancias para verificar que es Singleton
    calc1 = FactorialCalculator()
    calc2 = FactorialCalculator()

    # Prueba del metodo factorial
    numero = 5
    print(f"{numero}! = {calc1.factorial(numero)}")

    # Verificacion de Singleton (debe imprimir True)
    print("Es la misma instancia?", calc1 is calc2)