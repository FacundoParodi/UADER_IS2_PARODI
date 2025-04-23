class CondicionImpositiva:
    def generar_factura(self, importe):
        pass


class IVAResponsable(CondicionImpositiva):
    def generar_factura(self, importe):
        print(f"Factura A - IVA Responsable. Importe total: ${importe:.2f}")

class IVANoInscripto(CondicionImpositiva):
    def generar_factura(self, importe):
        print(f"Factura C - IVA No Inscripto. Importe total: ${importe:.2f}")

class IVAExento(CondicionImpositiva):
    def generar_factura(self, importe):
        print(f"Factura E - IVA Exento. Importe total: ${importe:.2f}")


class Factura:
    def __init__(self, importe, condicion: CondicionImpositiva):
        self.importe = importe
        self.condicion = condicion

    def imprimir(self):
        self.condicion.generar_factura(self.importe)