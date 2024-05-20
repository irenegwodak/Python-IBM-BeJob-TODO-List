# 2. Invertir palabras de una cadena dada.

# Ejemplo:
# Entrada:
str = "código de práctica de prueba de geeks"
# Salida:
str = "geeks de prueba de práctica de código"

def reverse(sentence):
    words = sentence.split()
    words.reverse()
    reverse_sentence = " ".join(words)
    return reverse_sentence


sentence = "Ola k ase"
reverse_sentence = reverse(sentence)
print(reverse_sentence)