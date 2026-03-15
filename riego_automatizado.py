"""
Problema 5: Sistema de Riego Automatizado
Sistema que optimiza el uso del agua según humedad del suelo y clima.
"""


def leer_humedad():
    """
    Simula sensores de humedad del suelo.
    """
    return {
        "zona1": 25,
        "zona2": 40,
        "zona3": 30
    }


def consultar_clima():
    """
    Simula consulta meteorológica.
    """
    return "soleado"


def calcular_riego(humedad, clima):
    """
    Determina cantidad de agua necesaria.
    """
    if clima == "lluvia":
        return 0

    if humedad < 30:
        return 20
    elif humedad < 40:
        return 10
    else:
        return 0


def controlar_valvula(zona, agua):
    """
    Abre o cierra válvula de riego.
    """
    if agua > 0:
        print(f"Regar {zona} con {agua} litros")
    else:
        print(f"No regar {zona}")


if __name__ == "__main__":

    humedad = leer_humedad()
    clima = consultar_clima()

    for zona, valor in humedad.items():
        agua = calcular_riego(valor, clima)
        controlar_valvula(zona, agua)