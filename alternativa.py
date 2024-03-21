class Alternativa:
    def __init__(self, contenido, ayuda=None):
        # Constructor de la clase Alternativa
        self.contenido = contenido  # Define el contenido de la alternativa
        self.ayuda = ayuda  # Define la ayuda asociada, opcional

    def mostrar_alternativa(self):
        # Método para mostrar la información de la alternativa
        print("Contenido:", self.contenido)
        if self.ayuda:
            print("Ayuda:", self.ayuda)