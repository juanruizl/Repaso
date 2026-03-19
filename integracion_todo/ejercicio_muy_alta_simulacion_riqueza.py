"""
Ejercicio muy alto: simular riqueza por turnos en un espacio

INSTRUCCIONES
-------------
Completa la función simular_riqueza(personas, monedas, movimientos_por_turno)
para ejecutar una pequeña simulación por turnos.

Datos de entrada:
- personas: lista de objetos Persona
- monedas: lista de objetos Moneda
- movimientos_por_turno: lista de diccionarios. Cada diccionario representa un turno y
  asocia el nombre de una persona con una nueva posición (x, y).

Qué debe hacer en cada turno:
1) Mover a cada persona según el diccionario de ese turno.
2) Comprobar si alguna persona cae en la misma posición que una moneda no recogida.
   Si ocurre, la persona suma el valor de esa moneda y la moneda queda marcada como recogida.
3) Al final de cada turno, guardar la riqueza total acumulada.

La función debe devolver una tupla con esta forma:
    (historial_riqueza_total, riqueza_final_por_persona)

Donde:
- historial_riqueza_total es una lista con la riqueza total tras cada turno.
- riqueza_final_por_persona es un diccionario con el número final de monedas de cada persona.

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
        self.monedas = 0

    def posicion(self):
        return (self.x, self.y)

    def mover_a(self, x, y):
        self.x = x
        self.y = y


class Moneda:
    def __init__(self, x, y, valor=1):
        self.x = x
        self.y = y
        self.valor = valor
        self.recogida = False

    def posicion(self):
        return (self.x, self.y)


def simular_riqueza(personas, monedas, movimientos_por_turno):
    pass


# =========================
# BLOQUE DE PRUEBAS (TESTS)
# =========================
if __name__ == "__main__":
    ana = Persona("Ana", 0, 0)
    luis = Persona("Luis", 1, 0)
    marta = Persona("Marta", 2, 0)

    monedas = [
        Moneda(1, 1, 2),
        Moneda(2, 2, 3),
        Moneda(0, 2, 1),
    ]

    movimientos = [
        {"Ana": (1, 1), "Luis": (1, 0), "Marta": (2, 2)},
        {"Ana": (0, 2), "Luis": (2, 2), "Marta": (2, 2)},
        {"Ana": (0, 2), "Luis": (1, 1), "Marta": (0, 0)},
    ]

    historial, riqueza_final = simular_riqueza([ana, luis, marta], monedas, movimientos)

    # Turno 1: Ana recoge 2, Marta recoge 3 -> total 5
    # Turno 2: Ana recoge 1 -> total 6
    # Turno 3: no se recoge nada -> total 6
    assert historial == [5, 6, 6], "Error en el historial de riqueza total"

    assert riqueza_final == {"Ana": 3, "Luis": 0, "Marta": 3}, (
        "Error en la riqueza final por persona"
    )

    # Comprobar que las monedas han quedado como recogidas
    assert all(moneda.recogida for moneda in monedas), (
        "Error: todas las monedas deberían estar recogidas al final"
    )

    print("¡Felicidades! Todos los tests han pasado.")
