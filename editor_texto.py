"""
PROBLEMA 2: Editor de Texto Básico con Operaciones de Línea
===========================================================

Este programa implementa un editor de texto basado en consola que permite
al usuario manipular líneas de texto utilizando listas enlazadas.

Cada nodo representa una línea de texto con operaciones como:
- Insertar líneas en cualquier posición
- Eliminar líneas específicas
- Mover líneas
- Buscar y reemplazar texto
- Guardar y cargar desde archivos
"""

import os
from datetime import datetime

class NodoLinea:
    """Representa una línea de texto en el editor"""
    def __init__(self, numero, contenido=""):
        self.numero = numero
        self.contenido = contenido
        self.siguiente = None
        self.anterior = None

class EditorTexto:
    """Editor de texto basado en listas enlazadas (doblemente enlazadas)"""
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.cantidad_lineas = 0
        self.archivo_actual = None

    def insertar_linea(self, num_linea, contenido=""):
        """
        Inserta una nueva línea en la posición especificada.
        Si existe, desplaza las demás hacia abajo.
        """
        # Normalizar número de línea
        if num_linea < 1:
            num_linea = 1
        if num_linea > self.cantidad_lineas + 1:
            num_linea = self.cantidad_lineas + 1
        
        nuevo_nodo = NodoLinea(num_linea, contenido)
        
        # Si está vacío
        if self.cabeza is None:
            self.cabeza = self.cola = nuevo_nodo
            self.cantidad_lineas = 1
            return True
        
        # Si inserta al principio
        if num_linea == 1:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
            self._renumerar_desde(self.cabeza)
            return True
        
        # Buscar posición
        actual = self.cabeza
        posicion_actual = 1
        
        while actual and posicion_actual < num_linea - 1:
            actual = actual.siguiente
            posicion_actual += 1
        
        # Insertar
        if actual:
            nuevo_nodo.siguiente = actual.siguiente
            nuevo_nodo.anterior = actual
            
            if actual.siguiente:
                actual.siguiente.anterior = nuevo_nodo
            else:
                self.cola = nuevo_nodo
            
            actual.siguiente = nuevo_nodo
            self._renumerar_desde(nuevo_nodo)
            self.cantidad_lineas += 1
            return True
        
        return False

    def eliminar_linea(self, num_linea):
        """Elimina una línea específica"""
        if not self.cabeza or num_linea < 1 or num_linea > self.cantidad_lineas:
            return False
        
        # Buscar línea
        actual = self._obtener_nodo(num_linea)
        
        if not actual:
            return False
        
        # Es la única línea
        if self.cabeza == self.cola:
            self.cabeza = self.cola = None
            self.cantidad_lineas = 0
            return True
        
        # Es la cabeza
        if actual == self.cabeza:
            self.cabeza = actual.siguiente
            self.cabeza.anterior = None
        # Es la cola
        elif actual == self.cola:
            self.cola = actual.anterior
            self.cola.siguiente = None
        # En el medio
        else:
            actual.anterior.siguiente = actual.siguiente
            actual.siguiente.anterior = actual.anterior
        
        self.cantidad_lineas -= 1
        self._renumerar_desde(self.cabeza)
        return True

    def mover_linea(self, de_linea, a_linea):
        """Mueve una línea de una posición a otra"""
        if de_linea < 1 or de_linea > self.cantidad_lineas:
            return False
        
        # Obtener contenido
        nodo = self._obtener_nodo(de_linea)
        contenido = nodo.contenido
        
        # Eliminar línea original
        self.eliminar_linea(de_linea)
        
        # Insertar en nueva posición
        self.insertar_linea(a_linea, contenido)
        
        return True

    def buscar_texto(self, texto_buscar):
        """
        Busca un texto en todas las líneas.
        Retorna lista de números de línea donde aparece.
        """
        resultados = []
        actual = self.cabeza
        
        while actual:
            if texto_buscar.lower() in actual.contenido.lower():
                resultados.append((actual.numero, actual.contenido))
            actual = actual.siguiente
        
        return resultados

    def reemplazar_texto(self, num_linea, texto_viejo, texto_nuevo):
        """Reemplaza texto en una línea específica"""
        nodo = self._obtener_nodo(num_linea)
        
        if not nodo:
            return False
        
        if texto_viejo in nodo.contenido:
            nodo.contenido = nodo.contenido.replace(texto_viejo, texto_nuevo)
            return True
        
        return False

    def reemplazar_texto_global(self, texto_viejo, texto_nuevo):
        """Reemplaza texto en todas las líneas"""
        reemplazos = 0
        actual = self.cabeza
        
        while actual:
            if texto_viejo in actual.contenido:
                actual.contenido = actual.contenido.replace(texto_viejo, texto_nuevo)
                reemplazos += 1
            actual = actual.siguiente
        
        return reemplazos

    def mostrar_contenido(self, mostrar_numeros=True):
        """Muestra todo el contenido del documento"""
        if self.cabeza is None:
            print("(documento vacío)")
            return
        
        print("\n" + "="*80)
        actual = self.cabeza
        
        while actual:
            if mostrar_numeros:
                print(f"{actual.numero:3d} │ {actual.contenido}")
            else:
                print(actual.contenido)
            actual = actual.siguiente
        
        print("="*80 + f" Total: {self.cantidad_lineas} líneas\n")

    def obtener_linea(self, num_linea):
        """Obtiene el contenido de una línea específica"""
        nodo = self._obtener_nodo(num_linea)
        return nodo.contenido if nodo else None

    def modificar_linea(self, num_linea, nuevo_contenido):
        """Modifica el contenido de una línea"""
        nodo = self._obtener_nodo(num_linea)
        
        if nodo:
            nodo.contenido = nuevo_contenido
            return True
        
        return False

    def guardar(self, nombre_archivo):
        """Guarda el contenido en un archivo de texto"""
        try:
            with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
                actual = self.cabeza
                while actual:
                    archivo.write(actual.contenido + '\n')
                    actual = actual.siguiente
            
            self.archivo_actual = nombre_archivo
            return True
        except Exception as e:
            print(f"Error al guardar: {e}")
            return False

    def cargar(self, nombre_archivo):
        """Carga contenido desde un archivo"""
        try:
            if not os.path.exists(nombre_archivo):
                print(f"Archivo '{nombre_archivo}' no encontrado")
                return False
            
            # Limpiar editor
            self.cabeza = None
            self.cola = None
            self.cantidad_lineas = 0
            
            # Cargar líneas
            with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
                for linea in archivo:
                    contenido = linea.rstrip('\n')
                    self.insertar_linea(self.cantidad_lineas + 1, contenido)
            
            self.archivo_actual = nombre_archivo
            return True
        except Exception as e:
            print(f"Error al cargar: {e}")
            return False

    def _obtener_nodo(self, num_linea):
        """Obtiene un nodo por número de línea"""
        if num_linea < 1 or num_linea > self.cantidad_lineas:
            return None
        
        # Optimización: empezar desde el inicio o final según número
        if num_linea <= self.cantidad_lineas // 2:
            actual = self.cabeza
            posicion = 1
            while actual and posicion < num_linea:
                actual = actual.siguiente
                posicion += 1
        else:
            actual = self.cola
            posicion = self.cantidad_lineas
            while actual and posicion > num_linea:
                actual = actual.anterior
                posicion -= 1
        
        return actual

    def _renumerar_desde(self, nodo_inicio):
        """Renumera los nodos a partir de uno dado"""
        if not nodo_inicio:
            return
        
        # Encontrar el inicio
        actual = nodo_inicio
        while actual.anterior:
            actual = actual.anterior
        
        # Renumerar
        numero = 1
        while actual:
            actual.numero = numero
            numero += 1
            actual = actual.siguiente

    def obtener_estadisticas(self):
        """Obtiene estadísticas del documento"""
        if self.cabeza is None:
            return {
                'lineas': 0,
                'caracteres': 0,
                'palabras': 0,
                'linea_mas_larga': 0
            }
        
        lineas = self.cantidad_lineas
        caracteres = 0
        palabras = 0
        linea_mas_larga = 0
        
        actual = self.cabeza
        while actual:
            caracteres += len(actual.contenido)
            palabras += len(actual.contenido.split())
            linea_mas_larga = max(linea_mas_larga, len(actual.contenido))
            actual = actual.siguiente
        
        return {
            'lineas': lineas,
            'caracteres': caracteres,
            'palabras': palabras,
            'linea_mas_larga': linea_mas_larga
        }


