def final_msg(var):
    print(f"Tarea {var} correctamente.")
    input("Pulsa intro para continuar.")


def add_task(list):
    print("Añadir una tarea")
    new_description = input("¿Qué tarea quieres añadir?: ")
    list.append({"description": new_description, "is_completed": False})
    final_msg("añadida")


def complete_task(list):
    print("Completar una tarea")
    task_to_complete = int(
        input("¿Qué tarea quieres completar? Introduce un número: "))
    index_task_to_complete = task_to_complete - 1
    list[index_task_to_complete]["is_completed"] = True
    final_msg("completada")


def delete_task(list):
    print("Eliminar una tarea")
    task_to_delete = int(
        input("¿Qué tarea quieres eliminar? Introduce un número: "))
    index_task_to_delete = task_to_delete - 1
    list.pop(index_task_to_delete)
    final_msg("eliminada")
