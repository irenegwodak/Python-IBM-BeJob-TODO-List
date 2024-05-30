from printers import printer, print_tasks
from user_actions import *

tasks = []

# INTRO
print("""\n
    Bienvenida al To-Do List de Irene García Wodak.
    En este programa puedes añadir, completar o
    eliminar tareas de forma sencilla.
    Espero que lo disfrutes y cualquier duda
    o sugerencia son bienvenidas!!!\n""")
input("Pulsa intro para continuar.")


# Loop since user select Exit
while True:
    try:
        print_tasks(tasks)
        user_selection = select_menu_option()

        if user_selection == 1:
            add_task(tasks)
        elif user_selection in {2, 3}:
            if not tasks:
                print("No hay tareas.")
            else:
                complete_delete_task(user_selection, tasks)
        elif user_selection == 4:
            print("Gracias por usar mi programa!!!")
            break
        else:
            print("Ha habido un error, contacta con el administrador.")
    finally:
        input("Pulsa intro para continuar.")
