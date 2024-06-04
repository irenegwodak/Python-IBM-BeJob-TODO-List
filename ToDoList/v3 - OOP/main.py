from constants import CONST
from classes import ToDoList
from printers import print_title_option
from inputs import select_menu_option, get_task_number, ask_confirmation


todolist = ToDoList()
print(CONST["WELCOME_MSG"])
input("Pulsa intro para continuar.")


# LOOP SINCE EXIT
while True:
    try:
        todolist.print_tasks()
        user_selection = select_menu_option()

        if user_selection == 1:
            print_title_option(user_selection)
            todolist.add_task()

        elif user_selection in {2, 3}:
            print_title_option(user_selection)

            if not todolist.tasks:
                print("No hay tareas.")
            else:
                while True:
                    index_of_task = get_task_number(todolist.tasks)
                    confirmation_to_continue = ask_confirmation()

                    if confirmation_to_continue == "yes":
                        if user_selection == 2:
                            todolist.complete_task(index_of_task)
                            break
                        elif user_selection == 3:
                            todolist.delete_task(index_of_task)
                            break
                    elif confirmation_to_continue == "no":
                        break
                    elif confirmation_to_continue == "other":
                        continue

        elif user_selection == 4:
            print("Gracias por usar este programa!!!")
            break

        else:
            print("Ha habido un error, contacta con el administrador.")
    finally:
        input("Pulsa intro para continuar.")
