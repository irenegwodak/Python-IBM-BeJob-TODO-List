class Task():
    def __init__(self, description):
        self.description = description
        self.is_complete = False

    def complete_task(self):
        self.is_complete = True

    def get_description(self):
        return self.description

    def get_status(self):
        return self.is_complete

    def __str__(self):
        status = "Completada" if self.is_complete else "Pendiente"
        return f"{self.description} - {status}"


class ToDoList():
    def __init__(self):
        self.tasks = []

    def print_tasks(self):
        print("\nTareas:")
        if not self.tasks:
            print("No hay tareas.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(i, task)
        print("\n")

    def add_task(self):
        new_task = Task(input("¿Qué tarea quieres añadir?: "))
        self.tasks.append(new_task)
        final_successful_msg("añadida")

    def complete_task(self, index_of_task):
        if self.tasks[index_of_task].get_status():
            print(
                f"La tarea '{self.tasks[index_of_task].get_description()}' ya estaba completada.")

        else:
            self.tasks[index_of_task].is_complete = True
            final_successful_msg("completada")

    def delete_task(self, index_of_task):
        del self.tasks[index_of_task]
        final_successful_msg("eliminada")


todolist = ToDoList()

CONST = dict(

    WELCOME_MSG="""\n
    Bienvenida al To-Do List de Irene García Wodak.
    En este programa puedes añadir, completar o
    eliminar tareas de forma sencilla.
    Espero que lo disfrutes y cualquier duda
    o sugerencia son bienvenidas!!!\n""",

    USER_MENU_OPTIONS=("Agregar una tarea.", "Completar una tarea.",
                       "Eliminar una tarea.", "Salir."),

    CONTINUE_OPTION={"si", "s"},
    NO_CONTINUE_OPTION={"no", "n"},
    OTHER_OPTION={"otro", "otra", "o"},
)
CONST["USER_CHECK_OPTIONS"] = (
    CONST["CONTINUE_OPTION"] | CONST["NO_CONTINUE_OPTION"] | CONST["OTHER_OPTION"])


# FUNCTIONS
def select_menu_option():
    for item in CONST["USER_MENU_OPTIONS"]:
        print(item, f"({CONST['USER_MENU_OPTIONS'].index(item)+1})")

    # handle input
    while True:
        try:
            user_selection = int(input("Elige una opción: "))

            if 1 <= user_selection <= len(CONST["USER_MENU_OPTIONS"]):
                print("\n")
                return user_selection
            else:
                print(
                    f"No existe la opción con número '{user_selection}'. Por favor introduce una opción válida.")

        except ValueError:
            print("\nIntroduce un número válido.")


def print_title_option(option):
    if option == 1:
        action = "Añadir"
    elif option == 2:
        action = "Completar"
    elif user_selection == 3:
        action = "Eliminar"
    print(f"{action} una tarea.".upper())


def final_successful_msg(var):
    print(f"Tarea {var} correctamente.")


# input to select task number
def get_task_number(task_list):
    while True:
        try:
            task_selected = int(
                input("Cuál es el número de la tarea que quieres seleccionar?: "))
            if 0 < task_selected:
                index_task_selected = task_selected - 1
                print(
                    f"La tarea seleccionada es: {task_list[index_task_selected]}")
                return index_task_selected
            else:
                print("Introduce un número mayor a 0.")
        except ValueError:
            print("\nIntroduce un número válido.")
        except IndexError:
            print("No existe la tarea.")


def ask_confirmation():
    while True:
        ask_to_continue = input(
            "¿Deseas continuar o prefieres seleccionar otra tarea? (SI/NO/OTRA): ").strip().lower()

        if ask_to_continue in CONST["CONTINUE_OPTION"]:
            return "yes"
        elif ask_to_continue in CONST["NO_CONTINUE_OPTION"]:
            print("Operación cancelada.")
            return "no"
        elif ask_to_continue in CONST["OTHER_OPTION"]:
            print("Seleccionar otra tarea.")
            return "other"
        else:
            print("\nIntroduce una respuesta válida (SI/NO/OTRA).")


# PROGRAM
# INTRO
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
