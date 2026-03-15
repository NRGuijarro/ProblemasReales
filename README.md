# Sistemas Modulares en Python

Este proyecto implementa cinco problemas reales utilizando programación modular con funciones y procedimientos en Python.  
Cada problema se encuentra en un archivo independiente para mejorar la organización del código.

---

## Problema 1: Control de Temperatura en un Edificio Inteligente

Funciones implementadas:

- **leer_sensores_temperatura()**
  Lee los sensores de temperatura en cada zona.

- **calcular_temperatura_optima()**
  Determina la temperatura ideal considerando hora, ocupación y clima.

- **ajustar_climatizacion()**
  Envía señales al sistema HVAC para calefacción o refrigeración.

- **registrar_consumo()**
  Guarda el consumo energético y calcula el promedio.

Impacto en rendimiento:
El uso de funciones permite reutilizar cálculos y separar responsabilidades, reduciendo duplicación de código.

---

## Problema 2: Gestión de Inventario

Funciones implementadas:

- **registrar_entrada()**
  Añade productos al inventario.

- **registrar_salida()**
  Reduce el stock al vender o retirar productos.

- **calcular_nivel_optimo()**
  Determina el nivel mínimo de inventario.

- **generar_alerta()**
  Genera alertas cuando el inventario es bajo.

Impacto en rendimiento:
El sistema usa un diccionario para acceso rápido a productos (O(1)), mejorando eficiencia.

---

## Problema 3: Navegación de Vehículo Autónomo

Funciones implementadas:

- **leer_sensores()**
  Obtiene datos de sensores.

- **calcular_ruta_optima()**
  Genera la ruta hacia el destino.

- **detectar_obstaculo()**
  Detecta obstáculos en la vía.

- **ajustar_velocidad()**
  Ajusta la velocidad según tráfico.

Impacto en rendimiento:
La modularidad permite integrar algoritmos más complejos sin modificar todo el sistema.

---

## Problema 4: Optimización de Producción

Funciones implementadas:

- **monitorear_maquinas()**
  Verifica estado de máquinas.

- **planificar_mantenimiento()**
  Programa mantenimiento preventivo.

- **analizar_rendimiento()**
  Calcula eficiencia productiva.

- **ajustar_produccion()**
  Modifica la producción según demanda.

Impacto en rendimiento:
Separar monitoreo, mantenimiento y análisis mejora la escalabilidad del sistema.

---

## Problema 5: Sistema de Riego Automatizado

Funciones implementadas:

- **leer_humedad()**
  Obtiene humedad del suelo.

- **consultar_clima()**
  Consulta condiciones meteorológicas.

- **calcular_riego()**
  Determina cantidad de agua necesaria.

- **controlar_valvula()**
  Activa o desactiva válvulas de riego.

Impacto en rendimiento:
La modularidad permite optimizar cada función individualmente y reutilizar sensores o cálculos.