import csv
from viajero import Viajero_Frecuente

class controladorviajero:
    __listaviajeros=[]

    def __init__(self):
        self.__listaviajeros=[]

    def cargararchivos(self):
        archivo=open("file.csv")
        reader=csv.reader(archivo,delimiter=',')
        for persona in reader:
            viajero=Viajero_Frecuente(persona[0], persona[1], persona[2], persona[3], persona[4])
            self.__listaviajeros.append(viajero)
    
    def mostrar(self):
        for i in range(len(self.__listaviajeros)):
            print(self.__listaviajeros[i])

    def bucarviajeros(self, num:int):
        flag=False
        c=0
        retorno= None
        while (c<len(self.__listaviajeros)) & (flag==False):
            if num == self.__listaviajeros[c].getviajero():
                flag = True
                j = c
            c += 1
       # if flag == False:
       #    print("El numero de pasajero no se pudo encontrar")
        if flag == True:
            #print("viajero encontrado:{}".format(self.__listaviajeros[j]))
            retorno = self.__listaviajeros[j]
        return(retorno)
