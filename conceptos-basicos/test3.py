# 3. Realizar una suma de los elementos de una tupla

def add(tupla):
    acc = 0
    for number in tupla:
        acc += number
    return acc


tupla = (2, 2, 2, 2, 2)
result = add(tupla)

print(result)

#otra opción

res = sum(tupla)
print(res)