# Enunciado:

""" Escribe un programa en Python utilizando Programación Orientada a Objetos que gestione
una lista de tareas pendientes. El programa deberá permitir al usuario realizar las siguientes
operaciones: """
# • Agregar una nueva tarea: El programa deberá permitir al usuario agregar una nueva tarea a la lista de tareas pendientes.
# • Marcar una tarea como completada: El programa deberá permitir al usuario marcar una tarea como completada, dada su posición en la lista.
# • Mostrar todas las tareas: El programa deberá imprimir en pantalla todas las tareas pendientes, numeradas y mostrando su estado (completada o pendiente).
# • Eliminar una tarea: El programa deberá permitir al usuario eliminar una tarea de la lista, dada su posición.

""" El programa deberá incluir las siguientes características:"""
# • Manejo de excepciones: El programa deberá manejar excepciones en caso de que el usuario ingrese una opción no válida o una posición que no exista en la lista.
# • Comentarios explicativos: El código deberá estar comentado para explicar su funcionamiento en cada parte relevante.

user_options = ["Agregar una tarea.",
                "Completar una tarea.", "Eliminar una tarea."]

tasks = {
    "1": {"Description": "Tarea a",
          "is_completed": False},
    "2": {"Description": "Tarea b",
          "is_completed": True},
}


def print_tasks():
    print("Tareas:")
    for task in tasks:
        is_completed = "Completada" if tasks[task]["is_completed"] else "Pendiente"
        print(task, tasks[task]["Description"], "-", is_completed)
    print("\n")


def print_options():
    for option in user_options:
        print(user_options.index(option) + 1, option)


def select_option():
    print("Tienes estas opciones:")
    print_options()
    user_selection = int(input("¿Qué te gustaría hacer? Introduce un número: "))
    return user_selection


while True:
    print_tasks()
    user_selection = select_option()

    break
