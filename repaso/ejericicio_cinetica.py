"""
Ejercicio de autoevaluación (dificultad media)
Tema: Repaso de Python - funciones, operaciones y retorno de valores

INSTRUCCIONES
-------------
Completa la función energia_cinetica(masa, velocidad) para que devuelva
la energía cinética de un objeto.

Recuerda la fórmula:
    E = 1/2 * m * v**2

Requisitos:
- Debes devolver el resultado numérico.
- No debes pedir datos con input() dentro de la función.
- No uses librerías externas.

Ejemplos:
- energia_cinetica(2, 3) -> 9.0
- energia_cinetica(10, 0) -> 0.0

TU TAREA
--------
Sustituye 'pass' por tu solución.
"""


def energia_cinetica(masa, velocidad):
    pass


# =========================
# BLOQUE DE PRUEBAS (TESTS)
# =========================
if __name__ == "__main__":
    assert energia_cinetica(2, 3) == 9.0, "Error: con masa=2 y velocidad=3 el resultado debe ser 9.0"
    assert energia_cinetica(10, 0) == 0.0, "Error: si la velocidad es 0, la energía debe ser 0.0"
    assert energia_cinetica(1, 4) == 8.0, "Error: con masa=1 y velocidad=4 el resultado debe ser 8.0"
    assert energia_cinetica(0.5, 2) == 1.0, "Error: con masa=0.5 y velocidad=2 el resultado debe ser 1.0"
    assert energia_cinetica(3, 1.5) == 3.375, "Error: con masa=3 y velocidad=1.5 el resultado debe ser 3.375"

    print("¡Felicidades! Todos los tests han pasado.")