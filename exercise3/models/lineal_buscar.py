
class BusquedaLineal:
    def buscar(self, datos, objetivo):
        for indice, elemento in enumerate(datos):
            if elemento == objetivo:
                return indice
        return -1
    
    def obtener_nombre(self):
        return "Búsqueda Lineal"