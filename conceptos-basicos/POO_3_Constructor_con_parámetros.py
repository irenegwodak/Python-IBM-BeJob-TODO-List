class Coche:
    # Declaración del constructor con parámetros
    def __init__(self, largo, ancho, ruedas, peso, color, is_enMarcha):
        self.ancho = ancho
        self.ruedas = ruedas
        self.peso = peso
        self.color = color
        self.is_enMarcha = is_enMarcha


# Declaración de dos instancias de clase pasándoles los parámetros requeridos en el constructor.
coche_1 = Coche(400, 160, 4, 1200, "amarillo", True)
coche_2 = Coche(420, 150, 4, 1500, "verde", False)

print(coche_1.color)
print(coche_2.color)

coche_3 = Coche(ruedas = 4, color="piruleta", largo=420, ancho=150, peso=1500,
                is_enMarcha=False)

print(coche_3.color)
print(coche_3.ruedas)
