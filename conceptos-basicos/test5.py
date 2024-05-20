# 5. Escriba un código que desordene al azar una lista.

from random import shuffle

def shuff(el):
    shuffle(el)
    return el 

list = [1, 2, 3, 4, 5]
print(shuff(list))
