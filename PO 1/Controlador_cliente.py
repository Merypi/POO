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
        band = False
        for fila in reader:
            if not band:
                band = True
            else:
                crear=Cliente(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6])
                self.__lista.append(crear)
        archivo.close()
# Leer un Dni de un cliente por teclado en informar los datos del cliente y todas las 
# reparaciones hechas al vehículo siguiendo el siguiente formato:


# Determinar el o los clientes que le hacen servicio a más de un vehículo, mostrando dni, 
# nombre, apellido, teléfono, patente y vehículo 
    def informadatos(self, dni,reparacion):
        i=0
        ban=False

        while(i<len(self.__lista)) & (ban==False):
            if self.__lista[i].getdni() == str(dni):
                ban=True
            else:
                i+=1
        if ban == True:
            print(f"DNI:{self.__lista[i].getdni():<20} Apellidos y nombre:{self.__lista[i].getAyN()} \nPatente:{self.__lista[i].getpatente():<20} Vehiculo:{self.__lista[i].getvehiculo()}")
            patente=self.__lista[i].getpatente()
            reparacion.mostrarReparaciones(patente)
            #print(f"Reparacion:{reparacion.getreparacion():<10} Precio repuesto:{rep.getpreciorepues():<10} Mano de obra:{rep.get_manoobra():<10} Subtotal:{rep.subtotal()}")

    def cambiarestado(self, patente):
        i=-1
        flag=False
        while not flag and i<len(self.__lista):
            i+=1
            flag=self.__lista[i].verifPatente(patente)

        if flag:
            self.__lista[i].EstadoTermnado()
            print("{} {} {}".format(self.__lista[i].getAyN(), self.__lista[i].gettelefono(), self.__lista[i].getvehiculo()))
        

    def sinfinalizar(self, reparacion:Manejador_reparacion):
        print("---Listado de clientes con reparaciones sin finalizar---")
        for i in range(len(self.__lista)):
            if self.__lista[i].getestado() == "P":
                print(f"{self.__lista[i].getAyN():<20} {self.__lista[i].gettelefono()} \n {self.__lista[i].getpatente():<20} {self.__lista[i].getvehiculo()}")
                reparacion.mostrarReparacionesPendientesPorPatente(self.__lista[i].getpatente())
                    

    def comparar(self):
        print("Clientes con más de un vehiculo")
        for i in range(0,len(self.__lista)-1):
            j=i+1
            while j<len(self.__lista):
                if self.__lista[i]== self.__lista[j]:
                     print("{} {} {} {} {}".format(self.__lista[i].getdni(), self.__lista[i].getAyN(), self.__lista[i].gettelefono(), self.__lista[i].getpatente(), self.__lista[i].getvehiculo()))
                j+=1

