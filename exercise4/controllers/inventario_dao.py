
import models.inventario as inv_model
import models.producto as prod_model

class InventarioDAO:
    def __init__(self):
        self.inventario = inv_model.Inventario()
    
    def registrar_producto(self, datos_producto):
        producto = prod_model.Producto(**datos_producto)
        self.inventario.agregar_producto(producto)
        return producto
    
    def buscar_producto(self, codigo):
        return self.inventario.buscar_producto(codigo)
    
    def actualizar_existencias(self, codigo, cantidad):
        producto = self.inventario.buscar_producto(codigo)
        if producto:
            producto.actualizar_existencias(cantidad)
    
    def eliminar_producto(self, codigo):
        self.inventario.eliminar_producto(codigo)
    
    def obtener_todos_los_productos(self):
        return self.inventario.listar_productos()