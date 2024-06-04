from constants import CONST


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
            "¿Deseas continuar o prefieres seleccionar otra tarea? (Si/No - Otra): ").strip().lower()

        if ask_to_continue in CONST["CONTINUE_OPTION"]:
            return "yes"
        elif ask_to_continue in CONST["NO_CONTINUE_OPTION"]:
            print("Operación cancelada.")
            return "no"
        elif ask_to_continue in CONST["OTHER_OPTION"]:
            print("Seleccionar otra tarea.")
            return "other"
        else:
            print("\nIntroduce una respuesta válida (Si/No - Otra).")
