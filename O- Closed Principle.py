#No corregido

class Descuento:
    def calcular(self, tipo, precio):
        if tipo == "regular":
            return precio * 0.1
        elif tipo == "vip":
            return precio * 0.2
        elif tipo == "empleado":
            return precio * 0.3
#Corregido

class Descuento:
    def calcular(self, precio):
        raise NotImplementedError


class DescuentoRegular(Descuento):
    def calcular(self, precio):
        return precio * 0.1


class DescuentoVIP(Descuento):
    def calcular(self, precio):
        return precio * 0.2


class DescuentoEmpleado(Descuento):
    def calcular(self, precio):
        return precio * 0.3
