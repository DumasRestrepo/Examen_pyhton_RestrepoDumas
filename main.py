from interfaz import menu_calcular_propina, menu_dividir_total, menu_salir

def main():
    
    while True:
        print("\n=============================================")
        print(" -----------SIMULADOR DE PROPINA----------- ")
        print("=============================================")
        print('''\n1. Calcular propina y total a pagar\n2. Calcular total a pagar dividido entre varias personas\n3. Salir''')
        print("=============================================")
        
        opcion = input("Seleccione una opción (1-3): ")
        
        if opcion == "1":
            menu_calcular_propina()
        elif opcion == "2":
            menu_dividir_total()
        elif opcion == "3":
            menu_salir()
            break  # Salir del bucle while
        else:
            print("Opción inválida. Por favor ingrese 1, 2 o 3.")

main()