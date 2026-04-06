class Punto:
    def __init__(self, x, y):
        """Constructor que inicializa las coordenadas x e y."""
        self.x = x
        self.y = y

    def eje_x(self):
        """Devuelve el valor de la coordenada x."""
        return self.x

    def eje_y(self):
        """Devuelve el valor de la coordenada y."""
        return self.y

    def impresion(self):
        """Devuelve una representación en string del punto."""
        return f"Punto({self.x}, {self.y})"

    def opuesto(self):
        """Devuelve un nuevo objeto Punto con los atributos negativos."""
        return Punto(-self.x, -self.y)

    # --- Método adicional que considero importante ---
    def distancia_al_origen(self):
        """Calcula la distancia euclidiana desde (0,0)."""
        import math
        return math.sqrt(self.x**2 + self.y**2)
