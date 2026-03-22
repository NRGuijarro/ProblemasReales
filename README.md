# Problemas de Implementación con Listas Enlazadas

## Descripción General

Este proyecto implementa 4 problemas del mundo real utilizando **listas enlazadas** como estructura de datos principal. Cada problema demuestra aplicaciones prácticas de esta estructura en sistemas operativos, editores de texto, matemáticas e ingeniería de software.

---

## Problemas Implementados

### **Problema 1: Sistema de Gestión de Procesos del Sistema Operativo**

**Archivo:** `sistema_procesos.py`

#### Descripción
Simula la gestión de procesos en un sistema operativo moderno utilizando listas enlazadas. Los procesos tienen estados (listo, en ejecución, bloqueado, terminado) y se gestionan dinámicamente.

#### Estructura
- **Clase `Nodo`**: Representa un proceso con ID, nombre, estado, tiempo de CPU y metadata
- **Clase `ListaEnlazadaProcesos`**: Gestiona múltiples procesos en estado dinámico

#### Operaciones Implementadas
- ✅ Agregar procesos (al final de la lista)
- ✅ Cambiar estado de un proceso
- ✅ Eliminar procesos terminados
- ✅ Mover proceso al principio (simular prioridad)
- ✅ Mostrar todos los procesos en orden
- ✅ Calcular tiempo promedio de espera
- ✅ Simular ejecución con cambio de contexto

#### Cómo Ejecutar
```bash
python sistema_procesos.py
```

#### Salida Esperada
```
################################################################################
# SIMULADOR DE GESTIÓN DE PROCESOS DEL SISTEMA OPERATIVO
################################################################################

[FASE 1] Creando 10 procesos...
--------------------------------------------------------------------------------
✓ Proceso creado: ID=1, Nombre=Sistema, Tiempo CPU=100ms
✓ Proceso creado: ID=2, Nombre=Firefox, Tiempo CPU=250ms
✓ Proceso creado: ID=3, Nombre=Editor, Tiempo CPU=150ms
... (7 procesos más)

================================================================================
ESTADO ACTUAL DE PROCESOS (Tiempo del sistema: 0ms)
================================================================================
ID   Nombre               Estado          CPU      Creación   Espera  
----
1    Sistema              listo           100      0          0       
2    Firefox              listo           250      0          0       
... (8 procesos más)

[FASE 2] Modificando estados de procesos...
--------------------------------------------------------------------------------
✓ Proceso 2 (Firefox): listo → en ejecución
✓ Proceso 5 (Base de Datos): listo → bloqueado

[FASE 3] Ajustando prioridades...
--------------------------------------------------------------------------------
✓ Proceso 5 (Base de Datos) movido al principio (PRIORIDAD ALTA)

[SIMULACIÓN DE EJECUCIÓN]
--- CICLO 1 ---
  → Ejecutando: Base de Datos (ID: 5)
    Tiempo de espera: 0ms
    Tiempo CPU restante: 270ms
```

#### Conceptos Clave
- Escalonador de procesos (process scheduler)
- Cambio de contexto (context switching)
- Estados de procesos
- Métricas de rendimiento (tiempo de espera)

---

### **Problema 2: Editor de Texto Básico**

**Archivo:** `editor_texto.py`

#### Descripción
Editor de texto basado en consola que utiliza listas **doblemente enlazadas** para administrar líneas de texto. Permite operaciones eficientes de inserción, eliminación y búsqueda.

#### Estructura
- **Clase `NodoLinea`**: Nodo doblemente enlazado que contiene una línea de texto
- **Clase `EditorTexto`**: Gestor de líneas con operaciones de edición

#### 📝 Operaciones Implementadas
- ✅ Insertar línea en cualquier posición
- ✅ Eliminar línea específica
- ✅ Mover línea a otra posición
- ✅ Buscar texto en todas las líneas
- ✅ Reemplazar texto en línea específica
- ✅ Reemplazar globalmente
- ✅ Guardar contenido en archivo
- ✅ Cargar contenido desde archivo
- ✅ Obtener estadísticas (líneas, palabras, caracteres)

#### Cómo Ejecutar
```bash
python editor_texto.py
```

