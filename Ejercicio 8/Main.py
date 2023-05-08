from Menu import Menu

if __name__ == "__main__":
    crear = Menu()
    print("---MENU DE OPCIONES---")
    print("1:Unir dos conjuntos")
    print("2: diferencia entre dos conjuntos")
    print("3: Igualdad de conjuntos")
    opcion = input("ingrese opcion:")
    crear.choose(opcion)