from Controlador_federados import Controlador_Federados
from controlador_evaluaciones import Controlador_Evaluaciones
if __name__ == '__main__':
    federados= Controlador_Federados()
    federados.carga()
    evaluacion=Controlador_Evaluaciones()
    evaluacion.carga()
    print("---Menu de opciones---")
    print("1:Listar patinador de acuerdo al estilo dado")
    print("2:Patinador con mayor puntaje")
    print("3:Patinadores en ambos estilos")
    print("4:Mostrar las valoraciones de los jueces a partir de un dni ingresado:")
    op=input("Ingrese opcion de menu:")
    
    while op !="0":
        if op == "1":
            estilo=input("Ingrese un estilo:")
            edad=input("ingrese edad:")
            evaluacion.listarPorEstilo(estilo, federados, edad)
        elif op == "2":
            evaluacion.mayorPuntaje(federados)
        elif op=="3":
            #Listar los datos de los patinadores que participaron en estilo libre y en escuela. 
            print("---Patinadores que participaron en dos estilos---")
            federados.AmbosEstilos(evaluacion)
        elif op=="4":
            #Dado el DNI de un inscripto y un estilo, mostrar las 3 valoraciones dadas por los jueces.
            dni=input("Ingrese dni:")
            estilo2=input("Ingrese estilo:")
            evaluacion.valoracionPorJueces(dni, estilo2)
        op=input("Ingrese opcion de menu")