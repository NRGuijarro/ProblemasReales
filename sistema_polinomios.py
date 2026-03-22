"""
PROBLEMA 3: Sistema de Gestión de Polinomios
=============================================

Este programa implementa un sistema para manipular polinomios utilizando
listas enlazadas. Cada nodo contiene un coeficiente y su exponente.

Las listas enlazadas son especialmente útiles para polinomios dispersos
que tienen muchos coeficientes cero, ya que solo se almacenan los
términos con coeficientes diferentes de cero.

Operaciones implementadas:
- Suma y resta de polinomios
- Multiplicación de polinomios
- Evaluación en un valor x
- Derivación e integración
- Representación en formato estándar
"""

import math
from typing import Optional, Tuple

class Termino:
    """Representa un término del polinomio (coeficiente * x^exponente)"""
    def __init__(self, coeficiente: float, exponente: int):
        self.coeficiente = coeficiente
        self.exponente = exponente
        self.siguiente = None

    def __repr__(self):
        if self.coeficiente == 0:
            return "0"
        
        # Formato del término
        coef_str = f"{self.coeficiente:.1f}" if self.coeficiente != int(self.coeficiente) else str(int(self.coeficiente))
        
        if self.exponente == 0:
            return coef_str
        elif self.exponente == 1:
            return f"{coef_str}x"
        else:
            return f"{coef_str}x^{self.exponente}"

