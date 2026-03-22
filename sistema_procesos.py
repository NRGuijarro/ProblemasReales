"""
PROBLEMA 1: Sistema de Gestión de Procesos del Sistema Operativo
==============================================================

Este programa simula la gestión de procesos en un sistema operativo,
utilizando listas enlazadas para gestionar múltiples procesos en estados
de ejecución, espera, bloqueo y terminación.

Cada proceso tiene:
- ID único
- Nombre descriptivo
- Estado (listo, en ejecución, bloqueado, terminado)
- Tiempo de creación
- Tiempo de CPU requerido
"""

class Nodo:
    """Representa un nodo en la lista enlazada para un proceso"""
    def __init__(self, proceso_id, nombre, estado, tiempo_cpu):
        self.id = proceso_id
        self.nombre = nombre
        self.estado = estado  # 'listo', 'en ejecución', 'bloqueado', 'terminado'
        self.tiempo_cpu = tiempo_cpu  # milisegundos
        self.tiempo_creacion = 0  # se asigna en la gestión
        self.tiempo_espera = 0
        self.siguiente = None

class ListaEnlazadaProcesos:
    """Lista enlazada para gestionar procesos del sistema operativo"""
    def __init__(self):
        self.cabeza = None
        self.tiempo_actual = 0

    def agregar_proceso(self, proceso_id, nombre, tiempo_cpu):
        """
        Añade un nuevo proceso al final de la lista.
        El estado inicial es 'listo'.
        """
        nuevo_nodo = Nodo(proceso_id, nombre, 'listo', tiempo_cpu)
        nuevo_nodo.tiempo_creacion = self.tiempo_actual
        
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        
        print(f"✓ Proceso creado: ID={proceso_id}, Nombre={nombre}, "
              f"Tiempo CPU={tiempo_cpu}ms")

    def cambiar_estado(self, proceso_id, nuevo_estado):
        """Cambia el estado de un proceso específico"""
        actual = self.cabeza
        while actual:
            if actual.id == proceso_id:
                estado_anterior = actual.estado
                actual.estado = nuevo_estado
                print(f"✓ Proceso {proceso_id} ({actual.nombre}): "
                      f"{estado_anterior} → {nuevo_estado}")
                return True
            actual = actual.siguiente
        
        print(f"✗ Proceso {proceso_id} no encontrado")
        return False

    def eliminar_procesos_terminados(self):
        """Elimina todos los procesos con estado 'terminado'"""
        procesos_eliminados = []
        
        # Eliminar de la cabeza
        while self.cabeza and self.cabeza.estado == 'terminado':
            procesos_eliminados.append(self.cabeza.id)
            self.cabeza = self.cabeza.siguiente
        
        # Eliminar del resto
        if self.cabeza:
            actual = self.cabeza
            while actual.siguiente:
                if actual.siguiente.estado == 'terminado':
                    procesos_eliminados.append(actual.siguiente.id)
                    actual.siguiente = actual.siguiente.siguiente
                else:
                    actual = actual.siguiente
        
        if procesos_eliminados:
            print(f"✓ Procesos eliminados (terminados): {procesos_eliminados}")
        else:
            print("✓ No hay procesos terminados para eliminar")

    def mover_al_principio(self, proceso_id):
        """
        Mueve un proceso al principio de la lista (simula prioridad).
        Se usa cuando un proceso debe ejecutarse urgentemente.
        """
        if self.cabeza is None:
            print(f"✗ Lista vacía")
            return False
        
        if self.cabeza.id == proceso_id:
            print(f"✓ Proceso {proceso_id} ya está al principio")
            return True
        
        # Buscar y remover el proceso
        actual = self.cabeza
        while actual.siguiente:
            if actual.siguiente.id == proceso_id:
                proceso = actual.siguiente
                actual.siguiente = proceso.siguiente
                
                # Mover al principio
                proceso.siguiente = self.cabeza
                self.cabeza = proceso
                
                print(f"✓ Proceso {proceso_id} ({proceso.nombre}) movido al principio "
                      f"(PRIORIDAD ALTA)")
                return True
            actual = actual.siguiente
        
        print(f"✗ Proceso {proceso_id} no encontrado")
        return False

    def mostrar_procesos(self):
        """Muestra todos los procesos en orden de ejecución"""
        if self.cabeza is None:
            print("La lista de procesos está vacía\n")
            return
        
        print("\n" + "="*80)
        print(f"ESTADO ACTUAL DE PROCESOS (Tiempo del sistema: {self.tiempo_actual}ms)")
        print("="*80)
        print(f"{'ID':<4} {'Nombre':<20} {'Estado':<15} {'CPU':<8} {'Creación':<10} "
              f"{'Espera':<8}")
        print("-"*80)
        
        actual = self.cabeza
        while actual:
            print(f"{actual.id:<4} {actual.nombre:<20} {actual.estado:<15} "
                  f"{actual.tiempo_cpu:<8} {actual.tiempo_creacion:<10} "
                  f"{actual.tiempo_espera:<8}")
            actual = actual.siguiente
        print("="*80 + "\n")

    def tiempo_promedio_espera(self):
        """Calcula el tiempo promedio de espera de todos los procesos"""
        if self.cabeza is None:
            print("✗ No hay procesos en la lista")
            return 0
        
        total_espera = 0
        cantidad = 0
        actual = self.cabeza
        
        while actual:
            total_espera += actual.tiempo_espera
            cantidad += 1
            actual = actual.siguiente
        
        promedio = total_espera / cantidad if cantidad > 0 else 0
        print(f"✓ Tiempo de espera total: {total_espera}ms")
        print(f"✓ Cantidad de procesos: {cantidad}")
        print(f"✓ Tiempo promedio de espera: {promedio:.2f}ms\n")
        return promedio

    def simular_ejecucion(self, ciclos=10):
        """
        Simula la ejecución de procesos del sistemas operativo.
        En cada ciclo:
        - Un proceso en estado 'listo' pasa a 'en ejecución'
        - Consume tiempo de CPU
        - Si completa, pasa a 'terminado'
        """
        print("\n" + "="*80)
        print("SIMULACIÓN DE EJECUCIÓN DE PROCESOS")
        print("="*80)
        
        for ciclo in range(ciclos):
            print(f"\n--- CICLO {ciclo + 1} ---")
            self.tiempo_actual = ciclo * 100  # 100ms por ciclo
            
            # Simular ejecución: buscar un proceso en 'listo'
            actual = self.cabeza
            proceso_ejecutado = False
            
            while actual:
                if actual.estado == 'listo':
                    # Cambiar a ejecución
                    tiempo_espera = self.tiempo_actual - actual.tiempo_creacion
                    actual.tiempo_espera = tiempo_espera
                    actual.estado = 'en ejecución'
                    
                    # Simular ejecución (reduce tiempo CPU)
                    actual.tiempo_cpu -= 30  # 30ms por ciclo
                    
                    print(f"  → Ejecutando: {actual.nombre} (ID: {actual.id})")
                    print(f"    Tiempo de espera: {tiempo_espera}ms")
                    print(f"    Tiempo CPU restante: {max(0, actual.tiempo_cpu)}ms")
                    
                    # Si terminó
                    if actual.tiempo_cpu <= 0:
                        actual.estado = 'terminado'
                        print(f"    ✓ {actual.nombre} COMPLETADO")
                    else:
                        # Si no terminó, volver a listo (simular cambio de contexto)
                        actual.estado = 'listo'
                    
                    proceso_ejecutado = True
                    break
                
                actual = actual.siguiente
            
            if not proceso_ejecutado:
                print("  ⊘ Sin procesos listos para ejecutar")
            
            # Mostrar estado actual
            self.mostrar_procesos()
            
            # Eliminar procesos terminados cada 3 ciclos
            if (ciclo + 1) % 3 == 0:
                self.eliminar_procesos_terminados()


