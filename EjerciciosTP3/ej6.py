import copy

class Prototipo:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def clonar(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Prototipo(nombre={self.nombre}, tipo={self.tipo})"

# Crear instancia base
original = Prototipo("Avión A", "Comercial")
print("Original:", original)

# Clonar la instancia original
copia1 = original.clonar()
print("Copia 1:", copia1)

# Clonar la copia (esto verifica que tambien puede clonarse)
copia2 = copia1.clonar()
print("Copia 2:", copia2)