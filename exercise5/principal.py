
import models.cliente as m
import controllers.cliente_controlador as cc

def obtener_entero_valido(mensaje, valor_minimo=None, valor_maximo=None):
    while True:
        try:
            valor = int(input(mensaje))
            if (valor_minimo is not None and valor < valor_minimo) or (valor_maximo is not None and valor > valor_maximo):
                print(f"Por favor, ingrese un número entre {valor_minimo} y {valor_maximo}.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

def obtener_decimal_valido(mensaje, valor_minimo=None, valor_maximo=None):
    while True:
        try:
            valor = float(input(mensaje))
            if (valor_minimo is not None and valor < valor_minimo) or (valor_maximo is not None and valor > valor_maximo):
                print(f"Por favor, ingrese un número entre {valor_minimo} y {valor_maximo}.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número decimal.")

def obtener_cadena_no_vacia(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        else:
            print("La entrada no puede estar vacía. Por favor, intente de nuevo.")

def crear_cliente(tipo_cliente):
    id_cliente = obtener_entero_valido(f"Ingrese el ID para el cliente {tipo_cliente}: ", valor_minimo=1)
    nombre_cliente = obtener_cadena_no_vacia(f"Ingrese el nombre del cliente {tipo_cliente}: ")
    telefono_cliente = obtener_cadena_no_vacia(f"Ingrese el número de teléfono del cliente {tipo_cliente}: ")
    if tipo_cliente == "VIP":
        descuento_cliente = obtener_entero_valido("Ingrese el porcentaje de descuento para el cliente VIP: ", valor_minimo=0, valor_maximo=100)
    else:
        descuento_cliente = 0  # Sin descuento para clientes regulares
    return m.Cliente(id_cliente, nombre_cliente, telefono_cliente, descuento_cliente)

def crear_pedido(tipo_cliente):
    return [
        m.Pedido("comida", obtener_decimal_valido(f"Ingrese el precio de la comida para el cliente {tipo_cliente}: ", valor_minimo=0)),
        m.Pedido("bebida", obtener_decimal_valido(f"Ingrese el precio de la bebida para el cliente {tipo_cliente}: ", valor_minimo=0))
    ]

def main():
    cliente_regular = None
    cliente_vip = None
    pedido_regular = []
    pedido_vip = []

    while True:
        print("\nMenú:")
        print("1. Crear Cliente Regular")
        print("2. Crear Cliente VIP")
        print("3. Agregar Pedido para Cliente Regular")
        print("4. Agregar Pedido para Cliente VIP")
        print("5. Calcular Totales")
        print("6. Salir")
        opcion = int(input("Ingrese su opción: ").strip())

        if opcion == 1:
            cliente_regular = crear_cliente("regular")
        elif opcion == 2:
            cliente_vip = crear_cliente("VIP")
        elif opcion == 3:
            if cliente_regular:
                pedido_regular = crear_pedido("regular")
            else:
                print("Por favor, cree un cliente regular primero.")
        elif opcion == 4:
            if cliente_vip:
                pedido_vip = crear_pedido("VIP")
            else:
                print("Por favor, cree un cliente VIP primero.")
        elif opcion == 5:
            if cliente_regular:
                print("Total para cliente regular:", cliente_regular.calcular_total(pedido_regular))
            else:
                print("No se encontró un cliente regular.")
            if cliente_vip:
                print("Total para cliente VIP:", cliente_vip.calcular_total(pedido_vip))
            else:
                print("No se encontró un cliente VIP.")
        elif opcion == 6:
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()