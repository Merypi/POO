def busca(numero, lista):
    indice= 0
    valorDeRetorno = 0
    bandera= False
    while not bandera and indice < len(lista):
        if numero == lista[indice].getNumViajero():
            bandera= True
            valorDeRetorno= indice
        else:
            indice +=1
    return valorDeRetorno
        
    
def menu_1(lista):
    numero = int(input("Ingrese el Numero de Viajero: \n"))
    pos= (busca(numero, lista))
    while pos !=-1:
         opcion = (input("A-Consultar Cantidad de Millas \n B- Acumular Millas \n C- Canjear Millas, finalizar con Opcion 0 \n"))
         if opcion == "A":
             print("El Viajero {} tiene una cantidad de millas acumuladas de: {}".format(lista[pos].getNumViajero(), lista[pos].cantidadTotaldeMillas()))
         elif opcion == "B":
                print ("\nLas millas que posee actualmente el viajero es: {}\n".format(lista[pos].acumularMillas(int(input("Ingrese la cantidad de millas para acumular:")))))
         elif opcion=="C":
                print ("\nLas millas que posee actualmente el viajero es: {}\n".format(lista[pos].canjearMillas(int(input("Ingrese la cantidad de millas a canjear:")))))
         elif opcion == "0":
             break
         else:
          print("Opción inválida. Intente nuevamente.")
          print("--FIN--")
          numero = int(input("Ingrese el Numero de Viajero: \n"))
          pos= (busca(numero, lista))
             
            
    


         
    
            
    