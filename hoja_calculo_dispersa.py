"""
PROBLEMA 4: Implementación de una Hoja de Cálculo Dispersa
==========================================================

Una hoja de cálculo dispersa (sparse spreadsheet) es una representación
eficiente de una matriz que contiene muchas celdas vacías. En lugar de
almacenar todas las celdas, solo se almacenan aquellas con valores.

Estructura: Dos listas enlazadas
- Una lista de filas
- Cada fila contiene una lista enlazada de celdas no vacías

Esta implementación es mucho más eficiente en memoria que una matriz
completa cuando la mayoría de celdas están vacías.

Operaciones:
- Insertar/actualizar valores
- Obtener valores de celdas
- Eliminar valores
- Operaciones en rangos (suma, promedio)
- Insertar/eliminar filas y columnas
- Guardar/cargar desde archivos
- Mostrar en forma tabular
"""

import json
import os
from typing import Optional, Tuple, List, Dict

class Celda:
    """Representa una celda en la hoja de cálculo"""
    def __init__(self, fila: int, columna: int, valor):
        self.fila = fila
        self.columna = columna
        self.valor = valor
        self.siguiente = None

    def __repr__(self):
        return f"({self.fila},{self.columna})={self.valor}"

class FilaEnlazada:
    """Representa una fila con sus celdas no vacías"""
    def __init__(self, numero_fila: int):
        self.numero_fila = numero_fila
        self.cabeza_celda = None  # Lista de celdas en esta fila
        self.siguiente_fila = None  # Siguiente fila no vacía

