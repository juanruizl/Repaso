"""
Ejercicio medio: comprobar si existe conexión en un grafo dirigido

INSTRUCCIONES
-------------
Completa la función hay_camino(grafo, origen, destino).

El grafo está representado con un diccionario de adyacencia dirigido:
- Cada clave es un nodo.
- Su valor es la lista de nodos a los que puede ir directamente.

La función debe devolver:
- True si se puede llegar desde 'origen' hasta 'destino'
  siguiendo una o varias aristas.
- False en caso contrario.

Ejemplo:
    grafo = {
        "A": ["B"],
        "B": ["C"],
        "C": [],
    }

    hay_camino(grafo, "A", "C") -> True
    hay_camino(grafo, "C", "A") -> False

REGLAS
------
- Puedes usar listas, bucles, condicionales y conjuntos.
- No uses librerías externas.
- Sustituye 'pass' por tu solución.

PISTA
-----
Puedes ir guardando nodos pendientes por visitar y un conjunto de visitados.
"""


def hay_camino(grafo, origen, destino):
    pass


# =========================
# BLOQUE DE PRUEBAS (TESTS)
# =========================
if __name__ == "__main__":
    grafo = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": [],
        "D": ["E"],
        "E": [],
        "F": ["A"],
    }

    assert hay_camino(grafo, "A", "D") is True, "Error: desde A sí se debe poder llegar a D"
    assert hay_camino(grafo, "A", "E") is True, "Error: desde A sí se debe poder llegar a E"
    assert hay_camino(grafo, "C", "A") is False, "Error: desde C no se debe poder llegar a A"
    assert hay_camino(grafo, "F", "E") is True, "Error: desde F sí se debe poder llegar a E"
    assert hay_camino(grafo, "E", "A") is False, "Error: desde E no se debe poder llegar a A"
    assert hay_camino(grafo, "X", "A") is False, "Error: si el origen no existe, debe devolver False"
    assert hay_camino(grafo, "A", "X") is False, "Error: si el destino no existe, debe devolver False"
    assert hay_camino(grafo, "A", "A") is True, "Error: un nodo debe poder llegar a sí mismo"

    print("¡Felicidades! Todos los tests han pasado.")
