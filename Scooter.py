from Tecnologia import Tecnologia 
from Transporte import Transporte 

class Scooter(Transporte, Tecnologia):
    def __init__(self, marca,voltaje,precio,eficiencia,peso,aro,velocidad):
        Transporte.__init__(self,peso,aro)
        Tecnologia.__init__(self,marca,voltaje,precio,eficiencia)
        self.__velocidad = velocidad

    def calcularDespacho(self):
        base = super().calcularDespacho()
        pesoa = super().getPeso()
        peso = int(pesoa)
        valorPeso = (peso * 300)
        despachoTotal = base + valorPeso
        return despachoTotal


    def printCotizacion(self):
        txt = f"Marca: {Tecnologia.get_marca(self)}\n"
        txt += f"{Transporte.__str__(self)}"
        return txt



    def __str__(self):
        a = self.calcular_descuento()
        txt = f"{Tecnologia.__str__(self)}"
        txt += f"{Transporte.__str__(self)}"
        txt += f"Velocidad: {self.__velocidad} km/h\n"
        txt += f"Total Despacho por Scooter: ${self.calcularDespacho()}\n"
        txt += f"Descuento Aplicado: ${a[1]}\n"
        txt += f"Total con Descuento: ${a[0]}\n"
        txt += f"Total a pagar: ${int(a[0])+self.calcularDespacho()}\n"
        return txt


    