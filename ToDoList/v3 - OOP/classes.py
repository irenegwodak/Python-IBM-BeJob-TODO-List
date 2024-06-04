from printers import final_successful_msg


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
        print("\n\n=========================")
        print("Tareas:")
        print("=========================\n")
        if not self.tasks:
            print("No hay tareas.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(i, task)
        print("\n=========================\n\n")

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
