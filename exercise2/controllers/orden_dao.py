# Ejercicio 2: Módulo de ordenamiento

import models.orden as mod_ord

class OrdenDao:
    """DAO para manejar operaciones de ordenamiento"""
    
    def __init__(self):
        self.algoritmo = mod_ord.BubbleSort()  # Acceso mediante el alias
        self.historial = []
    
    def ordenar_lista(self, lista, ascendente=True):
        resultado = self.algoritmo.ordenar(lista.copy(), ascendente=ascendente)  # Cambiado de 'order' a 'ordenar'
        self.historial.append({
            'lista_original': lista.copy(),
            'lista_ordenada': resultado,
            'ascendente': ascendente,
            'algoritmo': self.algoritmo.nombre
        })
        return resultado
    
    def mostrar_lista(self, lista, mensaje="Lista:"):
        self.algoritmo.mostrar_lista(lista, mensaje)