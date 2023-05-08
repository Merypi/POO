

class Viajero_Frecuente:
    __numviajero=0
    __dni= " "
    __nombre= " "
    __apellido=" "
    __millasacum=0

    def __init__(self, num_viajero: int=0, DNI="", nombre="", apellido= "", millas_acum:int=0 ):
        self.__numviajero= num_viajero
        self.__dni= DNI
        self.__nombre= nombre
        self.__apellido= apellido
        self.__millasacum= millas_acum

    def __str__(self):
        return('{} {} {} {} {}'.format(self.__numviajero, self.__dni, self.__nombre, self.__apellido, self.__millasacum))
    
    def getviajero(self):
        return self.__numviajero
    
    def cantidadTotaldeMillas(self): # retorna la cantidad de millas acumuladas.
        return  self.__millasacum

    def acumularMillas(self, newmillas:int): 
        if newmillas != 0:
            self.__millasacum += newmillas
            print("el nuevo total de millas acumuladas es:{}".format(self.__millasacum))
        else:
            print("no se ha podido encontrado al viajero solicitado")
        return self.__millasacum
    
    def canjearmillas(self, cant):
       if cant <= self.__millasacum:
           self.__millasacum -= cant
           print("El canje ha sido realizado con éxito, millas restantes{}".format(self.__millasacum))
       else:
           print("No es posible realizar el canje")
        