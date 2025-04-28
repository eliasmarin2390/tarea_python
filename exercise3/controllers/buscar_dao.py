#Ejercicio 3: Paquete de algoritmos de búsqueda

import models.lineal_buscar as lineal
import models.binario_buscar as binario

class BuscadorDAO:
    def __init__(self):
        self.algoritmos = {
            'lineal': lineal.BusquedaLineal(),
            'binaria': binario.BusquedaBinaria()
        }
        self.historial = []
    
    def buscar(self, tipo_algoritmo, datos, objetivo):
        algoritmo = self.algoritmos.get(tipo_algoritmo)
        if not algoritmo:
            raise ValueError("El algoritmo no existe")
        
        resultado = algoritmo.buscar(datos, objetivo)
        self.historial.append({
            'algoritmo': algoritmo.obtener_nombre(),
            'objetivo': objetivo,
            'resultado': resultado
        })
        return resultado