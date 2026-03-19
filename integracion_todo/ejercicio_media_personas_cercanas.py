"""
Ejercicio medio: obtener personas cercanas en un espacio

INSTRUCCIONES
-------------
Completa estas dos funciones:

1) calcular_distancia(persona1, persona2)
   Debe devolver la distancia euclidiana entre dos personas.

2) obtener_personas_cercanas(persona, espacio, distancia_maxima)
   Debe devolver una lista con los NOMBRES de las personas que están a una
   distancia menor o igual que distancia_maxima respecto a la persona dada.

REGLAS
------
- No incluyas a la propia persona en el resultado.
- Devuelve los nombres ordenados por distancia ascendente.
- Si hay empate de distancia, desempata por orden alfabético del nombre.
- No uses librerías externas.
- Sustituye cada 'pass' por tu solución.
- No modifiques los tests.
"""


class Persona:
    def __init__(self, nombre, x=0, y=0):
        self.nombre = nombre
        self.x = x
        self.y = y


class Espacio:
    def __init__(self, nombre):
        self.nombre = nombre
        self.personas = []

    def agregar_persona(self, persona):
        self.personas.append(persona)


def calcular_distancia(persona1, persona2):
    pass


def obtener_personas_cercanas(persona, espacio, distancia_maxima):
    pass


# =========================
# BLOQUE DE PRUEBAS (TESTS)
# =========================
if __name__ == "__main__":
    espacio = Espacio("Plaza")

    ana = Persona("Ana", 0, 0)
    luis = Persona("Luis", 3, 4)      # distancia 5 a Ana
    marta = Persona("Marta", 1, 1)    # distancia sqrt(2) a Ana
    pablo = Persona("Pablo", 6, 8)    # distancia 10 a Ana
    alberto = Persona("Alberto", -1, -1)  # distancia sqrt(2) a Ana

    for persona in [ana, luis, marta, pablo, alberto]:
        espacio.agregar_persona(persona)

    distancia_ana_luis = calcular_distancia(ana, luis)
    assert abs(distancia_ana_luis - 5.0) < 1e-9, "Error en calcular_distancia()"

    cercanas_ana_2 = obtener_personas_cercanas(ana, espacio, 2)
    assert cercanas_ana_2 == ["Alberto", "Marta"], (
        "Error: con distancia 2, Ana debe tener cerca a Alberto y Marta"
    )

    cercanas_ana_5 = obtener_personas_cercanas(ana, espacio, 5)
    assert cercanas_ana_5 == ["Alberto", "Marta", "Luis"], (
        "Error: con distancia 5, Ana debe tener cerca a Alberto, Marta y Luis"
    )

    cercanas_pablo_1 = obtener_personas_cercanas(pablo, espacio, 1)
    assert cercanas_pablo_1 == [], "Error: Pablo no debería tener personas a distancia <= 1"

    print("¡Felicidades! Todos los tests han pasado.")
