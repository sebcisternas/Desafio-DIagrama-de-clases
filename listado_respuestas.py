class ListadoRespuestas:
     # constructor de la clase ListadoRespuestas
    def __init__(self, encuesta, usuario):
       
        self.__encuesta = encuesta  
        self.__usuario = usuario  
        self.__respuestas = []  

    @property
    def encuesta(self):
        # getter para la encuesta asociada
        return self.__encuesta

    @property
    def usuario(self):
        # getter para el usuario asociado
        return self.__usuario

    @property
    def respuestas(self):
        # getter para la lista de respuestas
        return self.__respuestas

    def agregar_respuesta(self, respuesta):
        # metodo para agregar una respuesta a la lista
        self.__respuestas.append(respuesta)