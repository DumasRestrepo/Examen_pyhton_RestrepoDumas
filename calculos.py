# Simulador de Propina

def calcular_propina (total, porcentaje):

    if total < 0 or porcentaje < 0:
        raise ValueError("El monto a pagar y la propina a dar debe ser mayor a 0")
    else:
        calcular_propina = total * (porcentaje / 100)
        return (f"La propina a dar es: {calcular_propina}")
    
def calcular_total_con_propina(total, propina):

    if total < 0 or propina < 0:
        raise ValueError("El monto a pagar y la propina a dar debe ser mayor a 0")
    else:
        calcular_total_con_propina = total + propina
        return  (f"El monto total a pagar es: {calcular_total_con_propina}")

def dividir_total(total, personas):

    personas = int(input("Ingrese la cantidad de personas que van a pagar: "))
    
    if personas < 0:
        raise ValueError("Ingrese un número mayor a 0")
    else:
        total_personas = total / personas
        return (f"El monto a pagar por persona es: {total_personas}")
    
