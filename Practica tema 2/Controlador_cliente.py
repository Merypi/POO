from clasecliente import Cliente
import csv
from Controlador_reparacion import Manejador_reparacion

class Manejador_Cliente:
    __lista= []

    def __init__(self):
        self.__lista=[]

    def carga(self):
        archivo= open("clientes.csv")
        reader= csv.reader(archivo, delimiter=";")
        
        for fila in reader:
            crear=Cliente(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5],fila[6])
            self.__lista.append(crear)
        archivo.close()

    def informadatos(self, dni,reparacion:Manejador_reparacion):
        j=0
        ban=False

        # while(j<len(self.__lista)) & (ban==False):
        #     if self.__lista[j].getdni() == str(dni):
        #         ban=True
        #         i = j
        #     j += 1
        for i in     
        
        if ban == True:
            print(f"DNI:{self.__lista[i].getdni() :<20} Apellidos y nombre:{self.__lista[i].getAyN()} \n Patente:{self.__lista[i].getpatente() :<20} Vehiculo:{self.__lista[i].getvehiculo()}")
            #print(f"{self.__lista[i].getdni() :<20} {alCon.getAlumno(self.__lista[i].getdni()).getAyN():<30} {self.__lista[i].getfecha():<15} {self.__lista[i].getnota():<4} {alCon.getAlumno(self.__lista[i].getdni()).getcursado()}")
            print(f"Reparacion:{reparacion.getvehiculo(self.__lista[i].getpatente()).getreparacion():<10} Precio repuesto:{reparacion.getvehiculo(self.__lista[i].getpatente()).getpreciorepues():<10} Mano de obra:{reparacion.getvehiculo(self.__lista[i].getpatente()).get_manoobra():<10} Subtotal:{reparacion.getvehiculo(self.__lista[i].getpatente()).subtotal()}")


    def cambiarestado(self, patente, reparacion:Manejador_reparacion):
        c=0
        j=0
        for i in range(len(self.__lista)):
            if self.__lista[i].getpatente() == str(patente):
                j=0
                if reparacion.getvehiculo(self.__lista[i].getpatente()).getestado() == "T":
                    c=+1

        if c == j:#Todas las reparaciones estan terminadas
            print("{} {} {} {}".format(self.__lista.getAyN(), self.__lista().gettelefono(), self.__lista.getvehiculo(),))

    def sinfinalizar(self, reparacion:Manejador_reparacion):
        for i in range(len(self.__lista)):
            if reparacion.getvehiculo(self.__lista[i].getpatente()).getestado() == "P":
                print(f"{self.__lista[i].getAyN():<20} {self.__lista[i].gettelefono()} \n {self.__lista[i].getpatente():<20} {self.__lista[i].getvehiculo()}\n {reparacion.getvehiculo(self.__lista[i].getpatente()).getreparacion()}" )

    def comparar(self):
        a=self.__lista[0]
        for i in range(len(self.__lista)):
            if a == self.__lista[i+1]:
                a=self.__lista[i+1]
                print("{} {} {} {} {}".format(self.__lista[i].getdni(), self.__lista[i].getAyN(), self.__lista[i].gettelefono(), self.__lista[i].getpatente(), self.__lista[i].getvehiculo()))