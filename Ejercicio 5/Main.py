from controlador import Controlador

if __name__ == "__main__":
    crear = Controlador()
    crear.carga()
    print("---Menu de opciones---")
    print("1: Actualizar valor de vehiculo de cada plan")
    print("2:Ingresar valor de cuota para mostrar vehiculos con cuotas inferiores")
    print("3:Monto que se debe haber pagado para licitar el vehículo")
    print("4: Ingrese codigo para modificar cuotas para licitar")
    op=input("ingrese opcion de menu:")
    
    while op != "0":
        if op == "1":
            crear.actualizar_valor()
        elif op == "2":
            crear.valor_inferior()
        elif op=="3":
            crear.licitaciones()
        elif op=="4":
            crear.modificar_cuotas()
        op=input("ingrese opcion de menu:")
