from ClasePersona import Persona

class Empleado(Persona):
    def __init__(self, nombre, indent, edad, sexo, cargo, salario, legajo):
        Persona.__init__(self, nombre, indent, edad, sexo)
        self.cargo = cargo
        self.salario = salario
        self.legajo = legajo
    def __str__(self):
        return "Me llamo {} y mi cargo es {}".format(self.nombre, self.cargo)

daniela = Empleado("Daniela", 43917641, 30, "F", "Gerente", 50000, 1121)
print(daniela)

pedro = Persona("Pedro", 22640915, 2, "M")
print(pedro)
print(pedro.mayor_edad())