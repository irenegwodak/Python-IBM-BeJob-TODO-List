def printer(list):
    for item in list:
        print(item, f"({list.index(item)+1})")

# task printer:
    # check if the list is empty
    # print the list with the index number + status


def print_tasks(tasks):
    print("\nTareas:")
    if not tasks:
        print("No hay tareas.")
    else:
        for task in tasks:
            position = tasks.index(task) + 1
            is_completed = "Completada" if task["is_completed"] else "Pendiente"
            print(position, task["description"], "-", is_completed)
    print("\n")