def ejemplo_uso():
    """Demuestra el uso del editor"""
    print("\n" + "#"*80)
    print("# EDITOR DE TEXTO BÁSICO - LISTAS ENLAZADAS")
    print("#"*80)
    
    editor = EditorTexto()
    
    # 1. Insertar líneas
    print("\n[1] Insertando líneas...")
    print("-"*80)
    editor.insertar_linea(1, "Introducción a las listas enlazadas")
    editor.insertar_linea(2, "Las listas enlazadas son estructuras dinámicas")
    editor.insertar_linea(3, "Permiten inserción y eliminación eficiente")
    editor.insertar_linea(4, "Se usan en muchas aplicaciones prácticas")
    editor.insertar_linea(5, "Por ejemplo: sistemas de archivos, pilas, colas")
    
    print("✓ 5 líneas insertadas")
    editor.mostrar_contenido()
    
    # 2. Insertar en posición específica
    print("\n[2] Insertando línea en posición 2...")
    print("-"*80)
    editor.insertar_linea(2, "← Esta es una línea insertada en el medio")
    editor.mostrar_contenido()
    
    # 3. Buscar texto
    print("\n[3] Buscando texto: 'listas'...")
    print("-"*80)
    resultados = editor.buscar_texto("listas")
    for num_linea, contenido in resultados:
        print(f"Línea {num_linea}: {contenido}")
    
    # 4. Reemplazar texto
    print("\n[4] Reemplazando 'eficiente' por 'muy eficiente'...")
    print("-"*80)
    editor.reemplazar_texto(3, "eficiente", "muy eficiente")
    print("✓ Texto reemplazado")
    editor.mostrar_contenido()
    
    # 5. Reemplazar globalmente
    print("\n[5] Reemplazando 'listas enlazadas' por 'listas doblemente enlazadas'...")
    print("-"*80)
    cambios = editor.reemplazar_texto_global("listas enlazadas", 
                                             "listas doblemente enlazadas")
    print(f"✓ {cambios} cambios realizados")
    editor.mostrar_contenido()
    
    # 6. Mover línea
    print("\n[6] Moviendo línea 3 a posición 6...")
    print("-"*80)
    editor.mover_linea(3, 6)
    print("✓ Línea movida")
    editor.mostrar_contenido()
    
    # 7. Eliminar línea
    print("\n[7] Eliminando línea 4...")
    print("-"*80)
    editor.eliminar_linea(4)
    print("✓ Línea eliminada")
    editor.mostrar_contenido()
    
    # 8. Modificar línea
    print("\n[8] Modificando línea 1...")
    print("-"*80)
    editor.modificar_linea(1, "INTRODUCCIÓN A LAS LISTAS DOBLEMENTE ENLAZADAS")
    print("✓ Línea modificada")
    editor.mostrar_contenido()
    
    # 9. Guardar archivo
    print("\n[9] Guardando en archivo 'documento.txt'...")
    print("-"*80)
    nombre_archivo = "documento.txt"
    if editor.guardar(nombre_archivo):
        print(f"✓ Archivo guardado: {nombre_archivo}")
    
    # 10. Crear nuevo documento
    editor2 = EditorTexto()
    print("\n[10] Cargando desde archivo...")
    print("-"*80)
    if editor2.cargar(nombre_archivo):
        print(f"✓ Archivo cargado: {nombre_archivo}")
        editor2.mostrar_contenido()
    
    # 11. Estadísticas
    print("\n[11] Estadísticas del documento...")
    print("-"*80)
    stats = editor.obtener_estadisticas()
    print(f"Líneas: {stats['lineas']}")
    print(f"Caracteres: {stats['caracteres']}")
    print(f"Palabras: {stats['palabras']}")
    print(f"Línea más larga: {stats['linea_mas_larga']} caracteres")
    
    print("\n" + "#"*80)
    print("# FIN DE LA DEMOSTRACIÓN")
    print("#"*80 + "\n")


if __name__ == "__main__":
    ejemplo_uso()
