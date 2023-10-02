from Transporte import Transporte
class Bicicleta(Transporte):
    def __init__(self, peso, aro, precio, marca):
        super().__init__(peso, aro)
        self.__precio = precio
        self.__marca = marca


    def calcularDespacho(self):
        base = super().calcularDespacho()
        pesoa = super().getPeso()
        peso = int(pesoa)
        valorPeso = (peso * 400)
        despachoTotal = base + valorPeso
        return despachoTotal


    def printCotizacion(self):
        txt = f"Marca: {self.__marca}\n"
        txt += f"{super().__str__()}"
        return txt

    def __str__(self):
        txt = f"\nMarca: {self.__marca}\n"
        txt += f"{super().__str__()}"
        txt += f"Costo Despacho: ${self.calcularDespacho()}\n"
        txt += f"Precio Bicicleta: ${self.__precio}\n"
        txt += f"Total a pagar: ${int(self.__precio) + self.calcularDespacho()}\n"
        return txt
