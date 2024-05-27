# Creamos la clase Padre
class Padre():
    def __init__(self, ojos, cejas):
        self.ojos = ojos
        self.cejas = cejas


# Creamos clase hija que hereda de Padre
class Hijo(Padre):
    # Definimos los atributos en el constructor
    def __init__(self, ojos, cejas, cara):
        self.ojos = ojos  # Sobreescribimos cada atributo
        self.cejas = cejas
        self.cara = cara  # Especificamos el nuevo atributo para Hijo


# Instanciamos
Tomas = Hijo('Marrones', 'Negras', 'Larga')

# Imprimimos los atributos del objeto
print(Tomas.ojos, Tomas.cejas, Tomas.cara)

# Mismo ejemplo llamando al constructor de la clase padre:


class Padre(object):
    def __init__(self, ojos, cejas):
        self.ojos = ojos
        self.cejas = cejas


# Creamos clase hija que hereda de Padre
class Hijo(Padre):
    # creamos el constructor de la clase especificando atributos
    def __init__(self, ojos, cejas, cara):
        # Especificamos la clase y llamamos a su constructor + Atributos
        Padre.__init__(self, ojos, cejas)
        self.cara = cara  # Especificamos el nuevo atributo para Hijo


Tomas = Hijo('Marrones', 'Negras', 'Larga')
print(Tomas.ojos, Tomas.cejas, Tomas.cara)


# UTILIZANDO SUPER()

class Padre(object):
    def __init__(self, ojos, cejas):
        self.ojos = ojos
        self.cejas = cejas


class Hijo(Padre):
    def __init__(self, ojos, cejas, cara):
        # Solicitamos a super llamar de la clase padre esos atributos
        super().__init__(ojos, cejas)
        self.cara = cara  # Especificamos el nuevo atributo para Hijo


Tomas = Hijo('Marrones', 'Negras', 'Larga')
print(Tomas.ojos, Tomas.cejas, Tomas.cara)
