"""
Ejercicio media: diccionarios y listas de diccionarios

INSTRUCCIONES
-------------
Completa la funcion resumir_libros(libros) para que reciba una lista de diccionarios.
Cada diccionario representa un libro y siempre tendra estas claves:
- "titulo"
- "autor"
- "anio"

La funcion debe devolver una lista de strings con este formato exacto:
"<titulo> fue escrito por <autor> en <anio>"

Ejemplo de entrada:
[
    {"titulo": "Python", "autor": "Ana", "anio": 2020},
    {"titulo": "EDA", "autor": "Luis", "anio": 2024}
]

Ejemplo de salida:
[
    "Python fue escrito por Ana en 2020",
    "EDA fue escrito por Luis en 2024"
]

RESTRICCIONES
-------------
- Debes recorrer la lista de libros.
- Debes acceder a la informacion por clave.
- Sustituye 'pass' por tu solucion.
"""


def resumir_libros(libros):
    pass


# =========================
# BLOQUE DE PRUEBAS (TESTS)
# =========================
if __name__ == "__main__":
    libros_1 = [
        {"titulo": "Python", "autor": "Ana", "anio": 2020},
        {"titulo": "EDA", "autor": "Luis", "anio": 2024},
    ]
    esperado_1 = [
        "Python fue escrito por Ana en 2020",
        "EDA fue escrito por Luis en 2024",
    ]
    assert resumir_libros(libros_1) == esperado_1, "Error en el caso principal"

    libros_2 = [
        {"titulo": "Algoritmos", "autor": "Marta", "anio": 2018}
    ]
    esperado_2 = ["Algoritmos fue escrito por Marta en 2018"]
    assert resumir_libros(libros_2) == esperado_2, "Error con un solo libro"

    assert resumir_libros([]) == [], "Error: la lista vacia debe devolver lista vacia"

    libros_3 = [
        {"titulo": "A", "autor": "B", "anio": 1},
        {"titulo": "C", "autor": "D", "anio": 2},
        {"titulo": "E", "autor": "F", "anio": 3},
    ]
    esperado_3 = [
        "A fue escrito por B en 1",
        "C fue escrito por D en 2",
        "E fue escrito por F en 3",
    ]
    assert resumir_libros(libros_3) == esperado_3, "Error al recorrer varios libros"

    print("¡Felicidades! Todos los tests han pasado.")
