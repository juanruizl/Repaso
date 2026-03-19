"""
Ejercicio muy alto: sistema de autocompletado con Trie

INSTRUCCIONES
-------------
Completa la implementación de un Trie (árbol de prefijos).

Debes implementar la clase Trie con estos métodos:
- insertar(palabra): añade una palabra al trie
- contiene(palabra): devuelve True si la palabra completa existe, False en caso contrario
- sugerencias(prefijo): devuelve una lista con todas las palabras del trie que empiezan
  por ese prefijo, en orden alfabético

DETALLES IMPORTANTES
--------------------
- Usa nodos con:
    * un diccionario llamado hijos
    * un booleano llamado es_palabra
- Si el prefijo no existe, sugerencias(prefijo) debe devolver []
- Si el prefijo es una palabra completa y además hay otras que continúan,
  deben devolverse todas
- Para que los tests pasen, devuelve las sugerencias en orden alfabético

PISTA
-----
Te resultará útil crear un método auxiliar recursivo o iterativo que recorra
el subárbol a partir del nodo del prefijo.

RESTRICCIONES
-------------
- Sustituye cada 'pass' por tu solución.
- No modifiques los tests.
"""

class NodoTrie:
    def __init__(self):
        self.hijos = {}
        self.es_palabra = False


class Trie:
    def __init__(self):
        pass

    def insertar(self, palabra):
        pass

    def contiene(self, palabra):
        pass

    def sugerencias(self, prefijo):
        pass


# =========================
# BLOQUE DE PRUEBAS (TESTS)
# =========================
if __name__ == "__main__":
    trie = Trie()
    palabras = [
        "programa",
        "programar",
        "progreso",
        "probar",
        "python",
        "pila",
        "piloto",
    ]

    for palabra in palabras:
        trie.insertar(palabra)

    assert trie.contiene("programa") is True, "'programa' debería existir"
    assert trie.contiene("programar") is True, "'programar' debería existir"
    assert trie.contiene("pro") is False, "'pro' no debería existir como palabra completa"
    assert trie.contiene("py") is False, "'py' no debería existir como palabra completa"
    assert trie.contiene("python") is True, "'python' debería existir"
    assert trie.contiene("piloto") is True, "'piloto' debería existir"
    assert trie.contiene("java") is False, "'java' no debería existir"

    assert trie.sugerencias("pro") == [
        "probar",
        "programa",
        "programar",
        "progreso",
    ], "Las sugerencias para 'pro' no son correctas"

    assert trie.sugerencias("prog") == [
        "programa",
        "programar",
        "progreso",
    ], "Las sugerencias para 'prog' no son correctas"

    assert trie.sugerencias("python") == ["python"], "Las sugerencias para 'python' no son correctas"
    assert trie.sugerencias("pi") == ["pila", "piloto"], "Las sugerencias para 'pi' no son correctas"
    assert trie.sugerencias("z") == [], "Para un prefijo inexistente debe devolver []"
    assert trie.sugerencias("") == sorted(palabras), "Con prefijo vacío deberían salir todas las palabras ordenadas"

    print("¡Felicidades! Todos los tests han pasado.")
