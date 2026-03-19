"""
Ejercicio fácil: implementar una pila básica

INSTRUCCIONES
-------------
Completa la clase Pila para representar una estructura LIFO
(Last In, First Out): el último elemento en entrar es el primero en salir.

Debes implementar estos métodos:
- apilar(elemento): añade un elemento al final de la pila
- desapilar(): elimina y devuelve el último elemento
  * Si la pila está vacía, devuelve None
- ver_tope(): devuelve el último elemento sin eliminarlo
  * Si la pila está vacía, devuelve None
- esta_vacia(): devuelve True si la pila no tiene elementos y False en caso contrario
- tamano(): devuelve el número de elementos de la pila

RESTRICCIONES
-------------
- Usa una lista interna para almacenar los datos.
- Sustituye cada 'pass' por tu solución.
- No modifiques los tests.
"""

class Pila:
    def __init__(self):
        pass

    def apilar(self, elemento):
        pass

    def desapilar(self):
        pass

    def ver_tope(self):
        pass

    def esta_vacia(self):
        pass

    def tamano(self):
        pass


# =========================
# BLOQUE DE PRUEBAS (TESTS)
# =========================
if __name__ == "__main__":
    pila = Pila()

    assert pila.esta_vacia() is True, "La pila debe empezar vacía"
    assert pila.tamano() == 0, "El tamaño inicial debe ser 0"
    assert pila.ver_tope() is None, "El tope de una pila vacía debe ser None"
    assert pila.desapilar() is None, "Desapilar una pila vacía debe devolver None"

    pila.apilar("A")
    pila.apilar("B")
    pila.apilar("C")

    assert pila.esta_vacia() is False, "La pila ya no debe estar vacía"
    assert pila.tamano() == 3, "La pila debe tener 3 elementos"
    assert pila.ver_tope() == "C", "El tope debe ser 'C'"

    assert pila.desapilar() == "C", "El primer desapilado debe ser 'C'"
    assert pila.ver_tope() == "B", "Ahora el tope debe ser 'B'"
    assert pila.tamano() == 2, "La pila debe tener 2 elementos"

    assert pila.desapilar() == "B", "El siguiente desapilado debe ser 'B'"
    assert pila.desapilar() == "A", "El siguiente desapilado debe ser 'A'"
    assert pila.desapilar() is None, "La pila vuelve a estar vacía"
    assert pila.esta_vacia() is True, "La pila debe estar vacía al final"

    print("¡Felicidades! Todos los tests han pasado.")
