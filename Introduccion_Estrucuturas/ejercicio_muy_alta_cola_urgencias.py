"""
Ejercicio muy alto: cola de prioridad con heapq

INSTRUCCIONES
-------------
Completa la clase ColaUrgencias para gestionar pacientes de una sala de urgencias.

Cada paciente tendra:
- nombre (str)
- gravedad (int)

Reglas:
1) Cuanto MAYOR sea la gravedad, antes debe ser atendido el paciente.
2) Si dos pacientes tienen la misma gravedad, debe atenderse antes al que llego primero.
3) Debes usar el modulo heapq.

Debes implementar:
- __init__(self):
    Inicializa la estructura interna necesaria.

- agregar_paciente(self, nombre, gravedad):
    Inserta un paciente en la cola.

- atender_siguiente(self):
    Extrae y devuelve una tupla (nombre, gravedad) del siguiente paciente.
    Si no hay pacientes, debe devolver None.

- hay_pacientes(self):
    Devuelve True si quedan pacientes por atender y False si no.

PISTA
-----
heapq implementa un min-heap. Para que una gravedad mayor salga antes,
puedes transformar el valor de prioridad de alguna forma.

RESTRICCIONES
-------------
- Sustituye cada 'pass' por tu solucion.
- No modifiques los tests.
"""

import heapq


class ColaUrgencias:
    def __init__(self):
        pass

    def agregar_paciente(self, nombre, gravedad):
        pass

    def atender_siguiente(self):
        pass

    def hay_pacientes(self):
        pass


# =========================
# BLOQUE DE PRUEBAS (TESTS)
# =========================
if __name__ == "__main__":
    cola = ColaUrgencias()
    assert cola.hay_pacientes() is False, "Una cola nueva debe empezar vacia"
    assert cola.atender_siguiente() is None, "Si no hay pacientes debe devolver None"

    cola.agregar_paciente("Ana", 1)
    cola.agregar_paciente("Luis", 3)
    cola.agregar_paciente("Marta", 2)
    cola.agregar_paciente("Carlos", 3)

    assert cola.hay_pacientes() is True, "Debe haber pacientes en la cola"
    assert cola.atender_siguiente() == ("Luis", 3), "Debe salir primero el de mayor gravedad"
    assert cola.atender_siguiente() == ("Carlos", 3), "A igualdad de gravedad, sale antes quien llego primero"
    assert cola.atender_siguiente() == ("Marta", 2), "Luego debe salir la siguiente gravedad"
    assert cola.atender_siguiente() == ("Ana", 1), "El menos grave debe salir al final"
    assert cola.atender_siguiente() is None, "Si ya no quedan pacientes debe devolver None"
    assert cola.hay_pacientes() is False, "Despues de atender a todos no deben quedar pacientes"

    cola2 = ColaUrgencias()
    cola2.agregar_paciente("P1", 2)
    cola2.agregar_paciente("P2", 2)
    cola2.agregar_paciente("P3", 2)
    assert cola2.atender_siguiente() == ("P1", 2), "Debe respetar el orden de llegada en empates"
    assert cola2.atender_siguiente() == ("P2", 2), "Debe respetar el orden de llegada en empates"
    assert cola2.atender_siguiente() == ("P3", 2), "Debe respetar el orden de llegada en empates"

    print("¡Felicidades! Todos los tests han pasado.")
