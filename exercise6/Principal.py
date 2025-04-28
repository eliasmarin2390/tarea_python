
import models.Factura as mi

def solicitar_datos():
    while True:
        try:
            descripcion = input("Ingrese la descripción del producto: ").strip()
            if not descripcion:
                raise ValueError("La descripción no puede estar vacía.")
            
            cantidad = int(input("Ingrese la cantidad: ").strip())
            if cantidad <= 0:
                raise ValueError("La cantidad debe ser un número entero positivo.")
            
            precio_unitario = float(input("Ingrese el precio unitario: ").strip())
            if precio_unitario <= 0:
                raise ValueError("El precio unitario debe ser un número decimal positivo.")
            
            impuesto = float(input("Ingrese el impuesto (0-1): ").strip())
            if not (0 <= impuesto <= 1):
                raise ValueError("El impuesto debe ser un número decimal entre 0 y 1.")
            
            return descripcion, cantidad, precio_unitario, impuesto
        except ValueError as e:
            print(f"Error: {e}. Por favor, intente de nuevo.")
        except Exception as e:
            print(f"Error inesperado: {e}. Por favor, intente de nuevo.")

def menu():
    while True:
        print("\nMenú:")
        print("1. Generar factura")
        print("2. Salir")
        opcion = input("Ingrese una opción: ").strip()
        
        if opcion == "1":
            try:
                descripcion, cantidad, precio_unitario, impuesto = solicitar_datos()
                factura = mi.Factura(descripcion, cantidad, precio_unitario, impuesto)  # Cambiado a Factura
                
                total = factura.calcular_total()  # Cambiado a calcular_total
                print(f"\nEl total de la venta es: {total:.2f}")
                
                reporte = factura.generar_reporte()  # Cambiado a generar_reporte
                print(f"El reporte de la factura es:\n{reporte}")
            except AttributeError:
                print("Error: La clase 'Factura' no tiene los métodos necesarios.")
            except Exception as e:
                print(f"Error inesperado: {e}.")
        elif opcion == "2":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    menu()