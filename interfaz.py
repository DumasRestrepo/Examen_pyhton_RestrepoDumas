from calculos import calcular_propina, calcular_total_con_propina, dividir_total

def menu_calcular_propina():

    while True:

        print("============================================")
        print("\n-------------Cálculo de Propina-------------")
        print("\n============================================")
        total = float(input("\nIngrese el monto total de la cuenta: $"))
        porcentaje = int(input("Ingrese el porcentaje de propina (por ejemplo: 15):  %"))
        print("\n============================================")
        calcular_propina1 = calcular_propina(total, porcentaje)
        print(f"La propina calculada es: ${calcular_propina1}")
        calcular_total_con_propina1 = calcular_total_con_propina(total, calcular_propina1)
        print(f"El total a pagar es: {calcular_total_con_propina1}")
        print("\n============================================\n")
        repetir = input("¿Deseas calcular nuevamente? (S/N): ").upper()

        if repetir == "S":
            print("Recalculando")
        elif repetir == "N":
            menu_salir()
        else:
            print("Opción no válida")

def menu_dividir_total():

    while True:

        print("============================================")
        print("\n---Dividir Cuenta entre Varias Personas---")
        print("\n============================================")
        total = float(input("\nIngrese el monto total de la cuenta: $"))
        porcentaje = int(input("Ingrese el porcentaje de propina (por ejemplo: 15):  %"))
        personas = int(input("Ingrese el número de personas: "))
        print("\n============================================")
        calcular_propina2 = calcular_propina(total, porcentaje)
        calcular_total_con_propina2 = calcular_total_con_propina(total, calcular_propina2)
        dividir_total1 = dividir_total(total, personas)
        print(f"La propina calculada es: ${calcular_propina2}")
        print(f"El total a pagar es: ${calcular_total_con_propina2}")
        print(f"Monto por persona: ${dividir_total1}")
        print("\n============================================\n")
        repetir = input("¿Deseas calcular nuevamente? (S/N): ").upper()

        if repetir == "S":
            print("Recalculando")
        elif repetir == "N":
            menu_salir()
        else:
            print("Opción no válida")
            

def menu_salir():
    print("============================================")
    print("-¡Gracias por usar el Simulador de Propina!-")
    print("============================================")