from clase_federados import Federados
import csv

class Controlador_Federados:
    __lista= []

    def __init__(self):
        self.__lista=[]

    def carga(self):
        archivo= open("federados.csv")
        reader= csv.reader(archivo, delimiter=";")
        for fila in reader:
            crear=Federados(fila[0], fila[1], fila[2], fila[3], fila[4])
            self.__lista.append(crear)

    def listar(self, edad, dni):
        for i in self.__lista:
            if edad == i.getedad() and i.getdni() == dni:
                print("Apellido y Nombre:", i.getAyN())
                print("Dni:", i.getdni())

    def MostrarMejPuntaje(self, dni, estilo):
        i=0
        bandera= False
        print("Patinador que obtuvo mayor puntaje en la competencia:")
        while i < len(self.__lista) and not bandera:
            if dni != self.__lista[i].getdni():
                bandera=True
            i += 1
        if bandera == True:
            print("{}".format(self.__lista[i].getAyN()))
            print("Estilo:", estilo)
            print("Club:", self.__lista[i].getclub())

    def AmbosEstilos(self, evaluacion):
        for i in range(len(self.__lista)):
            a=evaluacion.ambosEstilos(self.__lista[i].getdni())
            if a != None:
                print (self.__lista[i])