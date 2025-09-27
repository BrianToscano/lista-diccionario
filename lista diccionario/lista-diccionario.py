import json
import os

# Nombre del archivo donde se guardarán los estudiantes
DATA_FILE = "estudiantes.json"

# -------------------------------
# Funciones para manejar archivo
# -------------------------------

def cargar_datos():
    """Carga los estudiantes desde el archivo JSON si existe."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []

def guardar_datos(estudiantes):
    """Guarda la lista de estudiantes en el archivo JSON."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(estudiantes, f, ensure_ascii=False, indent=2)

# -------------------------------
# Lista de estudiantes
# -------------------------------
estudiantes = cargar_datos()

# -------------------------------
# Funciones principales
# -------------------------------

def agregar_estudiante(nombre, edad, calificaciones):
    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "calificaciones": calificaciones
    }
    estudiantes.append(estudiante)
    guardar_datos(estudiantes)   # Guardar en archivo
    print(f" Estudiante {nombre} agregado con éxito.\n")

def eliminar_estudiante(nombre):
    global estudiantes
    estudiantes = [e for e in estudiantes if e["nombre"] != nombre]
    guardar_datos(estudiantes)   # Guardar en archivo
    print(f" Estudiante {nombre} eliminado (si existía en la lista).\n")

def promedio_estudiante(nombre):
    for e in estudiantes:
        if e["nombre"] == nombre:
            notas = [materia["nota"] for materia in e["calificaciones"]]
            promedio = sum(notas) / len(notas)
            return f" El promedio de {nombre} es: {promedio:.2f}"
    return f" Estudiante {nombre} no encontrado."

# -------------------------------
# Menú principal
# -------------------------------

while True:
    print("\n Menú:")
    print("1. Agregar estudiante")
    print("2. Eliminar estudiante")
    print("3. Calcular promedio")
    print("4. Mostrar todos los estudiantes")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre del estudiante: ")
        edad = int(input("Edad del estudiante: "))

        calificaciones = []
        for i in range(4):  # 4 materias fijas
            materia = input(f"Nombre de la materia {i+1}: ")
            nota = float(input(f"Calificación en {materia}: "))
            calificaciones.append({"materia": materia, "nota": nota})

        agregar_estudiante(nombre, edad, calificaciones)

    elif opcion == "2":
        nombre = input("Nombre del estudiante a eliminar: ")
        eliminar_estudiante(nombre)

    elif opcion == "3":
        nombre = input("Nombre del estudiante para calcular promedio: ")
        print(promedio_estudiante(nombre), "\n")

    elif opcion == "4":
        if estudiantes:
            print("\n Lista de estudiantes:")
            for e in estudiantes:
                print(f"- {e['nombre']} ({e['edad']} años)")
                for materia in e["calificaciones"]:
                    print(f"   {materia['materia']}: {materia['nota']}")
        else:
            print("No hay estudiantes registrados.\n")

    elif opcion == "5":
        print("Saliendo del programa...")
        break

    else:
        print(" Opción no válida, intenta de nuevo.\n")
