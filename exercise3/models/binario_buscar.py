
class BusquedaBinaria:
    def buscar(self, datos, objetivo):
        bajo = 0
        alto = len(datos) - 1
        
        while bajo <= alto:
            medio = (bajo + alto) // 2
            if datos[medio] == objetivo:
                return medio
            elif datos[medio] < objetivo:
                bajo = medio + 1
            else:
                alto = medio - 1
        return -1
    
    def obtener_nombre(self):
        return "Búsqueda Binaria"