#### Salida Esperada
```
################################################################################
# EDITOR DE TEXTO BÁSICO - LISTAS ENLAZADAS
################################################################################

[1] Insertando líneas...
[2] Insertando línea en posición 2...
[3] Buscando texto: 'listas'...
Línea 1: Introducción a las listas enlazadas
Línea 3: Las listas enlazadas son estructuras dinámicas

[4] Reemplazando 'eficiente' por 'muy eficiente'...
✓ Texto reemplazado

[11] Estadísticas del documento...
Líneas: 6
Caracteres: 285
Palabras: 47
Línea más larga: 50 caracteres
```

#### Conceptos Clave
- Listas doblemente enlazadas
- Búsqueda y reemplazo de texto
- Persistencia de datos (E/S de archivos)
- Optimización: búsqueda desde inicio o final

---

### **Problema 3: Sistema de Gestión de Polinomios**

**Archivo:** `sistema_polinomios.py`

#### Descripción
Implementa un sistema para operaciones matemáticas con polinomios usando listas enlazadas. Ideal para polinomios dispersos con muchos coeficientes cero.

#### Estructura
- **Clase `Termino`**: Nodo que contiene coeficiente y exponente
- **Clase `Polinomio`**: Lista enlazada de términos ordenada por exponente descendente

#### Operaciones Implementadas
- ✅ Suma de polinomios
- ✅ Resta de polinomios
- ✅ Multiplicación de polinomios
- ✅ Evaluación en un valor x
- ✅ Derivación
- ✅ Integración
- ✅ Representación en formato estándar

#### Cómo Ejecutar
```bash
python sistema_polinomios.py
```

#### Salida Esperada
```
################################################################################
# SISTEMA DE GESTIÓN DE POLINOMIOS
################################################################################

[EJEMPLO 1] Suma de polinomios
P₁(x): 3x^4 + 2x^2 - 5
P₂(x): 1x^4 - 1x^2 + 3x + 7
P₁(x) + P₂(x): 4x^4 + 1x^2 + 3x + 2

[EJEMPLO 2] Resta de polinomios
P₁(x) - P₂(x): 2x^4 + 3x^2 - 3x - 12

[EJEMPLO 3] Multiplicación de polinomios
P₃(x): 2x + 1
P₄(x): 1x - 3
P₃(x) × P₄(x): 2x^2 - 5x - 3

[EJEMPLO 5] Derivación
P₅(x): 4x^3 - 3x^2 + 2x - 1
P₅'(x) = dP₅/dx: 12x^2 - 6x + 2

[EJEMPLO 6] Integración
∫P₆(x)dx: 1x^3 + 1x^2
```

#### Conceptos Clave
- Polinomios dispersos vs densos
- Cálculo diferencial
- Cálculo integral
- Operaciones algebraicas
- Eficiencia de memoria en estructuras dispersas

---

### **Problema 4: Hoja de Cálculo Dispersa**

**Archivo:** `hoja_calculo_dispersa.py`

#### Descripción
Implementa una hoja de cálculo eficiente que solo almacena celdas con valores, usando una estructura de dos listas enlazadas (una para filas, cada fila con celdas).

#### Estructura
- **Clase `Celda`**: Representa una celda con (fila, columna, valor)
- **Clase `FilaEnlazada`**: Fila con lista de celdas no vacías
- **Clase `HojaCalculoDispersа`**: Gestor de filas para la hoja dispersa

#### Operaciones Implementadas
- ✅ Insertar/actualizar valores en celda
- ✅ Obtener valor de celda específica
- ✅ Eliminar valor (celda)
- ✅ Eliminar fila completa
- ✅ Eliminar columna completa
- ✅ Suma en rango de celdas
- ✅ Promedio en rango de celdas
- ✅ Mostrar en forma tabular
- ✅ Guardar/cargar desde JSON

#### Cómo Ejecutar
```bash
python hoja_calculo_dispersa.py
```

