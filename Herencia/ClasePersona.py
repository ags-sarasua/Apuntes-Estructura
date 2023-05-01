class Persona():
    def __init__(self, nombre, indent, edad, sexo):
        self.nombre = nombre
        self.indent = indent
        self.edad = edad
        self.sexo = sexo
    
    def __str__(self):
        cadena = ""
        cadena = "La persona llamada {} tiene DNI {}, su edad es {}".format(self.nombre, self.indent, self.edad)
        return cadena
    
    def mayor_edad(self):
        return self.edad >= 21

if __name__ == "__main__":
    #Este código se ejecuta solo cuando se ejecuta directamente este archivo, no cuando se lo importa como módulo
    daniela = Persona("Daniela", 43917641, 25, "F")
    print(daniela)