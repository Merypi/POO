import csv
from manejador import manejador
from clasemenu import menu_1

if __name__ == "__main__":
    crear=manejador()
    instancia=crear.carga()
    menu_1(instancia) 
    print("Determinar el/los viajero/s con mayor cantidad de millas acumuladas")
    instancia.sort()
    for i in instancia:
        print (i)
    crear.funcion2_3()
    
    
