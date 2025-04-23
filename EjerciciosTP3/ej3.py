class MetodoEntrega:
    def entregar(self):
        pass

class EntregaMostrador(MetodoEntrega):
    def entregar(self):
        print("La hamburguesa se entrega por mostrador")

class RetiroCliente(MetodoEntrega):
    def entregar(self):
        print("El cliente retira la hamburguesa personalmente.")

class Delivery(MetodoEntrega):
    def entregar(self):
        print("La hamburguesa se envia por delivery.")


# Clase principal
class Hamburguesa:
    def __init__(self, metodo_entrega: MetodoEntrega):
        self.metodo_entrega = metodo_entrega

    def entregar(self):
        self.metodo_entrega.entregar()

    def cambiar_metodo(self, nuevo_metodo: MetodoEntrega):
        self.metodo_entrega = nuevo_metodo