from claseplan import Plan_Ahorro
import csv

class Controlador:
    __lista=[]

    def __init__(self):
        self.__lista=[]
    
    def carga(self):
        archivo = open("planes.csv")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            plan= Plan_Ahorro(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5])
            self.__lista.append(plan)
        archivo.close()

    def actualizar_valor(self):
        for i in range(len(self.__lista)):
            self.__lista[i].mostrar()
            print("valor actual:{}".format(self.__lista[i].getvalor()))
            new_value= int(input("Ingrese nuevo valor del vehiculo:"))
            self.__lista[i].modificar_valor(new_value)
            print("El nuevo valor es:{}".format(self.__lista[i].getvalor()))

    def valor_inferior(self):
        low_value=int(input("Ingrese valor de cuota a comparar:"))
        bandera= False
        for i in range(len(self.__lista)):
            if low_value > self.__lista[i].getcuotas():
                self.__lista[i].mostrar()
                bandera=True
        if bandera == False: 
            print("No hay vehiculos con menos de {} cuotas".format(low_value))
    
    
    def licitaciones(self):
        #(cantidad de cuotas para licitar * importe de la cuota)
        for i in range(len(self.__lista)):
            v= self.__lista[i].cant_licitar() * self.__lista[i].valorcuota()
            print("El monto para licitar el vehiculo{} es: ${:.2f}".format(self.__lista[i].getversion(),v ))
    
    def getcodigo(self,cod):
        i=0
        while (i<len(self.__lista) and self.__lista[i].getcodigo() != int(cod)):
            i+=1
        return i
    
    def modificar_cuotas(self):
        cod=int(input("Ingrese codigo de un plan"))
        a=self.getcodigo(cod)
        new=int(input("ingrese nueva cantidad de cuotas para licitar:"))
        self.__lista[a].modificar(new)
        for i in range(len(self.__lista)):
            print("{}".format(self.__lista[i].cant_licitar()))
    