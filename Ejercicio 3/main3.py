import csv
from claseregistro import Registro
def menu():  
    print("")
    print("--------------------------MENU--------------------------")
    print("Seleccione la opcion deseada")
    print("Para ver la menor entrada de cada variable presione 1 ")
    print("Para ver la temperatura promedio mensual por hora presione 2")
    print("Para ver los tres valores de un dia seleccionado presione 3")
    print("Para finalizar el programa presione 0")
    print("--------------------------------------------------------")
    print("")
    o=int(input("Seleccione la opcion seleccionada:  "))
    return(o)

def menormayor(l):
        min=9999
        max=0
        d=0
        h=0
        for i in range(30):
             for j in range(24):
                if(type(l[i][j])== Registro):
                    c=l[i][j].getpres()
                    if(c<min):
                        
                        min=c
                        d=i
                        h=j
        print("La menor presion registrada de {} pascales se dio el dia {} a las {} horas".format(min,d+1,h))
        for i in range(30):
             for j in range(24):
                if(type(l[i][j])== Registro):
                    c=l[i][j].getpres()
                    if(c>max):
                        
                        max=c
                        d=i
                        h=j
        print("La mayor presion registrada de {} pascales se dio el dia {} a las {} horas".format(max,d+1,h))
        min=9999
        max=0
        for i in range(30):
             for j in range(24):
                if(type(l[i][j])== Registro):
                    c=float(l[i][j].gettemp())
                    if(c<min):
                        
                        min=c
                        d=i
                        h=j
        print("La menor temperatura registrada de {} grados celsius se dio el dia {} a las {} horas".format(min,d+1,h))
        for i in range(30):
             for j in range(24):
                if(type(l[i][j])== Registro):
                    c=float(l[i][j].gettemp())
                    if(c>max):
                        
                        max=c
                        d=i
                        h=j
        print("La mayor temperatura registrada de {} grados celsius se dio el dia {} a las {} horas".format(max,d+1,h))
        min=9999
        max=0
        for i in range(30):
             for j in range(24):
                if(type(l[i][j])== Registro):
                    c=l[i][j].gethum()
                    if(c<min):
                        
                        min=c
                        d=i
                        h=j
        print("La menor humedad registrada de {} g / m³ se dio el dia {} a las {} horas".format(min,d+1,h))
        for i in range(30):
             for j in range(24):
                if(type(l[i][j])== Registro):
                    c=l[i][j].gethum()
                    if(c>max):
                        
                        max=c
                        d=i
                        h=j
        print("La mayor humedad registrada de {} g / m³ se dio el dia {} a las {} horas".format(max,d+1,h))

def temppromhora(l):
    for j in range(24):
        acum=0
        cont=0
        for i in range(30):
            if(type(l[i][j])== Registro):
                acum+=float(l[i][j].gettemp())
                cont+=1
        print("El promedio de temperatura a las {} horas es de {} grados ".format(j,acum/cont))        


def variablesdia(l,ds):
    print("Hora Temperatura  Humedad  Presion" )
    for i in range(24):
       
        print(" {}         {}".format(i,l[ds][i]))


        
if __name__ == '__main__':
    
    matriz=[]
    dia=30
    hora=24
    
    for i in range(dia):
        lista=[]
        for j in range (hora):
            lista.append(j)
        # print(lista)
        matriz.append(lista)
    

    # for i in range(dia):
    #     matriz.append([0]*hora)

    archivo=open("datos3.csv")
    reader=csv.reader(archivo, delimiter=";")
    next(reader)

    for fila in reader:
        dia=int(fila[0])
        hora=int(fila[1])
        temp= float(fila[2])
        hum= int(fila[3])
        pres= int(fila[4])
        matriz[dia-1][hora]=Registro(float(temp), int(hum), int(pres))

    archivo.close()
   
    # for i in range(dia):
    #     for j in range(hora):
    #         print(matriz[i][j])
   
    
    opc=menu()

    while(int(opc)!= 0):
        if(opc==1):
            print("")
            print(">>>Opcion 1 seleccionada")
            menormayor(matriz)

        if(opc==2):
            print("")
            print(">>>Opcion 2 seleccionada")
            temppromhora(matriz)
        if(opc==3):
            print("")
            print(">>>Opcion 3 seleccionada")
            dias=int(input("Escriba el dia del que quiere averiguar las variables: "))
            variablesdia(matriz,dias)
        opc=menu()
    
    print(">>>Finalizando proceso")
    
   
