# CONSTRUCTOR

class Coche():
    # Declaración del constructor de la clase
    def __init__(self):
        self.largo = 250
        self.ancho = 120
        self.ruedas = 4
        self.peso = 900
        self.color = "rojo"
        self.is_enMarcha = False

    def arrancar(self):
        self.is_enMarcha = True

    def estado(self):
        if (self.is_enMarcha == True):
            return "El coche está arrancado"
        else:
            return "El coche está parado"


# Declaración de una instancia de clase, objeto de clase o ejemplar de clase.
coche_1 = Coche()

# Acceso a un atributo de la clase Coche.Nomenclatura del punto.coche_1.ruedas = 7
print("El largo del coche es de", coche_1.largo, "cm.")

# Acceso a un método de la clase Coche.Nomenclatura del punto.
coche_1.arrancar()
print(coche_1.estado())
print("El coche está arrancado:", coche_1.is_enMarcha)
