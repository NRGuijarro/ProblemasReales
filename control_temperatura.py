"""
Problema 1: Control de Temperatura en un Edificio Inteligente
Sistema que ajusta la temperatura según sensores, hora, ocupación y clima.
"""

# Función para leer sensores
def leer_sensores_temperatura():
    """
    Simula la lectura de sensores en distintas zonas del edificio.
    Retorna un diccionario con temperaturas actuales.
    """
    return {
        "oficina": 25,
        "sala_reuniones": 27,
        "recepcion": 23
    }


# Función para calcular temperatura óptima
def calcular_temperatura_optima(hora, ocupacion, clima):
    """
    Calcula la temperatura ideal según hora del día, ocupación y clima externo.
    """
    temp_base = 22

    if clima == "calor":
        temp_base -= 1
    elif clima == "frio":
        temp_base += 1

    if ocupacion > 20:
        temp_base -= 1

    if hora >= 18:
        temp_base -= 1

    return temp_base


# Procedimiento para ajustar climatización
def ajustar_climatizacion(zona, temp_actual, temp_optima):
    """
    Envía señal al sistema HVAC para ajustar temperatura.
    """
    if temp_actual < temp_optima:
        print(f"{zona}: Activar calefacción")
    elif temp_actual > temp_optima:
        print(f"{zona}: Activar refrigeración")
    else:
        print(f"{zona}: Temperatura correcta")


# Función para registrar consumo energético
def registrar_consumo(consumo, historial):
    """
    Guarda consumo energético y calcula promedio.
    """
    historial.append(consumo)
    return sum(historial) / len(historial)


# Ejecución de prueba
if __name__ == "__main__":

    sensores = leer_sensores_temperatura()
    temp_optima = calcular_temperatura_optima(14, 15, "calor")

    for zona, temp in sensores.items():
        ajustar_climatizacion(zona, temp, temp_optima)