class HojaCalculoDispersа:
    """
    Hoja de cálculo dispersa implementada con dos listas enlazadas:
    principales para las filas, cada fila es una lista de celdas.
    """
    def __init__(self, nombre: str = "Hoja1"):
        self.nombre = nombre
        self.cabeza_fila = None  # Primera fila con datos
        self.max_fila = 0
        self.max_columna = 0

    def insertar_valor(self, fila: int, columna: int, valor):
        """
        Inserta o actualiza un valor en una celda específica.
        Si el valor es None o 0, se considera como vacío.
        """
        if valor is None or (isinstance(valor, (int, float)) and valor == 0):
            self.eliminar_valor(fila, columna)
            return

        # Actualizar máximos
        self.max_fila = max(self.max_fila, fila)
        self.max_columna = max(self.max_columna, columna)

        # Si no hay filas
        if self.cabeza_fila is None:
            self.cabeza_fila = FilaEnlazada(fila)
            self.cabeza_fila.cabeza_celda = Celda(fila, columna, valor)
            return

        # Buscar fila o crearla
        if self.cabeza_fila.numero_fila == fila:
            fila_actual = self.cabeza_fila
        elif self.cabeza_fila.numero_fila > fila:
            # Insertar nueva fila al principio
            nueva_fila = FilaEnlazada(fila)
            nueva_fila.siguiente_fila = self.cabeza_fila
            self.cabeza_fila = nueva_fila
            nueva_fila.cabeza_celda = Celda(fila, columna, valor)
            return
        else:
            # Buscar posición correcta
            fila_actual = self.cabeza_fila
            fila_encontrada = False

            while fila_actual.siguiente_fila:
                if fila_actual.siguiente_fila.numero_fila == fila:
                    fila_actual = fila_actual.siguiente_fila
                    fila_encontrada = True
                    break
                elif fila_actual.siguiente_fila.numero_fila > fila:
                    # Insertar nueva fila
                    nueva_fila = FilaEnlazada(fila)
                    nueva_fila.siguiente_fila = fila_actual.siguiente_fila
                    fila_actual.siguiente_fila = nueva_fila
                    nueva_fila.cabeza_celda = Celda(fila, columna, valor)
                    return
                fila_actual = fila_actual.siguiente_fila

            if not fila_encontrada:
                # Crear nueva fila al final
                nueva_fila = FilaEnlazada(fila)
                fila_actual.siguiente_fila = nueva_fila
                nueva_fila.cabeza_celda = Celda(fila, columna, valor)
                return

        # Ahora insertar/actualizar celda en la fila encontrada
        celda_actual = fila_actual.cabeza_celda

        if celda_actual is None:
            fila_actual.cabeza_celda = Celda(fila, columna, valor)
            return

        # Buscar posición correcta
        if celda_actual.columna == columna:
            celda_actual.valor = valor
            return
        elif celda_actual.columna > columna:
            # Insertar al principio
            nueva_celda = Celda(fila, columna, valor)
            nueva_celda.siguiente = celda_actual
            fila_actual.cabeza_celda = nueva_celda
            return

        # Buscar en el resto
        while celda_actual.siguiente:
            if celda_actual.siguiente.columna == columna:
                celda_actual.siguiente.valor = valor
                return
            elif celda_actual.siguiente.columna > columna:
                # Insertar
                nueva_celda = Celda(fila, columna, valor)
                nueva_celda.siguiente = celda_actual.siguiente
                celda_actual.siguiente = nueva_celda
                return
            celda_actual = celda_actual.siguiente

        # Insertar al final
        nueva_celda = Celda(fila, columna, valor)
        celda_actual.siguiente = nueva_celda

    def obtener_valor(self, fila: int, columna: int):
        """Obtiene el valor de una celda específica"""
        fila_actual = self.cabeza_fila

        while fila_actual:
            if fila_actual.numero_fila == fila:
                # Buscar celda en la fila
                celda_actual = fila_actual.cabeza_celda

                while celda_actual:
                    if celda_actual.columna == columna:
                        return celda_actual.valor
                    celda_actual = celda_actual.siguiente
                return 0  # No encontrada, retorna 0
            
            fila_actual = fila_actual.siguiente_fila

        return 0  # Fila no encontrada

    def eliminar_valor(self, fila: int, columna: int) -> bool:
        """Elimina el valor de una celda específica"""
        fila_actual = self.cabeza_fila
        fila_anterior = None

        while fila_actual:
            if fila_actual.numero_fila == fila:
                # Buscar y eliminar celda
                celda_actual = fila_actual.cabeza_celda
                celda_anterior = None

                while celda_actual:
                    if celda_actual.columna == columna:
                        if celda_anterior:
                            celda_anterior.siguiente = celda_actual.siguiente
                        else:
                            fila_actual.cabeza_celda = celda_actual.siguiente

                        # Si la fila quedó vacía, eliminarla
                        if fila_actual.cabeza_celda is None:
                            if fila_anterior:
                                fila_anterior.siguiente_fila = fila_actual.siguiente_fila
                            else:
                                self.cabeza_fila = fila_actual.siguiente_fila

                        return True

                    celda_anterior = celda_actual
                    celda_actual = celda_actual.siguiente

                return False

            fila_anterior = fila_actual
            fila_actual = fila_actual.siguiente_fila

        return False

    def eliminar_fila(self, numero_fila: int) -> bool:
        """Elimina una fila completa"""
        if self.cabeza_fila is None:
            return False

        if self.cabeza_fila.numero_fila == numero_fila:
            self.cabeza_fila = self.cabeza_fila.siguiente_fila
            return True

        fila_anterior = self.cabeza_fila
        while fila_anterior.siguiente_fila:
            if fila_anterior.siguiente_fila.numero_fila == numero_fila:
                fila_anterior.siguiente_fila = fila_anterior.siguiente_fila.siguiente_fila
                return True
            fila_anterior = fila_anterior.siguiente_fila

        return False

    def eliminar_columna(self, numero_columna: int) -> bool:
        """Elimina una columna completa"""
        fila_actual = self.cabeza_fila
        cambios = 0

        while fila_actual:
            celda_actual = fila_actual.cabeza_celda
            celda_anterior = None

            while celda_actual:
                if celda_actual.columna == numero_columna:
                    if celda_anterior:
                        celda_anterior.siguiente = celda_actual.siguiente
                    else:
                        fila_actual.cabeza_celda = celda_actual.siguiente
                    cambios += 1
                    break

                celda_anterior = celda_actual
                celda_actual = celda_actual.siguiente

            # Si la fila quedó vacía, eliminarla
            if fila_actual.cabeza_celda is None:
                if self.cabeza_fila == fila_actual:
                    self.cabeza_fila = fila_actual.siguiente_fila
                else:
                    # Buscar fila anterior
                    fila_anterior = self.cabeza_fila
                    while fila_anterior.siguiente_fila != fila_actual:
                        fila_anterior = fila_anterior.siguiente_fila
                    fila_anterior.siguiente_fila = fila_actual.siguiente_fila

            fila_actual = fila_actual.siguiente_fila

        return cambios > 0

    def suma_rango(self, fila_inicio: int, fila_fin: int,
                   columna_inicio: int, columna_fin: int) -> float:
        """Suma los valores en un rango de celdas"""
        total = 0
        fila_actual = self.cabeza_fila

        while fila_actual:
            if fila_inicio <= fila_actual.numero_fila <= fila_fin:
                celda_actual = fila_actual.cabeza_celda
                while celda_actual:
                    if columna_inicio <= celda_actual.columna <= columna_fin:
                        total += celda_actual.valor
                    celda_actual = celda_actual.siguiente

            fila_actual = fila_actual.siguiente_fila

        return total

    def promedio_rango(self, fila_inicio: int, fila_fin: int,
                       columna_inicio: int, columna_fin: int) -> float:
        """Calcula el promedio en un rango de celdas"""
        total = 0
        cantidad = 0
        fila_actual = self.cabeza_fila

        while fila_actual:
            if fila_inicio <= fila_actual.numero_fila <= fila_fin:
                celda_actual = fila_actual.cabeza_celda
                while celda_actual:
                    if columna_inicio <= celda_actual.columna <= columna_fin:
                        total += celda_actual.valor
                        cantidad += 1
                    celda_actual = celda_actual.siguiente

            fila_actual = fila_actual.siguiente_fila

        return total / cantidad if cantidad > 0 else 0

    def mostrar(self, filas_mostrar: int = 10, columnas_mostrar: int = 10):
        """Muestra la hoja de cálculo en forma tabular"""
        print("\n" + "="*80)
        print(f"Hoja de Cálculo: {self.nombre}")
        print("="*80)

        if self.cabeza_fila is None:
            print("(vacío)")
            return

        # Obtener rango de datos
        filas_totales = self.max_fila + 1
        columnas_totales = self.max_columna + 1

        filas_mostrar = min(filas_mostrar, filas_totales)
        columnas_mostrar = min(columnas_mostrar, columnas_totales)

        # Encabezado de columnas
        encabezado = "     │ "
        for col in range(columnas_mostrar):
            encabezado += f"{col:>6} │ "
        print(encabezado)
        print("-" * len(encabezado))

        # Mostrar filas
        fila_actual = self.cabeza_fila
        for f in range(filas_mostrar):
            fila_str = f"{f:>3} │ "

            for c in range(columnas_mostrar):
                valor = self.obtener_valor(f, c)
                if valor == 0:
                    fila_str += "       │ "
                else:
                    fila_str += f"{valor:>6} │ "

            print(fila_str)

        print("="*80)
        print(f"Datos no vacíos: {self._contar_celdas()} celdas")
        print(f"Eficiencia de memoria vs matriz completa: {self._calcular_eficiencia()}")

    def guardar(self, nombre_archivo: str) -> bool:
        """Guarda la hoja en un archivo JSON"""
        try:
            datos = {
                'nombre': self.nombre,
                'celdas': []
            }

            fila_actual = self.cabeza_fila
            while fila_actual:
                celda_actual = fila_actual.cabeza_celda
                while celda_actual:
                    datos['celdas'].append({
                        'fila': celda_actual.fila,
                        'columna': celda_actual.columna,
                        'valor': celda_actual.valor
                    })
                    celda_actual = celda_actual.siguiente
                fila_actual = fila_actual.siguiente_fila

            with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
                json.dump(datos, archivo, indent=2)

            return True
        except Exception as e:
            print(f"Error al guardar: {e}")
            return False

    def cargar(self, nombre_archivo: str) -> bool:
        """Carga una hoja desde un archivo JSON"""
        try:
            if not os.path.exists(nombre_archivo):
                print(f"Archivo '{nombre_archivo}' no encontrado")
                return False

            with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
                datos = json.load(archivo)

            self.nombre = datos.get('nombre', 'Hoja1')
            self.cabeza_fila = None
            self.max_fila = 0
            self.max_columna = 0

            for celda_data in datos.get('celdas', []):
                self.insertar_valor(
                    celda_data['fila'],
                    celda_data['columna'],
                    celda_data['valor']
                )

            return True
        except Exception as e:
            print(f"Error al cargar: {e}")
            return False

    def _contar_celdas(self) -> int:
        """Cuenta el número total de celdas no vacías"""
        cantidad = 0
        fila_actual = self.cabeza_fila

        while fila_actual:
            celda_actual = fila_actual.cabeza_celda
            while celda_actual:
                cantidad += 1
                celda_actual = celda_actual.siguiente
            fila_actual = fila_actual.siguiente_fila

        return cantidad

    def _calcular_eficiencia(self) -> str:
        """Calcula la eficiencia de memoria comparado con una matriz completa"""
        if self.max_fila == 0 or self.max_columna == 0:
            return "N/A"

        celdas_usadas = self._contar_celdas()
        celdas_totales = (self.max_fila + 1) * (self.max_columna + 1)

        if celdas_totales == 0:
            return "N/A"

        porcentaje = (celdas_usadas / celdas_totales) * 100
        ahorro = ((celdas_totales - celdas_usadas) / celdas_totales) * 100

        return f"{ahorro:.1f}% de ahorro ({celdas_usadas}/{celdas_totales} celdas)"


