# 1. Dados dos números, escriba un código Python para encontrar el mínimo de estos dos números

# Ejemplos: 
# Entrada: a = 2, b = 4
# Salida: 2


# Entrada: a = -1, b = -4
# Salida:-4

def min(a, b):
    return a if a<b else b

print(min(-2, 4))