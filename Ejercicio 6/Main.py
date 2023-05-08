import csv
from manejador import manejador
from clasemenu import menu_1

if __name__ == "__main__":
    crear=manejador()
    instancia=crear.carga()
    #menu_1(instancia) 
    #print("Determinar el/los viajero/s con mayor cantidad de millas acumuladas")
    instancia.sort()
    """for i in instancia:
        print (i)"""
    crear.funcion2_3()
    crear.comparacion()
    crear.acumulaporderecha()
    crear.canjeporderecha()
    
    
'''1-    Comparar las cantidad de millas acumuladas de un viajero frecuente con un valor entero a través de la sobrecarga del operador igual (== o __eq__). 
Por ejemplo, sea v una instancia de la clase ViajeroFrecuente, debe ser posible realizar tanto v ==  100 como 100 == v.

2-    Acumular millas se pueda resolver de la siguiente forma: sea v una instancia de la clase ViajeroFrecuente, debe ser posible realizar v =  100 + v.

3-    Canjear millas se pueda resolver de la siguiente forma: sea v una instancia de la clase ViajeroFrecuente, debe ser posible realizar v =  100 - v.'''