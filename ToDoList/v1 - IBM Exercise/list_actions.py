# Function to print a final message with the task status
def final_msg(var):
    print(f"Tarea {var} correctamente.")

# Function to add a task to the list
# Ask user for the description of the new task
# Add the task at the last position in the list
def add_task(list):
    print("Añadir una tarea")
    new_description = input("¿Qué tarea quieres añadir?: ")
    list.append({"description": new_description, "is_completed": False})
    final_msg("añadida")

# Function to complete a task in the list
# Ask user for the task number to complete
# Check if the task was already completed

def complete_task(list):
    print("Completar una tarea")
    task_to_complete = int(
        input("¿Qué tarea quieres completar? Introduce un número: "))
    index_task_to_complete = task_to_complete - 1
    if list[index_task_to_complete]["is_completed"]:
        print("La tarea ya estaba completada.")
    else:
        list[index_task_to_complete]["is_completed"] = True
        final_msg("completada")

# Function to delete a task from the list
# Ask user for the task number to delete
# Delete the task from the list

def delete_task(list):
    print("Eliminar una tarea")
    task_to_delete = int(
        input("¿Qué tarea quieres eliminar? Introduce un número: "))
    index_task_to_delete = task_to_delete - 1
    list.pop(index_task_to_delete)
    final_msg("eliminada")
