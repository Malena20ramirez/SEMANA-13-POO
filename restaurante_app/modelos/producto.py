class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    @staticmethod
    def validar_texto(valor, campo):
        if not valor or not str(valor).strip():
            raise ValueError(f"El campo {campo} no puede estar vacio.")
        return str(valor).strip()

    @staticmethod
    def validar_positivo(valor, campo, tipo=float):
        try:
            val = tipo(valor)
            if val < 0:
                raise ValueError(f"El campo {campo} no puede ser negativo.")
            return val
        except (ValueError, TypeError):
            raise ValueError(f"El campo {campo} debe ser un valor numérico válido.")


    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        self._codigo = self.validar_texto(valor, "codigo")

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = self.validar_texto(valor, "nombre")

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        self._precio = self.validar_positivo(valor, "precio", float)

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, valor):
        self._stock = self.validar_positivo(valor, "stock", tipo=int)
