class Ordenador:
    def __init__(self, capacidad, procesador, precioBase):
        self.capacidad = capacidad
        self.procesador = procesador
        self.precioBase = precioBase

    def __str__(self):
        return "------ORDENADOR------\nCapacidad: %s\nProcesador: %s\nPrecio Base: %s" % \
               (self.capacidad, self.procesador, str(self.precioBase))

    def calcularPVP(self, porcentaje):
        return (self.precioBase*porcentaje) + self.precioBase


class Tablet(Ordenador):
    def __init__(self, capacidad, procesador, precioBase, extraRotura):
        Ordenador.__init__(self, capacidad, procesador, precioBase)
        self.extraRotura = extraRotura

    def __str__(self):
        return "------TABLET------\nCapacidad: %s\nProcesador: %s\nPrecio Base: %s" % \
               (self.capacidad, self.procesador, str(self.precioBase))

    def calcularPVP(self, porcentaje):
        return ((self.precioBase*porcentaje) + self.precioBase) + self.extraRotura

class Portatil(Ordenador):
    def __init__(self, capacidad, procesador, precioBase, descuento):
        Ordenador.__init__(self, capacidad, procesador, precioBase)
        self.descuento = descuento

    def __str__(self):
        return "------PORTATIL------\nCapacidad: %s\nProcesador: %s\nPrecio Base: %s" % \
               (self.capacidad, self.procesador, str(self.precioBase))

    def calcularPVP(self, porcentaje):
        return ((self.precioBase * porcentaje) + self.precioBase) - ((self.precioBase * self.descuento) / 100)

ganancia = 0.2
porcentaje_Descuento = 10
tablet = Tablet("64GB", "Exynos 9611", 349.99, 5)
print (tablet)
print ("El precio final de la tablet es de: " + str(round((tablet.calcularPVP(ganancia)), 2)) + "€\n")

portatil = Portatil("512GB", "AMD Ryzen 5 3500U", 749.99, porcentaje_Descuento)
print (portatil)
print ("El precio final del portatil es de: " + str(round((portatil.calcularPVP(ganancia)), 2)) + "€\n")
