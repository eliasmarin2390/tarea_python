# Ejercicio 3: Paquete de algoritmos de búsqueda

import controllers.buscar_dao as dao
import models.lineal_buscar as lineal
import models.binario_buscar as binario
import os

os.system('cls' if os.name == 'nt' else 'clear')

def main():
    buscador_dao = dao.BuscadorDAO()  # Cambiado de SearchDAO a BuscadorDAO
    
    # Pedir datos al usuario
    print("-" * 30)
    print("Algoritmos de Búsqueda")
    print("-" * 30)
    datos = list(map(int, input("Ingrese una lista de números separados por espacios: ").replace(',', ' ').split()))
    objetivo = int(input("Ingrese el número a buscar: "))
    datos_ordenados = sorted(datos)
    
    print(f"\nLista de números: {datos}")
    print(f"Número a buscar: {objetivo}\n")
    
    # Búsqueda lineal
    print("Posición por búsqueda Lineal:")
    resultado = buscador_dao.buscar('lineal', datos, objetivo)
    print(f"Posición: {resultado}" if resultado != -1 else "No encontrado")
    
    # Búsqueda binaria
    print("\nPosición por búsqueda Binaria:")
    resultado = buscador_dao.buscar('binaria', datos_ordenados, objetivo)
    print(f"Posición: {resultado}" if resultado != -1 else "No encontrado")
    
if __name__ == "__main__":
    main()