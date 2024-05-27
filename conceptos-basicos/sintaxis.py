tupla = ("a","b","c") # inmutable
lista = ["a", "b", "c"] # mutable
diccionario = {
    "clave1" : "valor1", 
    "clave2" : "valor2"
}

# if
if "condición1" :
     print() # Bloque de código a ejecutar 
elif "condición2":
    print() # Bloque de código a ejecutar
else:
    print() # Bloque de código a ejecutar

#if in
if 3 in tupla:
    print()
else:
    print()

#while
while "condición":
    # Bloque de código a ejecutar mientras la condición sea verdadera
    if "condición_para_break":
        break  # Sale del bucle
    if "condición_para_continue":
        continue  # Salta a la siguiente iteración
else:
    print() # Bloque de código que se ejecuta si el bucle no se rompe con break

#for
for elemento in secuencia:
    # Bloque de código a ejecutar por cada elemento en la secuencia
    if condición_para_break:
        break  # Sale del bucle
    if condición_para_continue:
        continue  # Salta a la siguiente iteración
else:
    # Bloque de código que se ejecuta si el bucle no se rompe con break
