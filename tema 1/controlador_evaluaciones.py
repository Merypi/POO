import csv
from clase_evaluacion import Evaluacion

class Controlador_Evaluaciones:
    __lista= []

    def __init__(self):
        self.__lista=[]

    def carga(self):
        archivo= open("evaluacion.csv")
        reader= csv.reader(archivo, delimiter=";")
        for fila in reader:
            crear=Evaluacion(fila[0], fila[1], fila[2], fila[3], fila[4])
            self.__lista.append(crear)
        archivo.close()

    def listarPorEstilo(self, estilo, federados, edad):
        print("Patinadores que participaron en el estilo", estilo)
        for est in self.__lista:
            if est.getestilo() == estilo:
                dni=est.getdni()
                federados.listar(edad, dni)
   
    def mayorPuntaje(self, federados):
        mayor=self.__lista[0]
        for i in range (len(self.__lista)-1):
            t = self.__lista[i+1]
            if (t > mayor):
                mayor = t
                dniganador = self.__lista[i].getdni()
                estilo= self.__lista[i].getestilo()
        federados.MostrarMejPuntaje(dniganador, estilo)

    def ambosEstilos(self, dni):
        c=0
        for i in self.__lista:
            if dni == i.getdni():
                c += 1
        if c == 2:
            return c 
        
    def valoracionPorJueces(self, dni, estilo):
        i=0
        Flag=False
        while i<len(self.__lista) and not Flag:
            if (self.__lista[i].getdni() == dni) and (self.__lista[i].getestilo() == estilo):
                Flag=True
            i +=1
        if Flag==True:
           print(self.__lista[i-1].getPuntajeJueces())