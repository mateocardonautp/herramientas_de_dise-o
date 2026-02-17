
//No corregido
class Ave:
    def volar(self):
        pass

class Pinguino(Ave):
    def volar(self):
        raise Exception("Los pingüinos no vuelan")

//corregido

class Ave:
    pass

class AveVoladora(Ave):
    def volar(self):
        pass

class Pinguino(Ave):
    pass
