# 11. Escribir un algoritmo de ordenación para un conjunto de datos numéricos en Python.


def ordenar(li):
    new_li = li[:]
    new_li.sort()
    return new_li


lista = [3, 7, 1, 9, 5]
lista_ordenada = ordenar(lista)

print("lista origianl", lista)
print("lista ordenada", lista_ordenada)
