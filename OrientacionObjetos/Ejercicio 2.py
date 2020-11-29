
class Documento:
    def __init__(self, encabezado):
        self.encabezado = encabezado

    def __str__(self):
        return self.encabezado

class Tarjeta_de_visita(Documento):
    def __init__(self, encabezado, nombre):
        self.encabezado = encabezado
        self.nombre = nombre

    def __str__(self):
        return self.encabezado + "\n" + self.nombre

class Carta(Documento):
    def __init__(self, encabezado, nombre, fecha):
        self.encabezado = encabezado
        self.nombre = nombre
        self.fecha = fecha

    def __str__(self):
        return self.encabezado + "\n" + self.nombre + "\n" + self.fecha

encabezado = "-------------------DYVEL AUTOMOVILES S.L.-------------------\n" \
             "Dirección: Av. Palomares, 106, 41100 Coria del Río, " \
             "Sevilla\n"

nombre = "Fco Javier Mateos Guillén\n"

fecha = "19/11/2020"

doc = Documento(encabezado)
tarj = Tarjeta_de_visita(encabezado, nombre)
carta = Carta(encabezado, nombre, fecha)

print(doc)
print("/////////////////////////////////////////////////////////////")
print(tarj)
print("/////////////////////////////////////////////////////////////")
print(carta)

