from viajero import Viajero_Frecuente
import csv

class manejador:
    __listaviajeros=[]

    def __init__(self):
        self.__listaviajeros=[]
    
    def carga(self):
        archivo= open("Viajeros.csv")
        reader = csv.reader(archivo, delimiter= ";")
        next(reader)
        for fila in reader:
            num = int(fila[0])
            dni = int(fila[1])
            nombre= str(fila[2])
            apellido= str(fila[3])
            millasAcum= int(fila[4])
            viajero = Viajero_Frecuente(num,dni,nombre, apellido, millasAcum)
            self.__listaviajeros.append(viajero)
        archivo.close()
        return self.__listaviajeros

    def funcion2_3(self):
        viajero= self.__listaviajeros[0]
        print("\n")
        print("Se mostrara una instancia de la clase viajero:")
        viajero.mostrar()
        viajero +=1000
        print("Se acumularon nuevas millas, a continuacion se muestra su actualizacion: ")
        viajero.mostrar()
        print("\n")
        print("Se realiza el canje:")
        viajero -=500
        viajero.mostrar()
        print("\n")

    def comparacion(self):
        print("Se realiza comparacion de cantidad de milla acumuladas con el numero 1000")
        for i in range(len(self.__listaviajeros)):
            print("El viajero {} tiene {} millas acumuladas".format(self.__listaviajeros[i].getnombre(), self.__listaviajeros[i].cantidadTotaldeMillas()))
            if self.__listaviajeros[i] == 1000:
                print("Misma cantidad de millas acumuladas")
            else:
                print("No tienen esa cantidad de millas")

    def acumulaporderecha(self):
        print("\n")
        print("NUEVA CANTIDAD DE MILLAS ACUMULADAS")
        for i in range(len(self.__listaviajeros)):
            a=1000 + self.__listaviajeros[i]
            print("El viajero {} ahora tiene {} millas acumuladas".format(self.__listaviajeros[i].getnombre(), a))
        print ("\n")

    def canjeporderecha(self):
        print("Realiza canje")
        for i in range(len(self.__listaviajeros)):
            b=1000 - self.__listaviajeros[i]
            print("Nueva cantidad de millas")
            print("El viajero {} ahora tiene {} millas acumuladas".format(self.__listaviajeros[i].getnombre(), b))
        