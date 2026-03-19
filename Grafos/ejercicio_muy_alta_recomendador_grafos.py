"""
Ejercicio muy alto: construir un grafo de similitud y recomendar categorías

INSTRUCCIONES
-------------
Completa las dos funciones siguientes:

1) construir_grafo_similitud(categorias)
   Recibe una lista de diccionarios. Cada diccionario representa una categoría con estas claves:
   - "nombre"
   - "tipo"
   - "color"
   - "estilo"

   Debe devolver un grafo ponderado con este formato:
       {
           "nombre_categoria": {
               "otra_categoria": peso,
               ...
           },
           ...
       }

   Reglas del peso:
   - +3 si coincide el "tipo"
   - +2 si coincide el "color"
   - +1 si coincide el "estilo"

   Solo debes añadir una conexión si el peso es mayor que 0.
   El grafo debe ser no dirigido, así que si A conecta con B con peso 4,
   entonces B también conecta con A con peso 4.

2) recomendar_categorias(grafo, nombre_categoria, top_n=3)
   Debe devolver una lista con los nombres de las categorías más similares,
   ordenadas de mayor peso a menor peso.

   Si hay empate de peso, desempata por orden alfabético del nombre.
   Solo debe devolver como máximo top_n elementos.
   Si la categoría no existe en el grafo, debe devolver una lista vacía.

Ejemplo de salida:
    ["camiseta_blanca", "chaqueta_roja", "pantalon_azul"]

REGLAS
------
- No uses librerías externas.
- Sustituye cada 'pass' por tu solución.
- No modifiques los tests.
"""


def construir_grafo_similitud(categorias):
    pass


def recomendar_categorias(grafo, nombre_categoria, top_n=3):
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

    grafo = construir_grafo_similitud(categorias)

    # Comprobaciones estructurales básicas
    assert isinstance(grafo, dict), "Error: el grafo debe ser un diccionario"
    assert "camiseta_roja" in grafo, "Error: debe existir el nodo camiseta_roja"
    assert "camiseta_blanca" in grafo, "Error: debe existir el nodo camiseta_blanca"

    # Pesos esperados
    # camiseta_roja vs camiseta_blanca -> mismo tipo (3) + mismo estilo (1) = 4
    assert grafo["camiseta_roja"]["camiseta_blanca"] == 4, "Error en el peso entre camiseta_roja y camiseta_blanca"

    # camiseta_roja vs chaqueta_roja -> mismo color (2)
    assert grafo["camiseta_roja"]["chaqueta_roja"] == 2, "Error en el peso entre camiseta_roja y chaqueta_roja"

    # camiseta_roja vs camiseta_roja_formal -> mismo tipo (3) + mismo color (2) = 5
    assert grafo["camiseta_roja"]["camiseta_roja_formal"] == 5, "Error en el peso entre camiseta_roja y camiseta_roja_formal"

    # El grafo debe ser simétrico
    assert grafo["camiseta_blanca"]["camiseta_roja"] == 4, "Error: el grafo debe ser no dirigido"
    assert grafo["chaqueta_roja"]["camiseta_roja"] == 2, "Error: el grafo debe ser no dirigido"

    # Recomendaciones
    recomendadas = recomendar_categorias(grafo, "camiseta_roja", top_n=3)
    assert recomendadas == ["camiseta_roja_formal", "camiseta_blanca", "chaqueta_roja"], (
        "Error en el orden de recomendaciones para camiseta_roja"
    )

    recomendadas_2 = recomendar_categorias(grafo, "camiseta_blanca", top_n=2)
    assert recomendadas_2 == ["camiseta_roja", "camiseta_roja_formal"], (
        "Error en las recomendaciones para camiseta_blanca"
    )

    recomendadas_3 = recomendar_categorias(grafo, "no_existe", top_n=3)
    assert recomendadas_3 == [], "Error: si la categoría no existe, debe devolver []"

    print("¡Felicidades! Todos los tests han pasado.")
