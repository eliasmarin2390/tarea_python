# Ejercicio #2: Módulo de ordenamiento Se requiere que los estudiantes diseñen un módulo independiente que contenga implementaciones de algoritmos de ordenamiento simples (bubble sort). El objetivo es que, a partir de una función principal, se invoquen los métodos del módulo para ordenar una lista de números y demostrar la correcta separación de responsabilidades, fomentando la modularidad y la reutilización del código.

class AlgoritmoOrdenamiento:
    """Clase base para algoritmos de ordenamiento"""
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    def ordenar(self, lista, ascendente=True):
        raise NotImplementedError("Método abstracto")
    
    def mostrar_lista(self, lista, mensaje="Lista:"):
        print(f"{mensaje} {', '.join(map(str, lista))}")


class BubbleSort(AlgoritmoOrdenamiento):
    """Implementación concreta de Bubble Sort"""
    
    def __init__(self):
        super().__init__("Bubble Sort")
    
    def ordenar(self, lista, ascendente=True):  # Cambiado 'ascendant' a 'ascendente'
        longitud = len(lista)
        for i in range(longitud):
            intercambio = False
            for j in range(0, longitud - i - 1):
                if (ascendente and lista[j] > lista[j + 1]) or (not ascendente and lista[j] < lista[j + 1]):
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
                    intercambio = True
            if not intercambio:
                break
        return lista