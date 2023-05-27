from clasereparacion import Reparacion
import csv

class Manejador_reparacion:
    __lista= []

    def __init__(self):
        self.__lista=[]

    def carga(self):
        archivo= open("reparaciones.csv")
        reader= csv.reader(archivo, delimiter=";")
        band = False
        for fila in reader:
            if not band:
                band = True
            else:
                crear=Reparacion(fila[0], fila[1], fila[2], fila[3], fila[4])
                self.__lista.append(crear)
        
    # def getvehiculo(self, patente):
    #     i=0
    #     repacion=None
    #     while i<len(self.__lista) and repacion==None:
    #         if self.__lista[i].getpatente() == str(patente):
    #             repacion=self.__lista[i]
    #         i+=1
    #     return repacion
    
    def mostrarReparaciones(self,pat):
        total=0
        print("Reparación:                  Precio repuesto:        Mano de obra:       Subtotal:")
        for rep in self.__lista:
            if rep.coincide(pat):
                print(f"{rep.getreparacion():<10} {rep.getpreciorepues():<10} {rep.get_manoobra():<10} {rep.subtotal()} ")
                total+=rep.subtotal()
        print("total: ",total)

    def PagoTotal(self,pat):
        total=0
        for rep in self.__lista:
            if rep.coincide(pat):
                total+=rep.subtotal()
        print("total: $",total)

    def verifReparaciones(self,patente):
        coincidencias=0
        terminados=0
        retorno=False
        for rep in  self.__lista:   #range(len(self.__lista)):
            if rep.getpatente() == str(patente):
                coincidencias+=1
                if rep.getestado() == "T":
                    terminados+=1

        if coincidencias == terminados:#Todas las reparaciones estan terminadas
            retorno=True
        return retorno
    
    def mostrarReparacionesPendientesPorPatente(self, patente):
        print("Reparaciones: ")
        for reparacion in self.__lista:
            if reparacion.getpatente() == patente and reparacion.getestado() == "P":
                print("-",reparacion.getreparacion())
        print("\n")    
        

    
