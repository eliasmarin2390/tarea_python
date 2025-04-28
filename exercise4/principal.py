          
import controllers.inventario_dao as dao
import os

# Limpiar consola y establecer colores
os.system('cls' if os.name == 'nt' else 'clear')

def main():
    # Inicializar DAO
    inventario_dao = dao.InventarioDAO()  # Cambiado de InventoryDAO a InventarioDAO
    
    print("-" * 30)
    print("Sistema de gestión de inventario")
    print("-" * 30)
    
    # Registrar productos
    while True:
        print("\nIngrese los datos del producto:")
        codigo = input("Código: ")
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        existencias = int(input("Stock: "))
        
        datos_producto = {"codigo": codigo, "nombre": nombre, "precio": precio, "existencias": existencias}
        inventario_dao.registrar_producto(datos_producto)  # Cambiado de register_product a registrar_producto
        
        otro = input("¿Desea agregar otro producto? (s/n): ").strip().lower()
        if otro != 's':
            break
    
    # Mostrar inventario
    print("-" * 30)
    print("\nProductos registrados:")
    print("-" * 30)
    for producto in inventario_dao.obtener_todos_los_productos():  # Cambiado de get_all_products a obtener_todos_los_productos
        print(f"- {producto}")
    
    # Ejemplo de búsqueda
    print("-" * 30)
    print("\nBuscar el producto:")
    print("-" * 30)
    codigo_busqueda = input("Ingrese el código del producto a buscar: ")
    encontrado = inventario_dao.buscar_producto(codigo_busqueda)  # Cambiado de search_product a buscar_producto
    print(f"Resultado: {encontrado}")

if __name__ == "__main__":
    main()