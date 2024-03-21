from listado_respuestas import ListadoRespuestas

class Encuesta():
    # constructor de la clase Encuesta
    def __init__(self, nombre):
        self.nombre = nombre
        self.preguntas = [] # inicializa la lista de preguntas
        self.listados_respuestas = [] # inicializa la lista de listados de respuestas

    def agregar_pregunta(self, pregunta):
        # metodo para agregar una pregunta a la encuesta
        self.preguntas.append(pregunta)

    def agregar_listado_respuestas(self, listado_respuestas):
        # metodo para agregar un listado de respuestas a la encuesta
        self.listados_respuestas.append(listado_respuestas)

    def mostrar_encuesta(self):
        # metodo para mostrar la información de la encuesta
        print("Nombre de la encuesta:", self.nombre)
        print("Preguntas:")
        for pregunta in self.preguntas:
            pregunta.mostrar_pregunta()
        print("Listados de respuestas:", self.listados_respuestas)
        
    def responder_encuesta(self, usuario):
        # metodo para que un usuario responda la encuesta
        listado_respuestas = ListadoRespuestas(usuario)
        self.listados_respuestas.append(listado_respuestas)
        return listado_respuestas


class EncuestaLimitadaPorEdad(Encuesta):
    # constructor de la clase EncuestaLimitadaPorEdad
    def __init__(self, nombre, edad_minima, edad_maxima):
        super().__init__(nombre)
        self.edad_minima = edad_minima
        self.edad_maxima = edad_maxima
        
    def agregar_listado_respuestas(self, listado_respuestas, usuario):
        # metodo para agregar un listado de respuestas a la encuesta limitada por edad
        if self.edad_minima <= usuario.edad <= self.edad_maxima:
            self.listados_respuestas.append(listado_respuestas)
        else:   
            print("El usuario no cumple con los criterios de región de esta encuesta.")


class EncuestaLimitadaPorRegion(Encuesta):
    # constructor de la clase EncuestaLimitadaPorRegion
    def __init__(self, nombre, regiones):
        super().__init__(nombre)
        self.regiones = regiones
    
    # metodo para agregar un listado de respuestas a la encuesta limitada por región
    def agregar_listado_respuestas(self, listado_respuestas, usuario):
        
        if usuario.region in self.regiones:
            self.listados_respuestas.append(listado_respuestas)
        else:
            print("El usuario no cumple con los criterios de región de esta encuesta.")    