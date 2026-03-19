"""
Ejercicio media-alta: recomendar categorías similares con un grafo ponderado

INSTRUCCIONES
-------------
Completa estas dos funciones:

1) calcular_similitud(cat1, cat2)
   Recibe dos diccionarios categoría con las claves:
   - nombre
   - tipo
   - color
   - estilo

   Debe devolver un peso entero con estas reglas:
   - +3 si coincide el tipo
   - +2 si coincide el color
   - +1 si coincide el estilo

2) categorias_mas_similares(categorias, nombre_objetivo, top_n=3)
   Recibe una lista de diccionarios categoría y el nombre de una categoría objetivo.
   Debe devolver una lista con los nombres de las top_n categorías más similares.

REGLAS
------
- No incluyas la categoría objetivo en el resultado.
- Ordena de mayor similitud a menor similitud.
- Si hay empate, desempata por orden alfabético del nombre.
- Si nombre_objetivo no existe, devuelve []
- No uses librerías externas.
- Sustituye cada 'pass' por tu solución.
- No modifiques los tests.
"""


def calcular_similitud(cat1, cat2):
    pass


def categorias_mas_similares(categorias, nombre_objetivo, top_n=3):
    pass


# =========================
# BLOQUE DE PRUEBAS (TESTS)
# =========================
if __name__ == "__main__":
    categorias = [
        {"nombre": "camiseta_roja", "tipo": "camiseta", "color": "rojo", "estilo": "casual"},
        {"nombre": "camiseta_blanca", "tipo": "camiseta", "color": "blanco", "estilo": "casual"},
        {"nombre": "pantalon_azul", "tipo": "pantalon", "color": "azul", "estilo": "casual"},
        {"nombre": "chaqueta_roja", "tipo": "chaqueta", "color": "rojo", "estilo": "formal"},
        {"nombre": "camiseta_roja_formal", "tipo": "camiseta", "color": "rojo", "estilo": "formal"},
    ]

    peso_1 = calcular_similitud(categorias[0], categorias[1])
    assert peso_1 == 4, "Error: camiseta_roja y camiseta_blanca deben tener peso 4"

    peso_2 = calcular_similitud(categorias[0], categorias[3])
    assert peso_2 == 2, "Error: camiseta_roja y chaqueta_roja deben tener peso 2"

    peso_3 = calcular_similitud(categorias[0], categorias[4])
    assert peso_3 == 5, "Error: camiseta_roja y camiseta_roja_formal deben tener peso 5"

    recomendadas = categorias_mas_similares(categorias, "camiseta_roja", top_n=3)
    assert recomendadas == ["camiseta_roja_formal", "camiseta_blanca", "chaqueta_roja"], (
        "Error en el orden de recomendaciones para camiseta_roja"
    )

    recomendadas_2 = categorias_mas_similares(categorias, "camiseta_blanca", top_n=2)
    assert recomendadas_2 == ["camiseta_roja", "camiseta_roja_formal"], (
        "Error en las recomendaciones para camiseta_blanca"
    )

    recomendadas_3 = categorias_mas_similares(categorias, "no_existe", top_n=3)
    assert recomendadas_3 == [], "Error: si la categoría no existe, debe devolver []"

    print("¡Felicidades! Todos los tests han pasado.")
