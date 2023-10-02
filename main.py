from Scooter import Scooter
from Tecnologia import Tecnologia
from TV import TV
from Consola import Consola
from Transporte import Transporte
from Bicicleta import Bicicleta
from Scooter import Scooter

teves = []
consolas = []
scooters = []
bicis = []


def entero(var:str):
    while True:
        try:
            ent = int(input(f"Ingrese {var}: "))
            break
        except:
            print("Debes ingresar un numero entero")   
    return ent

def cotizacion(lista:list,productoPlural:str,producto:str):
    if len(lista) != 0:
        a = 0
        print(f"{productoPlural} en el registro")
        for x in lista:
            print(f"\n\n{a+1}: \n{x.printCotizacion()}\n\n")
            a += 0
        valor = entero(f"{producto} que desea cotizar")
        print(f"{lista[valor-1]}")
    else:
        print(f"\nNo hay {productoPlural.lower()} en el registro\n")



def menu():
    while True:
        print("1. Registrar TV\n2. Registro Consola\n3. Registro Scooter\n4. Registro Bicicleta\n5. Cotizar TV\n6. Cotizar Consola\n7. Cotizar Scooter\n8. Cotizar Bicicleta\n9. Salir")
        opcion = input("Ingrese lo que desea realizar: ")
        if opcion == "1":
            RegistroTele()
        elif opcion == "2":
            RegistroConsola()
        elif opcion == "3":
            RegistroScooter()
        elif opcion == "4":
            RegistroBici()
        elif opcion == "5":
            CotizarTele()
        elif opcion == "6":
            CotizarConsolas()
        elif opcion == "7":
            CotizarScooter()
        elif opcion == "8":
            CotizarBici()
        elif opcion == "9":
            print("Gracias, vuelvas prontos")
            break
        else:
            print("Debes ingresar un valor válido")


def RegistroTele():
    print(f"\n\nVas a registrar una televisión: \n\n")
    marca = input("Ingrese la marca de la televisión: ")
    voltaje = entero("el voltaje que consume la TV (Wh) ")
    precio = entero("el precio de la TV: ") 
    eficiencia = input("Ingrese la eficiencia de la tv: ")
    tamanio = entero("el tamaño de la tv (en pulgadas): ")
    tele = TV(marca,voltaje,precio,eficiencia,tamanio)
    teves.append(tele)
    print("\nRegistro realizado\n")


def RegistroConsola():
    print(f"\nVas a registrar una consola: \n\n")
    nomConsola = input("Ingrese el nombre de la consola: ")
    version = input("Ingrese la versión: ")
    marca = input("Ingrese la marca de la consola: ")
    voltaje = entero("el voltaje que consume la consola (Wh) ")
    precio = entero("el precio de la consola: ")
    eficiencia = input("Ingrese la eficiencia de la consola: ")
    consola = Consola(nomConsola,marca,voltaje,precio,eficiencia,version)
    consolas.append(consola) 
    print("\nRegistro realizado\n")   
    

def RegistroScooter():
    print(f"\nVas a registrar un Scooter: \n\n")
    marca = input("Ingrese la marca del scooter: ")
    voltaje = entero("el voltaje que consume el scooter (Wh)") 
    precio = entero("el precio del scooter")
    eficiencia = input("Ingrese la eficiencia energética del scooter: ")
    peso = entero("el peso del scooter (en kg)")
    aro = entero("el aro de la rueda del scooter")
    velocidad = entero("la velocidad máxima del scooter")
    scooterI = Scooter(marca,voltaje,precio,eficiencia,peso,aro,velocidad)
    scooters.append(scooterI)
    print("\nRegistro realizado\n")
    

def RegistroBici():
    print(f"\nVas a registrar una bicicleta: \n\n")
    marca = input("Ingrese la marca de la bicicleta: ")
    aro = entero("el aro de la bicicleta")
    peso = entero("el peso de la bicicleta (kg)")
    precio = entero("el precio de la bicicleta") 
    cleta = Bicicleta(peso,aro,precio,marca)
    bicis.append(cleta)
    print("\nRegistro realizado\n")




def CotizarTele():
    cotizacion(teves,"Televisiones","la television")

def CotizarConsolas():
    cotizacion(consolas,"Consolas","la consola")


def CotizarScooter():
    cotizacion(scooters,"Scooters","el scooter")
    

def CotizarBici():
    cotizacion(bicis,"Bicicletas","la bicicleta")
        


menu()