class Polinomio:
    """Lista enlazada para representar un polinomio"""
    def __init__(self):
        self.cabeza = None

    def agregar_termino(self, coeficiente: float, exponente: int):
        """
        Agrega un término al polinomio.
        Mantiene los términos ordenados por exponente descendente.
        Si el exponente ya existe, suma los coeficientes.
        """
        if coeficiente == 0:
            return  # No agregar términos con coeficiente 0
        
        # Si la lista está vacía
        if self.cabeza is None:
            self.cabeza = Termino(coeficiente, exponente)
            return
        
        # Si debe ir al principio (exponente mayor)
        if exponente > self.cabeza.exponente:
            nuevo = Termino(coeficiente, exponente)
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo
            return
        
        # Buscar posición correcta
        actual = self.cabeza
        while actual:
            # Si ya existe este exponente, sumar coeficientes
            if actual.exponente == exponente:
                actual.coeficiente += coeficiente
                # Si el resultado es 0, eliminar el término
                if actual.coeficiente == 0:
                    self._eliminar_termino_por_exponente(exponente)
                return
            
            # Si el siguiente es menor o no existe
            if actual.siguiente is None or actual.siguiente.exponente < exponente:
                nuevo = Termino(coeficiente, exponente)
                nuevo.siguiente = actual.siguiente
                actual.siguiente = nuevo
                return
            
            actual = actual.siguiente

    def obtener_termino(self, exponente: int) -> Optional[float]:
        """Obtiene el coeficiente de un exponente específico"""
        actual = self.cabeza
        while actual:
            if actual.exponente == exponente:
                return actual.coeficiente
            actual = actual.siguiente
        return 0.0

    def evaluar(self, x: float) -> float:
        """Evalúa el polinomio en un valor x dado"""
        resultado = 0
        actual = self.cabeza
        
        while actual:
            resultado += actual.coeficiente * (x ** actual.exponente)
            actual = actual.siguiente
        
        return resultado

    def derivar(self) -> "Polinomio":
        """
        Calcula la derivada del polinomio.
        Derivada de ax^n es n*a*x^(n-1)
        """
        derivada = Polinomio()
        actual = self.cabeza
        
        while actual:
            if actual.exponente > 0:
                nuevo_coef = actual.coeficiente * actual.exponente
                nuevo_exp = actual.exponente - 1
                derivada.agregar_termino(nuevo_coef, nuevo_exp)
            actual = actual.siguiente
        
        return derivada

    def integrar(self, constante_integracion: float = 0) -> "Polinomio":
        """
        Calcula la integral indefinida del polinomio.
        Integral de ax^n es (a/(n+1))*x^(n+1) + C
        """
        integral = Polinomio()
        
        # Agregar constante de integración
        if constante_integracion != 0:
            integral.agregar_termino(constante_integracion, 0)
        
        actual = self.cabeza
        while actual:
            nuevo_exp = actual.exponente + 1
            nuevo_coef = actual.coeficiente / nuevo_exp
            integral.agregar_termino(nuevo_coef, nuevo_exp)
            actual = actual.siguiente
        
        return integral

    def sumar(self, otro: "Polinomio") -> "Polinomio":
        """Suma este polinomio con otro"""
        resultado = Polinomio()
        
        # Agregar todos los términos del primero
        actual = self.cabeza
        while actual:
            resultado.agregar_termino(actual.coeficiente, actual.exponente)
            actual = actual.siguiente
        
        # Agregar todos los términos del segundo
        actual = otro.cabeza
        while actual:
            resultado.agregar_termino(actual.coeficiente, actual.exponente)
            actual = actual.siguiente
        
        return resultado

    def restar(self, otro: "Polinomio") -> "Polinomio":
        """Resta otro polinomio de este"""
        resultado = Polinomio()
        
        # Agregar todos los términos del primero
        actual = self.cabeza
        while actual:
            resultado.agregar_termino(actual.coeficiente, actual.exponente)
            actual = actual.siguiente
        
        # Restar todos los términos del segundo
        actual = otro.cabeza
        while actual:
            resultado.agregar_termino(-actual.coeficiente, actual.exponente)
            actual = actual.siguiente
        
        return resultado

    def multiplicar(self, otro: "Polinomio") -> "Polinomio":
        """
        Multiplica este polinomio por otro.
        (ax^m) * (bx^n) = ab*x^(m+n)
        """
        resultado = Polinomio()
        
        # Multiplicar cada término del primero por cada del segundo
        actual1 = self.cabeza
        while actual1:
            actual2 = otro.cabeza
            while actual2:
                coef_resultado = actual1.coeficiente * actual2.coeficiente
                exp_resultado = actual1.exponente + actual2.exponente
                resultado.agregar_termino(coef_resultado, exp_resultado)
                actual2 = actual2.siguiente
            actual1 = actual1.siguiente
        
        return resultado

    def obtener_grado(self) -> int:
        """Obtiene el grado del polinomio (mayor exponente)"""
        if self.cabeza:
            return self.cabeza.exponente
        return -1  # Polinomio cero

    def obtener_representacion_matematica(self) -> str:
        """
        Retorna una representación matemática legible del polinomio
        Ejemplo: 3x^4 - 2x^2 + 5
        """
        if self.cabeza is None:
            return "0"
        
        terminos = []
        actual = self.cabeza
        es_primer_termino = True
        
        while actual:
            # Formato del coeficiente
            coef = actual.coeficiente
            
            # Determinar signo
            if es_primer_termino:
                signo = "-" if coef < 0 else ""
                es_primer_termino = False
            else:
                signo = "+ " if coef >= 0 else "- "
            
            coef_abs = abs(coef)
            
            # Formato según el exponente
            if actual.exponente == 0:
                # Término constante
                coef_str = f"{int(coef_abs) if coef_abs == int(coef_abs) else coef_abs}"
                término = f"{signo}{coef_str}"
            elif actual.exponente == 1:
                # Término lineal
                if coef_abs == 1:
                    término = f"{signo}x"
                else:
                    coef_str = f"{int(coef_abs) if coef_abs == int(coef_abs) else coef_abs}"
                    término = f"{signo}{coef_str}x"
            else:
                # Término con exponente mayor
                if coef_abs == 1:
                    término = f"{signo}x^{actual.exponente}"
                else:
                    coef_str = f"{int(coef_abs) if coef_abs == int(coef_abs) else coef_abs}"
                    término = f"{signo}{coef_str}x^{actual.exponente}"
            
            terminos.append(término)
            actual = actual.siguiente
        
        # Unir términos
        resultado = " ".join(terminos)
        # Limpiar espacios extras
        resultado = resultado.replace(" - ", " - ").replace(" + ", " + ")
        return resultado

    def mostrar(self, nombre: str = "Polinomio"):
        """Muestra el polinomio de forma legible"""
        print(f"{nombre}: {self.obtener_representacion_matematica()}")


def crear_polinomio_desde_lista(terminos: list) -> Polinomio:
    """
    Crea un polinomio a partir de una lista de tuplas (coeficiente, exponente)
    """
    p = Polinomio()
    for coef, exp in terminos:
        p.agregar_termino(coef, exp)
    return p