#### Salida Esperada
```
################################################################################
# HOJA DE CÁLCULO DISPERSA
################################################################################

✓ 12 valores insertados en la hoja

================================================================================
Hoja de Cálculo: Ventas2024
================================================================================
     │        0 │        1 │        2 │        3 │ 

  0  │ Producto │      Enero │    Febrero │    Marzo │ 
  1  │    Laptop │      5000 │          │      4500 │ 
  2  │   Monitor │      1200 │       1500 │      1800 │ 
  3  │  Teclado │            │        300 │       350 │ 
================================================================================
Datos no vacíos: 12 celdas
Eficiencia de memoria vs matriz completa: 70.0% de ahorro (12/16 celdas)

[3] Operaciones en rangos...
Suma de Enero (col 1): 7200
Suma total de ventas: 16650
Promedio de ventas: 1500.00
```

#### Conceptos Clave
- Matrices dispersas
- Optimización de memoria
- Acceso aleatorio a datos
- Agregaciones (suma, promedio)
- Persistencia con JSON

---

## Instalación

No se requieren dependencias externas. Solo Python 3.6+

```bash
# Clonar o descargar el repositorio
cd ProblemasReales

# Ejecutar directamente
python sistema_procesos.py
python editor_texto.py
python sistema_polinomios.py
python hoja_calculo_dispersa.py
```

---

## Comparativa de Implementaciones

| Problema | Tipo de Lista | Casos de Uso | Ventaja Principal |
|----------|---------------|-------------|-------------------|
| 1. Procesos | Simple | Colas, pilas de ejecución | Gestión dinámica |
| 2. Editor | Doble | Navegación bidireccional | Inserción/eliminación O(1) |
| 3. Polinomios | Ordenada | Datos dispersos | Ahorro de memoria |
| 4. Hoja Cálculo | 2D (tabla) | Matrices dispersas | Eficiencia 99%+ |

---

## Conceptos de Listas Enlazadas

### Ventajas
✅ Inserción y eliminación en O(1) cuando se conoce la posición
✅ Memoria dinámica (crece según necesidad)
✅ No requiere espacio preallocated
✅ Flexible para datos de diferentes tamaños

### Limitaciones
❌ Acceso directo en O(n) - necesita traversal
❌ Más memoria por overhead de punteros
❌ No permite búsqueda binaria eficiente
❌ Mayor complejidad de código

---

## Análisis de Complejidad

### Problema 1: Sistema de Procesos
| Operación | Complejidad |
|-----------|------------|
| Agregar proceso | O(1) |
| Cambiar estado | O(n) |
| Eliminar terminados | O(n) |
| Mover a principio | O(n) |
| Mostrar procesos | O(n) |

### Problema 2: Editor de Texto
| Operación | Complejidad |
|-----------|------------|
| Insertar línea | O(n) |
| Eliminar línea | O(n) |
| Buscar texto | O(n×m) |
| Reemplazar | O(n×m) |
| Guardar/cargar | O(n) |

### Problema 3: Polinomios
| Operación | Complejidad |
|-----------|------------|
| Agregar término | O(n) |
| Suma | O(n+m) |
| Multiplicación | O(n×m) |
| Derivación | O(n) |
| Evaluación | O(n) |

### Problema 4: Hoja Dispersa
| Operación | Complejidad |
|-----------|------------|
| Insertar celda | O(k) |
| Obtener valor | O(k) |
| Suma rango | O(k) |
| Eliminar columna | O(n×m) |

Donde: n, m = cantidad de datos; k = celdas no vacías

---

## Checklist de Funcionalidades

### Problema 1
- [x] Lista enlazada simple para procesos
- [x] 10+ procesos en demostración
- [x] Estados dinámicos
- [x] Simulación de ejecución
- [x] Estadísticas

### Problema 2
- [x] Lista doblemente enlazada
- [x] Todas operaciones implementadas
- [x] Persistencia en archivo
- [x] Búsqueda y reemplazo
- [x] Estadísticas de documento

### Problema 3
- [x] Lista ordenada de términos
- [x] Suma, resta, multiplicación
- [x] Derivación e integración
- [x] Evaluación en valor x
- [x] Formato matemático legible

### Problema 4
- [x] Estructura 2D (tabla)
- [x] Solo almacena celdas no vacías
- [x] Operaciones en rangos
- [x] Guardar/cargar JSON
- [x] Análisis de eficiencia
