# Unab_pa_tp_3
Tarea de programacion 
integrantes: Mauri,Axel y Santi

EJERCICIO NUMERO 2

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # valor del eje X
    def eje_x(self):
        return self.x

    # valor del eje Y
    def eje_y(self):
        return self.y

    # Devolvemos el punto 
    def impresion(self):
        return f"({self.x}, {self.y})"

    # Devuelve el punto opuesto
    def opuesto(self):
        return Punto(-self.x, -self.y)

    # Método extra: distancia al origen
    def distancia_origen(self):
        return (self.x**2 + self.y**2) ** 0.5


## probamos el codigo para ver si anda
p1 = Punto(2, 3)

print("Eje X:", p1.eje_x())
print("Eje Y:", p1.eje_y())
print("Punto:", p1.impresion())

p2 = p1.opuesto()
print("Punto opuesto:", p2.impresion())

print("Distancia al origen:", p1.distancia_origen())


EJERCICIO NUMERO 3
class Linea:
    def __init__(self, punto_a, punto_b):
        """
        Constructor que recibe dos objetos de la clase Punto.
        """
        self._punto_a = punto_a
        self._punto_b = punto_b

    def mueve_derecha(self, distancia):
        """Desplaza la línea a la derecha sumando a la coordenada x de ambos puntos."""
        self._punto_a.x += distancia
        self._punto_b.x += distancia

    def mueve_izquierda(self, distancia):
        """Desplaza la línea a la izquierda restando a la coordenada x de ambos puntos."""
        self._punto_a.x -= distancia
        self._punto_b.x -= distancia

    def mueve_arriba(self, distancia):
        """Desplaza la línea hacia arriba sumando a la coordenada y de ambos puntos."""
        self._punto_a.y += distancia
        self._punto_b.y += distancia

    def mueve_abajo(self, distancia):
        """Desplaza la línea hacia abajo restando a la coordenada y de ambos puntos."""
        self._punto_a.y -= distancia
        self._punto_b.y -= distancia

    def mostrar(self):
        """Método auxiliar para ver dónde quedó la línea."""
        return f"Línea de {self._punto_a.impresion()} a {self._punto_b.impresion()}"


EJERCICIO NUMERO 4

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

EJRCICIO NUMERO 5


class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"


class Libro:
    def __init__(self, titulo, autor, isbn, paginas, edicion, editorial, ciudad, pais, fecha):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.paginas = paginas
        self.edicion = edicion
        self.editorial = editorial
        self.ciudad = ciudad
        self.pais = pais
        self.fecha = fecha

    # Getters
    def get_titulo(self):
        return self.titulo

    def get_autor(self):
        return self.autor

    def get_isbn(self):
        return self.isbn

    def get_paginas(self):
        return self.paginas

    # Setters
    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_paginas(self, paginas):
        self.paginas = paginas

    # Método para mostrar la información
    def mostrar_info(self):
        print(f"Título: {self.titulo} {self.edicion} edición")
        print(f"Autor: {self.autor}")
        print(f"ISBN: {self.isbn}")
        print(f"{self.editorial}, {self.ciudad} ({self.pais})")
        print(self.fecha)
        print(f"{self.paginas} páginas")


# ===== PRUEBA =====
autor = Persona("Y. Daniel", "Liang")

libro = Libro(
    "Introduction to Java Programming",
    autor,
    "0-13-031997-X",
    784,
    "3a.",
    "Prentice-Hall",
    "New Jersey",
    "USA",
    "viernes 16 de noviembre de 2001"
)

libro.mostrar_info()




