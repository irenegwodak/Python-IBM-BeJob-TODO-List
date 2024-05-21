# 10. Escribir un programa en Python
# para comprobar si un número es capicúa

def is_capicua(num):
    stringify_num = str(num)
    reverse_str_num = stringify_num[::-1]
    reverse_num = int(reverse_str_num)

    print(num, "es capicúa") if num == reverse_num else print(
        num, "no es capicúa")

    return num == reverse_num


while True:
    try:
        input_number = int(
            input("Introduce un número y te digo si es capicúa: "))
        is_capicua(input_number)
    except ValueError:
        print("Introduce un número válido")
