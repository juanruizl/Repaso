"""
Ejercicio de autoevaluación (dificultad difícil)
Tema: Repaso de Python - numpy y ecuaciones lineales

INSTRUCCIONES
-------------
Completa la función resolver_sistema_lineal(A, B) para que resuelva un sistema
lineal de ecuaciones de la forma:

    A · X = B

Donde:
- A es la matriz de coeficientes.
- B es el vector de resultados.
- X es el vector solución que debes devolver.

Requisitos:
- Usa numpy.
- Usa numpy.linalg.solve().
- La función debe aceptar A y B como listas de Python o como arrays de numpy.
- Devuelve la solución como un array de numpy.

Ejemplos:
- A = [[2, 1], [1, 3]]
- B = [8, 13]
- La solución debe ser [2, 3]

TU TAREA
--------
Sustituye 'pass' por tu solución.
"""

import numpy as np


def resolver_sistema_lineal(A, B):
    pass


# =========================
# BLOQUE DE PRUEBAS (TESTS)
# =========================
if __name__ == "__main__":
    solucion_1 = resolver_sistema_lineal([[2, 1], [1, 3]], [8, 13])
    assert np.allclose(solucion_1, np.array([2.2, 3.6])), (
        "Error: para A=[[2,1],[1,3]] y B=[8,13], la solución debe ser [2.2, 3.6]"
    )

    solucion_2 = resolver_sistema_lineal([[1, 0], [0, 1]], [5, -2])
    assert np.allclose(solucion_2, np.array([5.0, -2.0])), (
        "Error: con la matriz identidad, la solución debe coincidir con B"
    )

    solucion_3 = resolver_sistema_lineal(
        [[3, 2, -1], [2, -2, 4], [-1, 0.5, -1]],
        [1, -2, 0],
    )
    assert np.allclose(solucion_3, np.array([1.0, -2.0, -2.0])), (
        "Error: la solución del sistema 3x3 debe ser [1, -2, -2]"
    )

    solucion_4 = resolver_sistema_lineal(
        np.array([[4, 1], [2, 3]], dtype=float),
        np.array([9, 13], dtype=float),
    )
    assert np.allclose(solucion_4, np.array([1.4, 3.4])), (
        "Error: el sistema con arrays de numpy debe devolver [1.4, 3.4]"
    )

    print("¡Felicidades! Todos los tests han pasado.")