def main():
    """Ejecuta el simulador de gestión de procesos"""
    print("\n" + "#"*80)
    print("# SIMULADOR DE GESTIÓN DE PROCESOS DEL SISTEMA OPERATIVO")
    print("#"*80)
    
    # Crear lista de procesos
    gestor = ListaEnlazadaProcesos()
    
    # Crear 10 procesos
    print("\n[FASE 1] Creando 10 procesos...")
    print("-"*80)
    
    procesos_datos = [
        (1, "Sistema", 100),
        (2, "Firefox", 250),
        (3, "Editor", 150),
        (4, "Terminal", 80),
        (5, "Base de Datos", 300),
        (6, "Servidor Web", 200),
        (7, "Anti-virus", 180),
        (8, "Reproductor", 120),
        (9, "Compilador", 280),
        (10, "Chat", 90),
    ]
    
    for pid, nombre, cpu in procesos_datos:
        gestor.agregar_proceso(pid, nombre, cpu)
    
    # Mostrar estado inicial
    gestor.mostrar_procesos()
    
    # Cambiar estados de algunos procesos
    print("\n[FASE 2] Modificando estados de procesos...")
    print("-"*80)
    gestor.cambiar_estado(2, 'en ejecución')
    gestor.cambiar_estado(5, 'bloqueado')
    
    gestor.mostrar_procesos()
    
    # Mover proceso a prioridad alta
    print("\n[FASE 3] Ajustando prioridades...")
    print("-"*80)
    gestor.mover_al_principio(5)
    gestor.mostrar_procesos()
    
    # Simular ejecución
    gestor.simular_ejecucion(ciclos=12)
    
    # Mostrar estadísticas
    print("\n[FASE 4] Estadísticas finales...")
    print("-"*80)
    gestor.tiempo_promedio_espera()
    
    print("\n" + "#"*80)
    print("# FIN DE LA SIMULACIÓN")
    print("#"*80 + "\n")


if __name__ == "__main__":
    main()
