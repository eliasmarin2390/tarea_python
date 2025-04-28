
class Factura:
    def __init__(self, nombre_producto, cantidad, precio, descuento):
        self.nombre_producto = nombre_producto
        self.cantidad = cantidad
        self.precio = precio
        self.descuento = descuento
    
    def calcular_total(self):
        if self.validaciones():
            raise ValueError("Datos inválidos")
        else:
            return self.precio * self.cantidad * (1 - self.descuento)
    
    def generar_reporte(self):
        return (
        f"Producto: {self.nombre_producto}\n"
        f"Cantidad: {self.cantidad}\n"
        f"Precio: {self.precio:.2f}\n"
        f"Descuento: {self.descuento * 100:.2f}%\n"
        f"Total: {self.calcular_total():.2f}\n" )

    def validaciones(self):
        if not isinstance(self.nombre_producto, str):
            return "Error: El nombre del producto debe ser una cadena de texto."
        if not isinstance(self.cantidad, int):
            return "Error: La cantidad debe ser un número entero."
        if not isinstance(self.precio, float):
            return "Error: El precio debe ser un número decimal."
        if not isinstance(self.descuento, float):
            return "Error: El descuento debe ser un número decimal."