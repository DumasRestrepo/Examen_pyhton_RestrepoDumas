from interfaz import menu_calcular_propina, menu_dividir_total, menu_salir

def main():
        
    while True:
        print("\n=============================================")
        print(" -----------SIMULADOR DE PROPINA----------- ")
        print("=============================================")
        print('''\n1. Calcular propina y total a pagar\n2.Calcular total a pagar divido entre varias personas\n3.Salir''')
        print("=============================================")
        print("\nPor favor, elige una opción (1-3)\n")

        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            menu_calcular_propina()
        elif opcion == "2":
            menu_dividir_total()
        elif opcion == "3":
            menu_salir()
        else:
            print("Opción inválida")

main()