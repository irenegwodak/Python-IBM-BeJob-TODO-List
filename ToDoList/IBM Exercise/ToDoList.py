# imported functions (modules created to avoid the spaghetti code)
from printers import *
from list_actions import *

# tupla for define the options for the user menu
user_options = ("Agregar una tarea.", "Completar una tarea.",
                "Eliminar una tarea.", "Salir.")

# empty list for the initial tasks
tasks = []


# function to collect user option
def select_option():
    print("¿Qué te gustaría hacer?")
    print_options(user_options)
    user_selection = int(
        input("Introduce un número: "))
    print("\n")
    return user_selection

# intro to my program
print("""\n
    Bienvenida al To-Do List de Irene García Wodak.
    En este programa puedes añadir, completar o
    eliminar tareas de forma sencilla.
    Espero que lo disfrutes y cualquier duda
    o sugerencia son bienvenidas!!!""")

# code execution in a loop until the user decides to exit
while True:
    # Try block to catch any errors during user interaction
    try:
        # Print the current list of tasks
        print_tasks(tasks)
        # Get the user's menu selection
        user_selection = select_option()

        # Add a task
        if user_selection == 1:
            add_task(tasks)
        # Complete a task
        elif user_selection == 2:
            if len(tasks) == 0:
                print("No hay tareas para completar.")
            else:
                complete_task(tasks)
        # Delete a task
        elif user_selection == 3:
            if len(tasks) == 0:
                print("No hay tareas para eliminar")
            else:
                delete_task(tasks)
        # Exit the program
        elif user_selection == 4:
            print("Gracias por usar mi programa!!!")
            break
        # Handle invalid menu options
        else:
            print(
                f"No existe la opción '{user_selection}'. Por favor introduce una opción válida.")
    except:
        # Handle errors in user input
        print("\nHa habido un error, revisa el dato introducido.")
    finally:
        input("Pulsa intro para continuar.")
