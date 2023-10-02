class Tecnologia():
    def __init__(self,marca,voltaje,precio,eficiencia):
        self.__marca = marca
        self.__voltaje = voltaje
        self.__precio = precio
        self.__eficiencia = eficiencia
        


    def calcular_descuento(self):
        if self.__eficiencia.upper() == "A" or self.__eficiencia == "B":
            descuento = ((self.__precio * 50)/100)
        elif self.__eficiencia.upper() == "C" or self.__eficiencia.upper() == "D":
            descuento = ((self.__precio * 30)/100)
        elif self.__eficiencia.upper() == "E" or self.__eficiencia.upper() == "F":
            descuento = ((self.__precio * 10)/100)
        else:
            descuento = 0
        total = self.__precio - descuento 
        return total, descuento

    def get_precio(self):
        return self.__precio

    def get_marca(self):
        return self.__marca

    def __str__(self):
        txt = f"\nMarca: {self.__marca}\n"
        txt += f"Voltaje: {self.__voltaje} Wh\n"
        txt += f"Precio: ${self.__precio}\n"
        txt += f"Eficiencia: {self.__eficiencia}\n"
        return txt
        

