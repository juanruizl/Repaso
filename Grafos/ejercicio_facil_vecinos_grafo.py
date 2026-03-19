"""
Ejercicio fácil: grado de un nodo en un grafo no dirigido

INSTRUCCIONES
-------------
Completa la función grado_nodo(grafo, nodo).

El grafo se representa con un diccionario de adyacencia:
- Cada clave es un nodo.
- Su valor es una lista con los nodos vecinos.

Tu función debe devolver cuántos vecinos tiene el nodo dado.
Es decir, debe devolver su grado.

Ejemplo:
    grafo = {
        "A": ["B", "C"],
        "B": ["A"],
        "C": ["A"]
    }

    grado_nodo(grafo, "A") -> 2
    grado_nodo(grafo, "B") -> 1

REGLAS
------
- Si el nodo no existe en el grafo, devuelve 0.
- No uses librerías externas.
- Sustituye 'pass' por tu solución.
"""


def grado_nodo(grafo, nodo):
    pass


# =========================
# BLOQUE DE PRUEBAS (TESTS)
# =========================
if __name__ == "__main__":
    grafo1 = {
        "A": ["B", "C", "D"],
        "B": ["A"],
        "C": ["A", "D"],
        "D": ["A", "C"],
    }

    assert grado_nodo(grafo1, "A") == 3, "Error: el nodo A debe tener grado 3"
    assert grado_nodo(grafo1, "B") == 1, "Error: el nodo B debe tener grado 1"
    assert grado_nodo(grafo1, "C") == 2, "Error: el nodo C debe tener grado 2"
    assert grado_nodo(grafo1, "Z") == 0, "Error: un nodo inexistente debe devolver 0"

    grafo2 = {
        "Madrid": ["Toledo", "Segovia"],
        "Toledo": ["Madrid"],
        "Segovia": ["Madrid"],
    }

    assert grado_nodo(grafo2, "Madrid") == 2, "Error: Madrid debe tener grado 2"
    assert grado_nodo(grafo2, "Toledo") == 1, "Error: Toledo debe tener grado 1"

    print("¡Felicidades! Todos los tests han pasado.")
