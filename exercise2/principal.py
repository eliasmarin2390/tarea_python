import controllers.orden_dao as dao
import models.orden as mod_ord
import os

# Limpiar consola y configurar colores
os.system('cls' if os.name == 'nt' else 'clear')

# Crear instancia del DAO
orden_dao = dao.OrdenDao()

# Pedir al usuario que ingrese una lista de números
entrada = input("Ingrese una lista de números separados por comas: ")
numeros = list(map(int, entrada.split(',')))

# Mostrar lista original
orden_dao.mostrar_lista(numeros, "Lista original:")

# Ordenar ascendente
ascendente = orden_dao.ordenar_lista(numeros)
orden_dao.mostrar_lista(ascendente, "Orden ascendente:")

# Ordenar descendente
descendente = orden_dao.ordenar_lista(numeros, ascendente=False)
orden_dao.mostrar_lista(descendente, "Orden descendente:")