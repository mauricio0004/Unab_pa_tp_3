class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre

class Libro:
    def __init__(self):
        # Inicializamos los atributos vacíos
        self.titulo = ""
        self.autor = None  # Aquí guardaremos un objeto de la clase Persona
        self.isbn = ""
        self.paginas = 0
        self.edicion = ""
        self.editorial = ""
        self.ciudad = ""
        self.pais = ""
        self.fecha_edicion = ""

    # Métodos para leer la información (Setters implícitos)
    def leer_informacion(self):
        print("--- Ingrese los datos del libro ---")
        self.titulo = input("Título: ")
        
        nombre_autor = input("Autor: ")
        self.autor = Persona(nombre_autor) # Uso de la clase Persona
        
        self.isbn = input("ISBN: ")
        self.edicion = input("Edición (ej. 3a): ")
        self.editorial = input("Editorial: ")
        self.ciudad = input("Ciudad: ")
        self.pais = input("País: ")
        self.fecha_edicion = input("Fecha de edición (texto): ")
        self.paginas = int(input("Número de páginas: "))

    # Método para mostrar la información con el formato solicitado
    def mostrar_informacion(self):
        print("\n" + "="*30)
        print(f"Título: {self.titulo} {self.edicion}. edición")
        print(f"Autor: {self.autor}")
        print(f"ISBN: {self.isbn}")
        print(f"Prentice-Hall, {self.ciudad} ({self.pais})")
        print(f"{self.fecha_edicion}")
        print(f"{self.paginas} páginas")
        print("="*30)
