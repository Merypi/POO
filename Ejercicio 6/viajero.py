class Viajero_Frecuente:
    __numviajero=0
    __dni= " "
    __nombre= " "
    __apellido=" "
    __millasacum=0

    def __init__(self, num_viajero: int=0, DNI="", nombre="", apellido= "", millasacum:int=0 ):
        self.__numviajero= num_viajero
        self.__dni= DNI
        self.__nombre= nombre
        self.__apellido= apellido
        self.__millasacum= millasacum

    def __str__(self):
        return('{} {} {} {} {}'.format(self.__numviajero, self.__dni, self.__nombre, self.__apellido, self.__millasacum))
    
    def __gt__(self,otro):
        if isinstance(otro, Viajero_Frecuente):
            return self.__millasacum < otro.__millasacum
        elif isinstance(otro, int):
            return self.__millasacum < otro
    
    def __add__(self, otro):
        if isinstance(otro, Viajero_Frecuente):
            return Viajero_Frecuente(self.__numviajero,self.__dni, self.__nombre, self.__apellido, self.__millasacum + otro.__millasacum)
        elif isinstance(otro, int):
            return Viajero_Frecuente(self.__numviajero,self.__dni, self.__nombre, self.__apellido, self.__millasacum + otro)
    
    def __radd__(self, otro):
        if type(self) == Viajero_Frecuente:
            return (otro + self.__millasacum)
        else:
            return (self.__millasacum + otro)
   
    def __sub__(self, otro):
        if isinstance(otro,Viajero_Frecuente):
            return Viajero_Frecuente(self.__numviajero,self.__dni, self.__nombre, self.__apellido, self.__millasacum - otro.__millasacum)
        elif isinstance(otro, int):
            return Viajero_Frecuente(self.__numviajero,self.__dni, self.__nombre, self.__apellido, self.__millasacum - otro)
   
    def __rsub__(self, otro):
        if type(self)==Viajero_Frecuente:
            return(otro - self.__millasacum)

    def __eq__(self, num):
        if type(self)== Viajero_Frecuente:
            return(self.__millasacum == num )  
        else: 
            return(num ==self.__millasacum)


    def mostrar(self):
        print("Nro:{}, DNI: {}, Nombre: {}, Apellido: {}, Millas: {}".format(self.__numviajero,self.__dni,self.__nombre,self.__apellido,self.__millasacum))
    

    def cantidadTotaldeMillas (self):
        return self.__millasacum
    
    def acumularMillas(self, cant):
         self.__millasacum += cant
         return self.__millasacum
    
    def canjearMillas(self, cant_canje):
       if cant_canje <= self.__millasacum:
           self.__millasacum -= cant_canje
           return self.__millasacum
       else: print("No se pudo realizar el canje \n")
   
    def getNumViajero(self):
        return self.__numviajero
    
    def getnombre(self):
        return self.__nombre