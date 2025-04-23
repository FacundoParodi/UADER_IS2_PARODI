class TaxCalculator:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TaxCalculator, cls).__new__(cls)
        return cls._instance

    def calcular_impuestos(self, base_imponible):
        if base_imponible < 0:
            raise ValueError("La base imponible debe ser un valor positivo.")
        
        iva = base_imponible * 0.21  # 21%
        iibb = base_imponible * 0.05  # 5%
        contribuciones = base_imponible * 0.012  # 1.2%
        total_impuestos = iva + iibb + contribuciones

        return total_impuestos