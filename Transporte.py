class Transporte():
    def __init__(self,peso,aro):
        self.__peso = peso
        self.__aro = aro
        self.__costoDespachoBase = 4000
    

    def getPeso(self):
        return self.__peso


    def calcularDespacho(self):
        return self.__costoDespachoBase




    def __str__(self):
        txt = f"Aro: {self.__aro} \n"
        txt += f"Peso: {self.__peso} kg\n"
        return txt