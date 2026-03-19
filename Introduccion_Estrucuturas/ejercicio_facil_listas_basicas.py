"""
Ejercicio facil: operaciones basicas con listas

INSTRUCCIONES
-------------
Completa la funcion actualizar_lista(lista) para que haga lo siguiente:

1) Reciba una lista de numeros.
2) Guarde el primer elemento y el ultimo elemento de la lista original.
3) Cree una copia de la lista para no modificar la original.
4) Si la copia tiene al menos 3 elementos, cambie el tercer elemento por 35.
5) Devuelva una tupla con este formato:
   (primer_elemento, ultimo_elemento, lista_modificada)

Ejemplos:
- actualizar_lista([10, 20, 30, 40, 50]) debe devolver
  (10, 50, [10, 20, 35, 40, 50])
- actualizar_lista([7, 8, 9]) debe devolver
  (7, 9, [7, 8, 35])

RESTRICCIONES
-------------
- No modifiques la lista original recibida.
- Sustituye 'pass' por tu solucion.
"""


def actualizar_lista(lista):
    pass


# =========================
# BLOQUE DE PRUEBAS (TESTS)
# =========================
if __name__ == "__main__":
    original = [10, 20, 30, 40, 50]
    resultado = actualizar_lista(original)
    assert resultado == (10, 50, [10, 20, 35, 40, 50]), "Error en el caso principal"
    assert original == [10, 20, 30, 40, 50], "No debes modificar la lista original"

    assert actualizar_lista([7, 8, 9]) == (7, 9, [7, 8, 35]), "Error con lista de 3 elementos"
    assert actualizar_lista([1, 2, 3, 4]) == (1, 4, [1, 2, 35, 4]), "Error con lista de 4 elementos"
    assert actualizar_lista([99]) == (99, 99, [99]), "Error con lista de 1 elemento"
    assert actualizar_lista([5, 6]) == (5, 6, [5, 6]), "Error con lista de 2 elementos"

    print("¡Felicidades! Todos los tests han pasado.")
