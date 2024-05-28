from printers import *
from list_actions import *


user_options = ("Agregar una tarea.", "Completar una tarea.",
                "Eliminar una tarea.", "Salir")
tasks = [
    {"description": "tarea uno", "is_completed": False},
    {"description": "tarea dos", "is_completed": True},
]


def select_option():
    print("¿Qué te gustaría hacer?")
    print_options(user_options)
    user_selection = int(
        input("Introduce un número: "))
    print("\n")
    return user_selection


while True:
    # try:
    print_tasks(tasks)
    user_selection = select_option()
    if user_selection == 1:
        add_task(tasks)
    elif user_selection == 2:
        complete_task(tasks)
    elif user_selection == 3:
        delete_task(tasks)
    elif user_selection == 4:
        break
    else:
        print(
            f"No existe la opción '{user_selection}'. Por favor introduce una opción válida.\n")
    # except:
    #     print("Ha habido un error")
