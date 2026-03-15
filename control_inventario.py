"""
Problema 2: Gestión de Inventario en un Almacén
Sistema que controla entradas, salidas y alertas de reabastecimiento.
"""

inventario = {}


def registrar_entrada(producto, cantidad):
    """
    Registra la entrada de productos al inventario.
    """
    inventario[producto] = inventario.get(producto, 0) + cantidad


def registrar_salida(producto, cantidad):
    """
    Registra la salida de productos del inventario.
    """
    if inventario.get(producto, 0) >= cantidad:
        inventario[producto] -= cantidad
    else:
        print("Stock insuficiente")


def calcular_nivel_optimo(producto):
    """
    Define un nivel mínimo recomendado de inventario.
    """
    return 20


def generar_alerta(producto):
    """
    Genera alerta si el inventario está por debajo del nivel óptimo.
    """
    if inventario.get(producto, 0) < calcular_nivel_optimo(producto):
        print(f"⚠ Reabastecer {producto}")


if __name__ == "__main__":

    registrar_entrada("tornillos", 50)
    registrar_salida("tornillos", 35)
    generar_alerta("tornillos")

    print(inventario)