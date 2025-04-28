
class Inventario:
    def __init__(self):
        self.productos = {}
    
    def agregar_producto(self, producto):
        if producto.codigo in self.productos:
            raise ValueError("El código de producto ya existe")
        self.productos[producto.codigo] = producto
    
    def buscar_producto(self, codigo):
        return self.productos.get(codigo)
    
    def eliminar_producto(self, codigo):
        if codigo not in self.productos:
            raise ValueError("Producto no encontrado")
        del self.productos[codigo]
    
    def listar_productos(self):
        return list(self.productos.values())