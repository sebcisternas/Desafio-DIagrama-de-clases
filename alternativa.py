class Alternativa:
    def __init__(self, contenido, ayuda=None):
        self.contenido = contenido
        self.ayuda = ayuda

    def mostrar_alternativa(self):
        print("Contenido:", self.contenido)
        if self.ayuda:
            print("Ayuda:", self.ayuda)
            
            
alternativa = Alternativa("Opción A", "Esta es la primera opción")
alternativa.mostrar_alternativa()