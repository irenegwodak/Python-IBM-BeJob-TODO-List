user_options = ("Agregar una tarea.", "Completar una tarea.",
                "Eliminar una tarea.", "Salir")


tasks = [
    {"description": "tarea uno", "is_completed": False},
    {"description": "tarea dos", "is_completed": True},
]


def print_tasks():
    print("Tareas:")
    for task in tasks:
        position = tasks.index(task) + 1
        is_completed = "Completada" if task["is_completed"] else "Pendiente"
        print(position, task["description"], "-", is_completed)
    print("\n")


def print_options():
    for option in user_options:
        print(user_options.index(option) + 1, option)


def select_option():
    print("¿Qué te gustaría hacer?")
    print_options()
    user_selection = int(
        input("Introduce un número: "))
    print("\n")
    return user_selection


def final_msg(var):
    print(f"Tarea {var} correctamente.")
    input("Pulsa intro para continuar.\n")
    # print("\n")


def add_task():
    print("Añadir una tarea")
    new_description = input("¿Qué tarea quieres añadir?: ")
    tasks.append({"description": new_description, "is_completed": False})
    final_msg("añadida")


def complete_task():
    print("Completar una tarea")
    task_to_complete = int(
        input("¿Qué tarea quieres completar? Introduce un número: "))
    tasks[task_to_complete-1]["is_completed"] = True
    final_msg("completada")


def delete_task():
    print("Eliminar una tarea")
    task_to_delete = int(
        input("¿Qué tarea quieres eliminar? Introduce un número: ")) - 1
    tasks.pop(task_to_delete)
    final_msg("eliminada")


while True:
    # try:
    print_tasks()
    user_selection = select_option()
    if user_selection == 1:
        add_task()
    elif user_selection == 2:
        complete_task()
    elif user_selection == 3:
        delete_task()
    elif user_selection == 4:
        break
    else:
        print(
            f"No existe la opción '{user_selection}'. Por favor introduce una opción válida.\n")
    # except:
    #     print("Ha habido un error")
