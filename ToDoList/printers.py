
def print_tasks(tasks):
    print("\nTareas:")
    for task in tasks:
        position = tasks.index(task) + 1
        is_completed = "Completada" if task["is_completed"] else "Pendiente"
        print(position, task["description"], "-", is_completed)
    print("\n")


def print_options(user_options):
    for option in user_options:
        print(user_options.index(option) + 1, option)
