class Pregunta:
   
    # constructor de la clase Pregunta
    def __init__(self, enunciado: str, requerida: bool, ayuda: str =None, alternativas=None):
        self.enunciado = enunciado
        self.requerida = requerida
        self.ayuda = ayuda
        
        if alternativas is None:
            alternativas = []
        self.alternativas = alternativas

    def agregar_alternativa(self, alternativa):
        # metodo para agregar una alternativa a la pregunta
        self.alternativas.append(alternativa)

 # metodo para mostrar la información de la pregunta
    def mostrar_pregunta(self):
        print("Enunciado:", self.enunciado)
        if self.ayuda:
            print("Ayuda:", self.ayuda)
        print("Requerida:", self.requerida)
        for i, alternativa in enumerate(self.alternativas, start=1):
            print(f"Alternativa {i}:")
            alternativa.mostrar_alternativa() # muestra cada alternativa