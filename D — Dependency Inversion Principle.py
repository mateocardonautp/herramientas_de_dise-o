#No corregido

class EmailNotificador:
    def enviar(self, mensaje):
        print(f"Enviando email: {mensaje}")


class UsuarioService:
    def __init__(self):
        self.notificador = EmailNotificador()

    def registrar_usuario(self, nombre):
        print(f"Registrando usuario {nombre}")
        self.notificador.enviar("Usuario registrado")

#Corregido

class Notificador:
    def enviar(self, mensaje):
        raise NotImplementedError


class EmailNotificador(Notificador):
    def enviar(self, mensaje):
        print(f"Enviando email: {mensaje}")


class UsuarioService:
    def __init__(self, notificador: Notificador):
        self.notificador = notificador

    def registrar_usuario(self, nombre):
        print(f"Registrando usuario {nombre}")
        self.notificador.enviar("Usuario registrado")
