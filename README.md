# Unab_pa_tp_3
Tarea de programacion 

Ejercicio numero 2

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
