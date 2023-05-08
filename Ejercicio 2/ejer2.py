
from viajero import Viajero_Frecuente
from menu import Menu   +
from manejadorviajero import controladorviajero

if __name__ == '__main__':
    #Item 1: Cargar una lista con los viajeros del archivo
    crear=controladorviajero()
    crear.cargararchivos()
    crear.mostrar()
    #Item 2:El usuario ingresa por teclado un número de viajero frecuente, el sistema presenta un menú 
    viajero=int(input("ingrese numero de viajero a buscar:"))
    v=crear.bucarviajeros(viajero)
    menu = Menu()
    salir = False
    while not salir:
        print("----------------Menu----------------")
        print("-1. Consultar cantidad de millas")
        print("-2. Acumular millas")
        print("-3. Canjear millas")
        print("-0. Salir")
        print("----------------Fin----------------")
        op = int(input("Que opcion elige: "))
        if op!=0:
            menu.opcion(op, v)
        else:
            salir=True
            print("Fin del programas")
        salir = op == 0
    