def ejemplo_uso():
    """Demuestra el uso de la hoja de cálculo dispersa"""
    print("\n" + "#"*80)
    print("# HOJA DE CÁLCULO DISPERSA")
    print("#"*80)

    # Crear hoja
    hoja = HojaCalculoDispersа("Ventas2024")

    # 1. Insertar valores
    print("\n[1] Insertando valores...")
    print("-"*80)

    # Simular datos de ventas (dispersos)
    hoja.insertar_valor(0, 0, "Producto")
    hoja.insertar_valor(0, 1, "Enero")
    hoja.insertar_valor(0, 2, "Febrero")
    hoja.insertar_valor(0, 3, "Marzo")

    hoja.insertar_valor(1, 0, "Laptop")
    hoja.insertar_valor(1, 1, 5000)
    hoja.insertar_valor(1, 3, 4500)  # Febrero sin datos

    hoja.insertar_valor(2, 0, "Monitor")
    hoja.insertar_valor(2, 1, 1200)
    hoja.insertar_valor(2, 2, 1500)
    hoja.insertar_valor(2, 3, 1800)

    hoja.insertar_valor(3, 0, "Teclado")
    hoja.insertar_valor(3, 2, 300)
    hoja.insertar_valor(3, 3, 350)

    print("✓ 12 valores insertados en la hoja")
    hoja.mostrar()

    # 2. Obtener valores
    print("\n[2] Obteniendo valores específicos...")
    print("-"*80)
    print(f"Valor en (1,1): {hoja.obtener_valor(1, 1)}")
    print(f"Valor en (1,2): {hoja.obtener_valor(1, 2)}")  # Vacío
    print(f"Valor en (3,3): {hoja.obtener_valor(3, 3)}")

    # 3. Suma en rango
    print("\n[3] Operaciones en rangos...")
    print("-"*80)

    suma_enero = hoja.suma_rango(1, 3, 1, 1)
    print(f"Suma de Enero (col 1): {suma_enero}")

    suma_todo = hoja.suma_rango(1, 3, 1, 3)
    print(f"Suma total de ventas: {suma_todo}")

    promedio = hoja.promedio_rango(1, 3, 1, 3)
    print(f"Promedio de ventas: {promedio:.2f}")

    # 4. Eliminar valor
    print("\n[4] Eliminando un valor...")
    print("-"*80)
    hoja.eliminar_valor(2, 1)
    print("✓ Valor eliminado en (2,1)")
    hoja.mostrar()

    # 5. Actualizar valor
    print("\n[5] Actualizando un valor...")
    print("-"*80)
    hoja.insertar_valor(1, 2, 5100)  # Agregar valor que faltaba
    print("✓ Valor actualizado en (1,2)")
    hoja.mostrar()

    # 6. Eliminar columna
    print("\n[6] Eliminando una columna...")
    print("-"*80)
    hoja2 = HojaCalculoDispersа("Ventas2024_copia")
    # Copiar datos
    hoja2.insertar_valor(0, 0, "Producto")
    hoja2.insertar_valor(1, 0, "Laptop")
    hoja2.insertar_valor(1, 1, 5000)
    hoja2.insertar_valor(1, 2, 5100)
    hoja2.insertar_valor(1, 3, 4500)
    hoja2.insertar_valor(2, 0, "Monitor")
    hoja2.insertar_valor(2, 1, 1200)
    hoja2.insertar_valor(2, 2, 1500)
    hoja2.insertar_valor(2, 3, 1800)

    print("Antes de eliminar columna 2:")
    hoja2.mostrar()

    hoja2.eliminar_columna(2)
    print("\nDespués de eliminar columna 2:")
    hoja2.mostrar()

    # 7. Guardar y cargar
    print("\n[7] Guardando y cargando desde archivo...")
    print("-"*80)

    nombre_archivo = "hoja_calculo.json"
    if hoja.guardar(nombre_archivo):
        print(f"✓ Hoja guardada en '{nombre_archivo}'")

    hoja3 = HojaCalculoDispersа()
    if hoja3.cargar(nombre_archivo):
        print(f"✓ Hoja cargada desde '{nombre_archivo}'")
        hoja3.mostrar()

    # 8. Demostración de eficiencia
    print("\n[8] Comparación de eficiencia de memoria...")
    print("-"*80)

    hoja_grande = HojaCalculoDispersа("Grande")

    # Insertar pocos datos en una matriz grande
    for i in range(1000):
        for j in range(100):
            if (i % 100 == 0) and (j % 20 == 0):
                hoja_grande.insertar_valor(i, j, i * j)

    print(f"Hoja con dimensiones teóricas: 1000x100 = 100,000 celdas")
    print(f"Celdas realmente usadas: {hoja_grande._contar_celdas()}")
    print(f"Eficiencia: {hoja_grande._calcular_eficiencia()}")

    print("\n" + "#"*80)
    print("# FIN DE LA DEMOSTRACIÓN")
    print("#"*80 + "\n")


if __name__ == "__main__":
    ejemplo_uso()
