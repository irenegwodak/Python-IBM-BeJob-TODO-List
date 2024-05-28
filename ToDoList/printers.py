# Printer of the list of tasks
# Check if the list is empty and print a message
# Print the list with the index number
def print_tasks(tasks):
    print("\nTareas:")
    if len(tasks) == 0:
        print("No hay tareas.")
    else:
        for task in tasks:
            position = tasks.index(task) + 1
            is_completed = "Completada" if task["is_completed"] else "Pendiente"
            print(position, task["description"], "-", is_completed)
    print("\n")

# Print the menu options to the user
def print_options(user_options):
    for option in user_options:
        print(user_options.index(option) + 1, option)
