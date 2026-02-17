#No corregido

class Trabajador:
    def trabajar(self):
        raise NotImplementedError

    def comer(self):
        raise NotImplementedError


class Robot(Trabajador):
    def trabajar(self):
        pass

    def comer(self):
        raise Exception("Unsupported operation")
#Corregido

class Trabajador:
    def trabajar(self):
        raise NotImplementedError


class SerHumano:
    def comer(self):
        raise NotImplementedError


class Robot(Trabajador):
    def trabajar(self):
        pass

