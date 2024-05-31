from constants import *
from printers import printer


def select_menu_option():
    printer(USER_MENU_OPTIONS)

    # handle input
    while True:
        try:
            user_selection = int(input("Elige una opción: "))

            if 1 <= user_selection <= len(USER_MENU_OPTIONS):
                print("\n")
                return user_selection
            else:
                print(
                    f"No existe la opción con número '{user_selection}'. Por favor introduce una opción válida.")

        except ValueError:
            print("\nIntroduce un número válido.")


def final_successful_msg(var):
    print(f"Tarea {var} correctamente.")


# input to select task number
# def get_task_number(task_list):
#     while True:
#         try:
#             task_to_complete = int(
#                 input("Cuál es el número de la tarea que quieres seleccionar?: "))
#             index_task_to_complete = task_to_complete - 1
#             print(
#                 f"La tarea seleccionada es: {task_list[index_task_to_complete]['description']}")
#             return index_task_to_complete
#         except ValueError:
#             print("\nIntroduce un número válido.")
#         except IndexError:
#             print("No existe la tarea.")


# input to continue/not cont process
# def get_confirmation():
#     while True:
#         user_check = input(
#             "¿Deseas continuar o prefieres seleccionar otra tarea? (SI/NO/OTRA): ").strip().lower()

#         if user_check in USER_CHECK_OPTIONS:
#             return user_check
#         else:
#             print("\nIntroduce una respuesta válida (SI/NO/OTRA).")


# def add_task(list):
#     print("Añadir una tarea".upper())
#     new_description = input("¿Qué tarea quieres añadir?: ")
#     list.append({"description": new_description, "is_completed": False})
#     final_successful_msg("añadida")


# def complete_delete_task(user_selection, task_list):


    # while True:
    #     index_of_task = get_task_number(task_list)
    #     confirmation_to_continue = get_confirmation()

    #     if confirmation_to_continue in CONTINUE_OPTION:

    #         # complete: first check if was completed
    #         if user_selection == 2:
    #             if task_list[index_of_task]["is_completed"]:
    #                 print(
    #                     f"La tarea '{task_list[index_of_task]['description']}' ya estaba completada.")
    #                 break
    #             else:
    #                 task_list[index_of_task]["is_completed"] = True
    #                 final_successful_msg("completada")
    #                 break
    #         # delete
    #         if user_selection == 3:
    #             task_list.pop(index_of_task)
    #             final_successful_msg("eliminada")
    #             break

    #     elif confirmation_to_continue in NO_CONTINUE_OPTION:
    #         print("Operación cancelada.")
    #         break
    #     elif confirmation_to_continue in OTHER_OPTION:
    #         print("Seleccionar otra tarea.")
    #         continue
