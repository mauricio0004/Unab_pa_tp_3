EJERCICIO NUMERO_4

class Cancion:
    
    def __init__(self, titulo , autor):
        self.titulo = titulo
        self.autor = autor

    def get_titulo(self):
        return self.titulo
    
    def get_autor(self):
        return self.autor
    
    def set_titulo(self, nuevotitulo):
        self.titulo = nuevotitulo

    def set_autor(self,nuevoautor):
        self.autor = nuevoautor


