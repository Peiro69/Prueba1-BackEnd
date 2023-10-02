from Tecnologia import Tecnologia
class TV(Tecnologia):
    def __init__(self, marca, voltaje, precio, eficiencia,tamanio):
        super().__init__(marca, voltaje, precio, eficiencia)
        self.__tamanio = tamanio


    def printCotizacion(self):
        txt = f"Marca: {super().get_marca()}\n{self.__tamanio} pulgadas"
        return txt
        


    def __str__(self):
        a = super().calcular_descuento()
        txt = super().__str__()
        txt += f"Tamaño: {self.__tamanio} pulgadas"
        txt += f"\nDescuento Aplicado: ${a[1]}"
        txt += f"\nTotal a pagar: ${a[0]}\n"
        return txt