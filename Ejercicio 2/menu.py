from viajero import Viajero_Frecuente

class Menu:
    __switcher={}
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.opcion3,
                            '4':self.salir,
                          }
    def getSwitcher(self):
        return self.__switcher

    #Obtener llamada a la opcion deseada, luego llamar a la funcion
    def opcion(self, op:int, v):
        func = self.__switcher.get(op)
        func(v)
    
    def salir(self):
        print('Salir')
          
    def opcion1(self,viajero):
        print("la cantidad de millas acumuladas es:{}".format(viajero.cantidadTotaldeMillas()))

    def opcion2(self, viajero):
        newmillas=int(input("ingrese la nueva cantidad de millas recorridas:"))
        viajero.acumularMillas(newmillas)
    
    def opcion3(self, viajero):
        change_millas=float(input("ingrese cantidad de millas que desea canjear:"))
        viajero.canjearmillas(change_millas)

        