def ejemplo_uso():
    """Demuestra el uso del sistema de polinomios"""
    print("\n" + "#"*80)
    print("# SISTEMA DE GESTIÓN DE POLINOMIOS")
    print("#"*80)
    
    # Ejemplo 1: Suma de polinomios
    print("\n[EJEMPLO 1] Suma de polinomios")
    print("-"*80)
    
    # P1(x) = 3x^4 + 2x^2 - 5
    p1 = crear_polinomio_desde_lista([(3, 4), (2, 2), (-5, 0)])
    p1.mostrar("P₁(x)")
    
    # P2(x) = x^4 - x^2 + 3x + 7
    p2 = crear_polinomio_desde_lista([(1, 4), (-1, 2), (3, 1), (7, 0)])
    p2.mostrar("P₂(x)")
    
    p_suma = p1.sumar(p2)
    p_suma.mostrar("P₁(x) + P₂(x)")
    
    # Ejemplo 2: Resta de polinomios
    print("\n[EJEMPLO 2] Resta de polinomios")
    print("-"*80)
    
    p_resta = p1.restar(p2)
    p_resta.mostrar("P₁(x) - P₂(x)")
    
    # Ejemplo 3: Multiplicación de polinomios
    print("\n[EJEMPLO 3] Multiplicación de polinomios")
    print("-"*80)
    
    # P3(x) = 2x + 1
    p3 = crear_polinomio_desde_lista([(2, 1), (1, 0)])
    p3.mostrar("P₃(x)")
    
    # P4(x) = x - 3
    p4 = crear_polinomio_desde_lista([(1, 1), (-3, 0)])
    p4.mostrar("P₄(x)")
    
    p_mult = p3.multiplicar(p4)
    p_mult.mostrar("P₃(x) × P₄(x)")
    print(f"(Esperado: 2x² - 6x + x - 3 = 2x² - 5x - 3)")
    
    # Ejemplo 4: Evaluación de polinomio
    print("\n[EJEMPLO 4] Evaluación de polinomio")
    print("-"*80)
    
    p1.mostrar("P₁(x)")
    
    for x in [0, 1, 2, -1]:
        valor = p1.evaluar(x)
        print(f"P₁({x}) = {valor}")
    
    # Ejemplo 5: Derivación
    print("\n[EJEMPLO 5] Derivación de polinomios")
    print("-"*80)
    
    # P5(x) = 4x^3 - 3x^2 + 2x - 1
    p5 = crear_polinomio_desde_lista([(4, 3), (-3, 2), (2, 1), (-1, 0)])
    p5.mostrar("P₅(x)")
    
    p5_derivada = p5.derivar()
    p5_derivada.mostrar("P₅'(x) = dP₅/dx")
    print(f"(Esperado: 12x² - 6x + 2)")
    
    # Ejemplo 6: Integración
    print("\n[EJEMPLO 6] Integración de polinomios")
    print("-"*80)
    
    # P6(x) = 3x^2 + 2x
    p6 = crear_polinomio_desde_lista([(3, 2), (2, 1)])
    p6.mostrar("P₆(x)")
    
    p6_integral = p6.integrar(constante_integracion=0)
    p6_integral.mostrar("∫P₆(x)dx")
    print(f"(Esperado: x³ + x² + C)")
    
    # Validar evaluación de integral
    print("\nValidación: si derivamos la integral obtenemos el polinomio original:")
    p6_integral_derivada = p6_integral.derivar()
    p6_integral_derivada.mostrar("(∫P₆(x)dx)' ")
    
    # Ejemplo 7: Operaciones combinadas
    print("\n[EJEMPLO 7] Operaciones combinadas")
    print("-"*80)
    
    print("Sea P(x) = x³ + 2x² - 5x + 3")
    p = crear_polinomio_desde_lista([(1, 3), (2, 2), (-5, 1), (3, 0)])
    p.mostrar("P(x)")
    
    print(f"Grado del polinomio: {p.obtener_grado()}")
    print(f"Evaluación en x=2: P(2) = {p.evaluar(2)}")
    
    p_deriv = p.derivar()
    p_deriv.mostrar("P'(x)")
    print(f"P'(1) = {p_deriv.evaluar(1)}")
    
    p_integ = p.integrar()
    p_integ.mostrar("∫P(x)dx")
    
    # Comparación de eficiencia
    print("\n[EFICIENCIA DE MEMORIA]")
    print("-"*80)
    print("Polinomio disperso: P(x) = 1000x^1000 + 1")
    print("Con lista enlazada: 2 términos almacenados")
    print("Con matriz completa: 1001 elementos necesarios")
    
    p_disperso = crear_polinomio_desde_lista([(1000, 1000), (1, 0)])
    p_disperso.mostrar("P(x)")
    print(f"Evaluación en x=2: P(2) = {p_disperso.evaluar(2)}")
    
    print("\n" + "#"*80)
    print("# FIN DE LA DEMOSTRACIÓN")
    print("#"*80 + "\n")


if __name__ == "__main__":
    ejemplo_uso()
