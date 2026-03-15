"""
Problema 3: Sistema de Navegación para Vehículo Autónomo
Sistema que planifica rutas, detecta obstáculos y ajusta velocidad.
"""


def leer_sensores():
    """
    Simula sensores de proximidad y cámaras.
    """
    return {
        "distancia_frontal": 4,
        "obstaculo_detectado": True
    }


def calcular_ruta_optima(origen, destino):
    """
    Genera una ruta simulada entre origen y destino.
    """
    return ["Avenida Central", "Calle 10", "Autopista Norte"]


def detectar_obstaculo(datos_sensor):
    """
    Determina si existe un obstáculo en la ruta.
    """
    return datos_sensor["distancia_frontal"] < 5 or datos_sensor["obstaculo_detectado"]


def ajustar_velocidad(trafico):
    """
    Ajusta velocidad según condiciones de tráfico.
    """
    if trafico == "alto":
        velocidad = 30
    elif trafico == "medio":
        velocidad = 50
    else:
        velocidad = 70

    print(f"Velocidad ajustada: {velocidad} km/h")


if __name__ == "__main__":

    sensores = leer_sensores()

    ruta = calcular_ruta_optima("Casa", "Trabajo")
    print("Ruta:", ruta)

    if detectar_obstaculo(sensores):
        print("Obstáculo detectado")

    ajustar_velocidad("medio")