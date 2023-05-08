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
    