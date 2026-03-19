"""
Ejercicio fácil: buscar una persona por nombre dentro de un espacio

INSTRUCCIONES
-------------
Completa la función buscar_persona_por_nombre(espacio, nombre) para que:
- recorra la lista de personas del espacio,
- devuelva el objeto Persona cuyo nombre coincida exactamente,
- y devuelva None si no existe ninguna coincidencia.

REGLAS
------
- No uses librerías externas.
- Sustituye 'pass' por tu solución.
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


def buscar_persona_por_nombre(espacio, nombre):
    pass


# =========================
# BLOQUE DE PRUEBAS (TESTS)
# =========================
if __name__ == "__main__":
    parque = Espacio("Parque")
    ana = Persona("Ana", 1, 2)
    luis = Persona("Luis", 3, 4)
    marta = Persona("Marta", 5, 6)

    parque.agregar_persona(ana)
    parque.agregar_persona(luis)
    parque.agregar_persona(marta)

    resultado_ana = buscar_persona_por_nombre(parque, "Ana")
    assert resultado_ana is ana, "Error: debe devolver el objeto de Ana"

    resultado_luis = buscar_persona_por_nombre(parque, "Luis")
    assert resultado_luis is luis, "Error: debe devolver el objeto de Luis"

    resultado_no_existe = buscar_persona_por_nombre(parque, "Carlos")
    assert resultado_no_existe is None, "Error: si no existe debe devolver None"

    parque_vacio = Espacio("Vacío")
    assert buscar_persona_por_nombre(parque_vacio, "Ana") is None, (
        "Error: en un espacio vacío debe devolver None"
    )

    print("¡Felicidades! Todos los tests han pasado.")
