class Vehiculo:
    def __init__(self, cilindrada, caballos, combustible, impuestoC):
        self.cilindrada = cilindrada
        self.caballos = caballos
        self.combustible = combustible
        self.impuestoC = impuestoC

    def calcularImpuestoCirculacion(self):
        return self.impuestoC


class Motocicleta(Vehiculo):
    def __init__(self, cilindrada, caballos, combustible, porcentajePotencia, impuestoC):
        self.cilindrada = cilindrada
        self.caballos = caballos
        self.combustible = combustible
        self.porcentajePotencia = porcentajePotencia
        self.impuestoC = impuestoC

    def __str__(self):
        return "MOTOCICLETA\nCilindrada: "+\
               str(self.cilindrada)+"\nCV: "\
               +str(self.caballos)+"\nCombustible: "\
               +self.combustible+"\nImpuesto de Circulación: "\
               +str(self.calcularImpuestoCirculacion())+"€"

    def calcularImpuestoCirculacion(self):
        return self.impuestoC + ((self.caballos * self.porcentajePotencia) / 100)

class Coche(Vehiculo):
    def __init__(self, cilindrada, caballos, combustible, porcentaceCilindrada, impuestoC):
        self.cilindrada = cilindrada
        self.caballos = caballos
        self.combustible = combustible
        self.porcentaceCilindrada = porcentaceCilindrada
        self.impuestoC = impuestoC

    def __str__(self):
        return "COCHE\nCilindrada: "+\
               str(self.cilindrada)+"\nCV: "\
               +str(self.caballos)+"\nCombustible: "\
               +self.combustible+"\nImpuesto de Circulación: "\
               +str(self.calcularImpuestoCirculacion())+"€"

    def calcularImpuestoCirculacion(self):
        return self.impuestoC + ((self.cilindrada * self.porcentaceCilindrada) / 100)

class Furgoneta(Vehiculo):
    def __init__(self, cilindrada, caballos, combustible, extra, impuestoC):
        self.cilindrada = cilindrada
        self.caballos = caballos
        self.combustible = combustible
        self.extra = extra
        self.impuestoC = impuestoC

    def __str__(self):
        return "FURGONETA\nCilindrada: "+\
               str(self.cilindrada)+"\nCV: "\
               +str(self.caballos)+"\nCombustible: "\
               +self.combustible+"\nImpuesto de Circulación: "\
               +str(self.calcularImpuestoCirculacion())+"€"

    def calcularImpuestoCirculacion(self):
        return self.impuestoC + self.extra

cilindrada = 1800
caballos = 100
combustible = "DIESEL"
porcentajeCilindrada = 25
porcentajePotencia = 60
extra = 7.5
impuestoC = 20

coche = Coche(cilindrada, caballos, combustible, porcentajeCilindrada, impuestoC)

moto = Motocicleta(cilindrada, caballos, combustible, porcentajePotencia, impuestoC)

furgoneta = Furgoneta(cilindrada, caballos, combustible, extra, impuestoC)

print(coche)
print("-----------------------------------------")
print(moto)
print("-----------------------------------------")
print(furgoneta)
