#No corregido

class Reporte:
    def __init__(self, contenido):
        self.contenido = contenido

    def generar(self):
        return f"Reporte: {self.contenido}"

    def guardar_archivo(self, nombre_archivo):
        with open(nombre_archivo, "w") as archivo:
            archivo.write(self.generar())

#Corregido

class Reporte:
    def __init__(self, contenido):
        self.contenido = contenido

    def generar(self):
        return f"Reporte: {self.contenido}"


class ReporteArchivo:
    def guardar(self, reporte: Reporte, nombre_archivo):
        with open(nombre_archivo, "w") as archivo:
            archivo.write(reporte.generar())
