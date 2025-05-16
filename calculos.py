def calcular_propina(total, porcentaje):
    if total <= 0 or porcentaje <= 0:
        raise ValueError("El monto y el porcentaje deben ser mayores a 0")
    return total * (porcentaje / 100)

def calcular_total_con_propina(total, propina):
    if total <= 0 or propina < 0:  # Propina puede ser 0 si el cliente decide no dar propina
        raise ValueError("El monto debe ser mayor a 0 y la propina no puede ser negativa")
    return total + propina

def dividir_total(total, personas):
    if personas <= 0:
        raise ValueError("El número de personas debe ser mayor a 0")
    return total / personas