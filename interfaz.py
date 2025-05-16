from calculos import calcular_propina, calcular_total_con_propina, dividir_total

def menu_calcular_propina():
    while True:
        print("\n============================================")
        print("-------------Cálculo de Propina-------------")
        print("============================================")
        
        try:
            total = float(input("\nIngrese el monto total de la cuenta: ","$"))
            porcentaje = int(input("Ingrese el porcentaje de propina (ej: 15): ","%"))
            
            propina = calcular_propina(total, porcentaje)
            total_con_propina = calcular_total_con_propina(total, propina)
            
            print("\n============================================")
            print(f"La propina calculada es: ${propina:.2f}")
            print(f"El total a pagar es: ${total_con_propina:.2f}")
            print("============================================")
            
            repetir = input("\n¿Deseas calcular nuevamente? (S/N): ").upper()
            if repetir != "S":
                break
                
        except ValueError as e:
            print(f"\nError: {e}")
            print("Por favor ingrese valores válidos.")

def menu_dividir_total():
    while True:
        print("\n============================================")
        print("---Dividir Cuenta entre Varias Personas---")
        print("============================================")
        
        try:
            total = float(input("\nIngrese el monto total de la cuenta: ","$"))
            porcentaje = int(input("Ingrese el porcentaje de propina (ej: 15): ","%"))
            personas = int(input("Ingrese el número de personas: "))
            
            propina = calcular_propina(total, porcentaje)
            total_con_propina = calcular_total_con_propina(total, propina)
            monto_por_persona = dividir_total(total_con_propina, personas)
            
            print("\n============================================")
            print(f"La propina calculada es: ${propina:.2f}")
            print(f"El total a pagar es: ${total_con_propina:.2f}")
            print(f"Monto por persona: ${monto_por_persona:.2f}")
            print("============================================")
            
            repetir = input("\n¿Deseas calcular nuevamente? (S/N): ").upper()
            if repetir != "S":
                break
                
        except ValueError as e:
            print(f"\nError: {e}")
            print("Por favor ingrese valores válidos.")

def menu_salir():
    print("\n============================================")
    print("-¡Gracias por usar el Simulador de Propina!-")
    print("============================================")