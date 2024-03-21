from listado_respuestas import ListadoRespuestas

class Usuario:
    # constructor de la clase Usuario
    def __init__(self, correo: str, edad: int, region: int):
        self.__correo = correo
        self.__edad = edad
        self.__region = region
        self.__listado_respuestas = ListadoRespuestas()

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, nuevo_correo):
        self._correo = nuevo_correo

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        self._edad = nueva_edad

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, nueva_region):
        self._region = nueva_region

    @property
    def listado_respuestas(self):
        return self.__listado_respuestas

    def contestar_encuesta(self, encuesta):
        pass