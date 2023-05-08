from manejador import manejador

class Menu:
    __op= ""
    __lista= []

    def __init__(self, op=""):
        self.__op= op
        self.__lista= []

    def choose(self, op):
        if op == "1":
            manejador.union()
        elif op == "2":
            manejador.diferencia()
        elif op == "3":
            manejador.igualdad()