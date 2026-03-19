"""
Ejercicio de autoevaluación: contar vocales en una cadena

INSTRUCCIONES
-------------
Completa la función contar_vocales(texto) para que devuelva cuántas vocales
hay en la cadena recibida.

Requisitos:
- Debes recorrer el texto letra a letra.
- Debes usar una condición para comprobar si cada letra es una vocal.
- Para simplificar, considera como vocales solo: a, e, i, o, u
  y sus versiones en mayúscula: A, E, I, O, U.
- No uses librerías externas.

Ejemplos:
- contar_vocales("hola") debe devolver 2
- contar_vocales("Murcielago") debe devolver 5
- contar_vocales("xyz") debe devolver 0

TU TAREA
--------
Sustituye 'pass' por tu solución.
"""

def contar_vocales(texto):
    pass


# =========================
# BLOQUE DE PRUEBAS (TESTS)
# =========================
if __name__ == "__main__":
    assert contar_vocales("hola") == 2, "Error: 'hola' tiene 2 vocales"
    assert contar_vocales("Murcielago") == 5, "Error: 'Murcielago' tiene 5 vocales"
    assert contar_vocales("xyz") == 0, "Error: 'xyz' tiene 0 vocales"
    assert contar_vocales("") == 0, "Error: la cadena vacía tiene 0 vocales"
    assert contar_vocales("AEIOU") == 5, "Error: 'AEIOU' tiene 5 vocales"
    assert contar_vocales("Python") == 1, "Error: 'Python' tiene 1 vocal"
    assert contar_vocales("Me gusta programar") == 6, "Error: 'Me gusta programar' tiene 6 vocales"

    print("¡Felicidades! Todos los tests han pasado.")