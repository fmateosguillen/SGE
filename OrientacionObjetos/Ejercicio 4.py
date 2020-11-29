import datetime

class Ticket:
    def __init__(self, productos):
        self.productos = []

    def __str__(self):
        return "---------------------------TICKET---------------------------" \
               "\nSUPERMERCADOS DAM                           TRIANA\n" \
               "ID      NOMBRE                  PRECIO.U        PRECIO.T\n" \
               "" + str(self.imprimirProductos()) +\
               "\n------------------------------------------------------------\n" \
               "PRECIO TOTAL COMPRA: " + str(self.sumarProductos()) + "€"

    def imprimirProductos(self):
        for i in self.productos:
            return print(i)

    def sumarProductos(self):
        return
        suma = 0
        for i in self.productos:
            suma = i.precio + suma

class Producto:
    def __init__(self, nombre, precio, codID):
        self.nombre = nombre
        self.precio = precio
        self.codID = codID

class Alimentacion(Producto):
    def __init__(self, nombre, precio, codID, fechaCad, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.codID = codID
        self.fechaCad = fechaCad
        self.cantidad = cantidad

    def comprobarCaducidad(self):
        caducidad = datetime.datetime(self.fechaCad)
        hoy = datetime.datetime.now()
        if(caducidad.year == hoy.year and caducidad.month == hoy.month):
            if(caducidad.day - hoy.day <= 2):
                print("¡<2 días para caducar!")

    def __str__(self):
        return str(self.codID) + "      " + self.nombre + "      " + str(self.precio) + "     " + str(round(self.precio * self.cantidad)) + \
               "\n" + self.comprobarCaducidad()

class Electronica(Producto):
    def __init__(self, nombre, precio, codID, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.codID = codID
        self.cantidad = cantidad

    def __str__(self):
        return str(self.codID) + "      " + self.nombre + "      " + str(self.precio) + "     " + str(round(self.precio * self.cantidad))

class Ropa(Producto):
    def __init__(self, nombre, precio, codID, cantidad, talla):
        self.nombre = nombre
        self.precio = precio
        self.codID = codID
        self.cantidad = cantidad
        self.talla = talla

    def __str__(self):
        return str(self.codID) + "      " + self.nombre + " " + self.talla + "      " + str(self.precio) + "     " + str(round(self.precio * self.cantidad))

camiseta = Ropa("Camiseta 'Llora aquí'", 12.99, 1, 2, "XL")
tablet = Electronica("Samsung Galaxy Tab A", 300, 2, 1)
yogurt = Alimentacion("Yogurt Griego Danone", 2.50, 3, "20/11/2020", 1)
productos = [camiseta, tablet, yogurt]
ticket = Ticket(productos)
print(ticket)

