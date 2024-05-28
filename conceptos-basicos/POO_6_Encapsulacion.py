class Ejemplo:
    __atributo_privado = "Soy un atributo inalcanzable desde fuera."

    def __metodo_privado(self):
        print("Soy un método inalcanzable desde fuera.")

    def atributo_publico(self):
        return self.__atributo_privado

    def metodo_publico(self):
        return self.__metodo_privado()


e = Ejemplo()
print("atributo público: ", e.atributo_publico())
e.metodo_publico()


class Coche:
    def __init__(self):
        self.__largo = 250
        self.__ancho = 120
        self.__ruedas = 4
        self.__peso = 900
        self.__color = "rojo"
        self.__is_enMarcha = False

    def arrancar(self):
        self.is_enMarcha = True

    def estado(self):
        if (self.is_enMarcha == True):
            return "El coche está arrancado"
        else:
            return "El coche está parado"


miCoche = Coche()
miCoche.__ruedas = 9
print("Mi coche tiene", miCoche.__ruedas, "ruedas.")
