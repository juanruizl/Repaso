"""
Ejercicio media-alta: calcular similitud entre categorías de producto

INSTRUCCIONES
-------------
Completa la función similitud_categoria(cat1, cat2).

Cada categoría se representa con un diccionario que tiene estas claves:
- "tipo"
- "color"
- "estilo"

Debes calcular una puntuación de similitud siguiendo estas reglas:
- +3 puntos si tienen el mismo "tipo"
- +2 puntos si tienen el mismo "color"
- +1 punto si tienen el mismo "estilo"

La función debe devolver la suma total.

Ejemplo:
    cat1 = {"tipo": "camiseta", "color": "rojo", "estilo": "casual"}
    cat2 = {"tipo": "camiseta", "color": "blanco", "estilo": "casual"}

    similitud_categoria(cat1, cat2) -> 4

REGLAS
------
- No uses librerías externas.
- Sustituye 'pass' por tu solución.
- Asume que los diccionarios siempre contienen las tres claves.
"""


def similitud_categoria(cat1, cat2):
    pass


# =========================
# BLOQUE DE PRUEBAS (TESTS)
# =========================
if __name__ == "__main__":
    a = {"tipo": "camiseta", "color": "rojo", "estilo": "casual"}
    b = {"tipo": "camiseta", "color": "blanco", "estilo": "casual"}
    c = {"tipo": "chaqueta", "color": "rojo", "estilo": "formal"}
    d = {"tipo": "camiseta", "color": "rojo", "estilo": "casual"}
    e = {"tipo": "pantalon", "color": "azul", "estilo": "deportivo"}

    assert similitud_categoria(a, b) == 4, "Error: mismo tipo y mismo estilo debe sumar 4"
    assert similitud_categoria(a, c) == 2, "Error: solo mismo color debe sumar 2"
    assert similitud_categoria(a, d) == 6, "Error: todo igual debe sumar 6"
    assert similitud_categoria(a, e) == 0, "Error: nada igual debe sumar 0"
    assert similitud_categoria(b, d) == 4, "Error: mismo tipo y mismo estilo debe sumar 4"

    print("¡Felicidades! Todos los tests han pasado.")
