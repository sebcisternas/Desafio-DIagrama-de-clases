class ListadoRespuestas:
    def __init__(self, encuesta, usuario):
        self._encuesta = encuesta
        self._usuario = usuario
        self._respuestas = []

    @property
    def encuesta(self):
        return self._encuesta

    @property
    def usuario(self):
        return self._usuario

    @property
    def respuestas(self):
        return self._respuestas

    def agregar_respuesta(self, respuesta):
        self._respuestas.append(respuesta)