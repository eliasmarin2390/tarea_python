import controllers.estudianteDao as dao

def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Salir")

if __name__ == "__main__":
    # Crear una instancia de EstudianteDAO
    estudiante_dao = dao.EstudianteDAO()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del estudiante: ")
            edad = input("Ingrese la edad del estudiante: ")
            peso = input("Ingrese el peso del estudiante: ")
            estatura = input("Ingrese la estatura del estudiante: ")
            sexo = input("Ingrese el sexo del estudiante: ")
            promedio = input("Ingrese el promedio del estudiante: ")

            try:
                edad = int(edad)
                estudiante_dao.insertar({"nombre": nombre, "edad": edad, "peso": peso, "estatura": estatura, "sexo": sexo, "promedio": promedio})
                print("Estudiante agregado correctamente.")
            except ValueError:
                print("La edad debe ser un número entero.")
        elif opcion == "2":
            print("Lista de estudiantes:")
            estudiante_dao.mostrar()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")