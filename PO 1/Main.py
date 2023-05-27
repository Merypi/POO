from Controlador_reparacion import Manejador_reparacion
from Controlador_cliente import Manejador_Cliente

if __name__ == "__main__":
    reparacion= Manejador_reparacion()
    reparacion.carga()
    cliente=Manejador_Cliente()
    cliente.carga()

    print("---Menu de opciones---")
    print("1:Informar los datos del cliente y todas las reparaciones hechas al vehículo")
    print("2:determinar si todas las reparaciones están terminadas")
    print("3:clientes con reparaciones sin terminar")
    print("4:Verificar si hay clientes con mas de dos vehiculos")

    op=input("ingrese opcion de menu: ")
    while op != "0":
        if op=="1":
            dni=input("ingrese dni para buscar datos del cliente: ")
            cliente.informadatos(dni,reparacion)
        elif op=="2":
            # Leer una patente por teclado, determinar si todas las reparaciones están terminadas, 
            # en caso afirmativo, cambiar el estado en el Cliente, y mostrar nombre y apellido del 
            # cliente, el teléfono, el vehículo y el total a pagar.
            paten=input("ingresar numero de patente: ")
            flag=reparacion.verifReparaciones(paten)
            if flag:
                cliente.cambiarestado(paten)
                reparacion.PagoTotal(paten)
            else:
                print("---Las reparaciones todavía no estan terminadas---")
        elif op=="3":
            cliente.sinfinalizar(reparacion)
        elif op=="4":
            cliente.comparar()

        op=input("ingrese opcion de menu:")
