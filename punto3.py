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
