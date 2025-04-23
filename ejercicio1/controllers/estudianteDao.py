from models.estudiante import Nodo

class EstudianteDAO:
    def __init__(self):
        self.cabeza = None

    def insertar(self, estudiante):
        nuevo_nodo = Nodo(estudiante)  # Ahora Nodo es una clase
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.estudiante)
            actual = actual.siguiente