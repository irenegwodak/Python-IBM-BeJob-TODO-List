def print_title_option(option):
    if option == 1:
        action = "Añadir"
    elif option == 2:
        action = "Completar"
    elif option == 3:
        action = "Eliminar"
    print(f"{action} una tarea.".upper())


def final_successful_msg(var):
    print(f"Tarea {var} correctamente.")

