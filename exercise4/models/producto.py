
class Producto:
    def __init__(self, codigo, nombre, precio, existencias):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.existencias = existencias
    
    def actualizar_existencias(self, cantidad):
        if self.existencias + cantidad < 0:
            raise ValueError("No se puede tener existencias negativas")
        self.existencias += cantidad
    
    def actualizar_precio(self, nuevo_precio):
        if nuevo_precio <= 0:
            raise ValueError("El precio debe ser positivo")
        self.precio = nuevo_precio
    
    def __str__(self):
        return f"{self.codigo} - {self.nombre} (${self.precio:.2f}) | Existencias: {self.existencias}"