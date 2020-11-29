class Empleado:
    def __init__(self, nombre, sueldoBase, numEmpleado):
        self.nombre = nombre
        self.sueldoBase = sueldoBase
        self.numEmpleado = numEmpleado

    def __str__(self):
        return "Número de Empleado: "+str(self.numEmpleado)+\
               "\nNombre: "+self.nombre+"\nSueldo: "+\
               str(self.sueldoBase) + "\n"

class Empleado_A_Comision(Empleado):
    def __init__(self, nombre, sueldoBase, numEmpleado, incentivo, ventas):
        self.nombre = nombre
        self.sueldoBase = sueldoBase
        self.numEmpleado = numEmpleado
        self.incentivo = incentivo
        self.ventas = ventas

    def __str__(self):
        return "Número de Empleado: "+str(self.numEmpleado)+\
               "\nNombre: "+self.nombre+"\nSueldo: "\
               +str(((self.sueldoBase * self.incentivo) / 100)
                    + self.sueldoBase) + "\n" + str(self.comprobarIncentivo()) + "\n"

    def comprobarIncentivo(self):
        if((self.ventas * self.incentivo) / 100 > 500):
            return print("¡Felicidades " +
                  self.nombre+ ", has ganado más de "
                               "500€ gracias a tus ventas!")

class Empleado_Fijo:
    def __init__(self, nombre, sueldoBase, numEmpleado, impuestos):
        self.nombre = nombre
        self.sueldoBase = sueldoBase
        self.numEmpleado = numEmpleado
        self.impuestos = impuestos

    def __str__(self):
        return "Número de Empleado: "+str(self.numEmpleado)+\
               "\nNombre: "+self.nombre+"\nSueldo: "\
               +str(self.sueldoBase -
                    ((self.sueldoBase * self.impuestos) / 100)) + "\n"

emp1 = Empleado("Pepe", 1000, 1)
emp2 = Empleado_A_Comision("Marta", 1000, 2, 10, 8000)
emp3 = Empleado_Fijo("Julio", 1000, 3, 5)
empleados = [emp1, emp2, emp3]

for i in empleados:
    print(i)

