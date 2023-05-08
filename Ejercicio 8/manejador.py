from clase_conjunto import Conjunto

class manejador:
    __lista= []

    def __init__(self):
        self.__lista=[]

    def union(self):
        A=Conjunto([1,2,3,4])
        B=Conjunto([3,6,9])
        C = A + B
        print("Conjunto {} + {}= es igual a:{}".format(A, B, C) ,end=' ')

    def diferencia(slf):
        C=Conjunto([1,2,3,4])
        D=Conjunto([3,4,6,5])
        E= C - D
        print("Conjunto {} - {}= es igual a:{}".format(C, D, E) ,end=' ')

    def igualdad():
        A=Conjunto([1,2,3,4])
        B=Conjunto([1,2,3,4])
        if A == B:
            print("El conjunto A:{} es igual al conjunto B:{}".format(A, B))
        else:
            print("Los conjuntos no son iguales")
        
