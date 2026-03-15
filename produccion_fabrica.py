"""
Problema 4: Optimización de Producción en una Fábrica
Sistema que monitorea máquinas y ajusta producción.
"""


def monitorear_maquinas():
    """
    Retorna estado de las máquinas.
    """
    return {
        "maquina1": "operativa",
        "maquina2": "mantenimiento",
        "maquina3": "operativa"
    }


def planificar_mantenimiento(maquinas):
    """
    Detecta máquinas que requieren mantenimiento.
    """
    for maquina, estado in maquinas.items():
        if estado == "mantenimiento":
            print(f"Programar mantenimiento para {maquina}")


def analizar_rendimiento(unidades, horas):
    """
    Calcula eficiencia de producción.
    """
    return unidades / horas


def ajustar_produccion(demanda):
    """
    Ajusta programación de producción según demanda.
    """
    if demanda > 1000:
        print("Aumentar producción")
    elif demanda < 300:
        print("Reducir producción")
    else:
        print("Producción estable")


if __name__ == "__main__":

    maquinas = monitorear_maquinas()
    planificar_mantenimiento(maquinas)

    eficiencia = analizar_rendimiento(500, 8)
    print("Eficiencia:", eficiencia)

    ajustar_produccion(1200)