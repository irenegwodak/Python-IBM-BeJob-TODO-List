from printers import *
from list_actions import *


user_options = ("Agregar una tarea.", "Completar una tarea.",
                "Eliminar una tarea.", "Salir.")
tasks = []


def select_option():
    print("¿Qué te gustaría hacer?")
    print_options(user_options)
    user_selection = int(
        input("Introduce un número: "))
    print("\n")
    return user_selection


print("""\n
    Bienvenida al To-Do List de Irene García Wodak.
    En este programa puedes añadir, completar o
    eliminar tareas de forma sencilla.
    Espero que lo disfrutes y cualquier duda
    o sugerencia son bienvenidas!!!""")

while True:
    try:
        print_tasks(tasks)
        user_selection = select_option()
        if user_selection == 1:
            add_task(tasks)
        elif user_selection == 2:
            complete_task(tasks)
        elif user_selection == 3:
            if len(tasks) == 0:
                print("No hay tareas para eliminar")
            else:
                delete_task(tasks)
        elif user_selection == 4:
            print("Gracias por usar mi programa!!!")
            break
        else:
            print(
                f"No existe la opción '{user_selection}'. Por favor introduce una opción válida.")
    except:
        print("\nHa habido un error, revisa el dato introducido.")
    finally:
        input("Pulsa intro para continuar.")
