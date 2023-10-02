from Tecnologia import Tecnologia
class Consola(Tecnologia):
    def __init__(self, nombreConsola, marca, voltaje, precio, eficiencia,version):
        super().__init__(marca, voltaje, precio, eficiencia)
        self.__nombreConsola = nombreConsola
        self.__version = version


    def calcular_descuento(self):
        a = super().calcular_descuento()
        descuentoEficiencia = a[1]
        if self.__version.lower()=="lite":
            descuentoVersion = (super().get_precio()*5)/100
            descuentoFinal = descuentoEficiencia + descuentoVersion
            return descuentoFinal

            
    def printCotizacion(self):
        txt = f"{self.__nombreConsola}\n{self.__version}"
        return txt

    def __str__(self):
        a = super().calcular_descuento()
        txt = f"\nNombre Consola: {self.__nombreConsola}"
        txt += f"\nVersion: {self.__version}"
        txt += f"{super().__str__()}"
        if self.__version.lower() != "lite":
            txt += f"Descuento total: ${a[1]}\n"
            txt += f"Total a pagar: ${a[0]}\n"
        else:
            descuento = self.calcular_descuento()
            descTotalVersion = super().get_precio() - descuento
            txt += f"Descuento total: ${descuento}\n"
            txt += f"Total a pagar: ${descTotalVersion}\n"
        return txt

