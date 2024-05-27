#  Crear e instanciar una clase

# Declaración de la clase
class Coche():
    # Declaración de atributos
    largo = 250
    ancho = 120
    ruedas = 4
    peso = 900
    color = "rojo"
    is_enMarcha = False

    # Declaración de métodos
    def arrancar(self):  # self hace referencia a la instancia de clase.
        self.is_enMarcha = True

    def estado(self):
        if (self.is_enMarcha == True):
            return "El coche está arrancado"
        else:
            return "El coche está parado"


# Ejercicios
# Crearemos una clase Usuario que tendrá los siguientes atributos:
# • nombre : string
# • edad : number
# • login : string
# • password : string
# • email : string
# • telefono : number

# Y los siguientes métodos:
# • Resumen(): Sacará un resumen de los datos del usuario
# • cambiaEdad(): Nos dará la posibilidad de pedir al usuario que introduzca una nueva edad.
# • muestraEdad(): Nos mostrará la edad del usuario

""" Por último, crearemos una instancia de la clase Usuario a la que llamaremos administrador 
y llamaremos a los métodos de la clase Usuario para este administrador usando la nomenclatura del punto. """


class Usuario():
    nombre = "Irene"
    edad = 34
    login = "irene"
    password = "abc1234"
    email = "email@gmail.com"
    telefono = 666777888

    def resumen(self):
        print(f'Los datos del usuario son:\n'
              f'Nombre: {self.nombre}\n'
              f'Edad: {self.edad}\n'
              f'Login: {self.login}\n'
              f'Password: {self.password}\n'
              f'Email: {self.email}\n'
              f'Teléfono: {self.telefono}')

    def cambiarEdad(self):
        nuevaEdad = int(input("Introduce la nueva edad (entre 18 y 100):"))
        if 18 <= nuevaEdad <= 100:
            self.edad = nuevaEdad
            print("Nueva edad introducida correctamente")
            return ""
        else:
            print("La edad introducida no es correcta")
            return ""

    def muestraEdad(self):
        print('La edad del usuario es:', self.edad, 'años.')
        return ""

administrador = Usuario()

administrador.resumen()
administrador.cambiarEdad()
administrador.muestraEdad()