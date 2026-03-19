"""
Ejercicio media-alta: conjuntos para eliminar duplicados

INSTRUCCIONES
-------------
Completa la funcion analizar_invitados(confirmados_correo, confirmados_app)
para trabajar con dos listas de nombres.

La funcion debe:
1) Calcular los invitados unicos que aparecen en al menos una lista.
2) Calcular los invitados repetidos que aparecen en ambas listas.
3) Devolver un diccionario con este formato exacto:
   {
       "unicos": [...],
       "repetidos": [...],
       "total_unicos": <int>
   }

IMPORTANTE
----------
- Las listas que devuelvas en "unicos" y "repetidos" deben estar ordenadas
  alfabeticamente para que el resultado sea determinista.
- Debes usar operaciones de conjuntos.
- No modifiques las listas originales.

Ejemplo:
confirmados_correo = ["Ana", "Luis", "Marta", "Ana"]
confirmados_app = ["Luis", "Carlos", "Marta"]

Salida esperada:
{
    "unicos": ["Ana", "Carlos", "Luis", "Marta"],
    "repetidos": ["Luis", "Marta"],
    "total_unicos": 4
}
"""


def analizar_invitados(confirmados_correo, confirmados_app):
    pass


# =========================
# BLOQUE DE PRUEBAS (TESTS)
# =========================
if __name__ == "__main__":
    correo = ["Ana", "Luis", "Marta", "Ana"]
    app = ["Luis", "Carlos", "Marta"]
    esperado = {
        "unicos": ["Ana", "Carlos", "Luis", "Marta"],
        "repetidos": ["Luis", "Marta"],
        "total_unicos": 4,
    }
    assert analizar_invitados(correo, app) == esperado, "Error en el caso principal"
    assert correo == ["Ana", "Luis", "Marta", "Ana"], "No debes modificar la lista correo"
    assert app == ["Luis", "Carlos", "Marta"], "No debes modificar la lista app"

    assert analizar_invitados([], []) == {
        "unicos": [],
        "repetidos": [],
        "total_unicos": 0,
    }, "Error con listas vacias"

    assert analizar_invitados(["A", "B"], ["C", "D"]) == {
        "unicos": ["A", "B", "C", "D"],
        "repetidos": [],
        "total_unicos": 4,
    }, "Error sin elementos repetidos"

    assert analizar_invitados(["Juan", "Juan", "Eva"], ["Juan", "Eva", "Eva"]) == {
        "unicos": ["Eva", "Juan"],
        "repetidos": ["Eva", "Juan"],
        "total_unicos": 2,
    }, "Error con muchos duplicados"

    print("¡Felicidades! Todos los tests han pasado.")
