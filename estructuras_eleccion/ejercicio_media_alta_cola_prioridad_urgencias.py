"""
Ejercicio media-alta: cola de prioridad para urgencias

INSTRUCCIONES
-------------
Completa la clase GestorUrgencias usando heapq para gestionar pacientes.

Cada paciente tendrá:
- nombre (str)
- gravedad (int)

Convención de gravedad:
- 1 -> más urgente
- 2 -> urgencia media
- 3 -> menos urgente

Debes implementar:
- registrar_paciente(nombre, gravedad): añade un paciente a la cola
  * Si gravedad no está entre 1 y 3, lanza ValueError
- atender_siguiente():
  * devuelve el nombre del paciente que debe ser atendido primero
  * elimina ese paciente de la cola
  * si no hay pacientes, devuelve None
- pacientes_pendientes(): devuelve cuántos pacientes quedan

MUY IMPORTANTE
--------------
Si dos pacientes tienen la misma gravedad, debe atenderse primero
al que llegó antes.

PISTA
-----
Guarda en el heap tuplas del tipo:
(gravedad, orden_llegada, nombre)

RESTRICCIONES
-------------
- Usa heapq.
- Sustituye cada 'pass' por tu solución.
- No modifiques los tests.
"""

import heapq


class GestorUrgencias:
    def __init__(self):
        pass

    def registrar_paciente(self, nombre, gravedad):
        pass

    def atender_siguiente(self):
        pass

    def pacientes_pendientes(self):
        pass


# =========================
# BLOQUE DE PRUEBAS (TESTS)
# =========================
if __name__ == "__main__":
    gestor = GestorUrgencias()

    assert gestor.pacientes_pendientes() == 0, "Al empezar no debe haber pacientes"
    assert gestor.atender_siguiente() is None, "Si no hay pacientes, debe devolver None"

    gestor.registrar_paciente("Ana", 2)
    gestor.registrar_paciente("Luis", 1)
    gestor.registrar_paciente("Marta", 3)
    gestor.registrar_paciente("Carlos", 1)
    gestor.registrar_paciente("Elena", 2)

    assert gestor.pacientes_pendientes() == 5, "Deben quedar 5 pacientes"

    assert gestor.atender_siguiente() == "Luis", "El primer paciente debería ser Luis"
    assert gestor.atender_siguiente() == "Carlos", "Después debería salir Carlos por mismo nivel y orden de llegada"
    assert gestor.atender_siguiente() == "Ana", "Después debería salir Ana"
    assert gestor.atender_siguiente() == "Elena", "Después debería salir Elena"
    assert gestor.atender_siguiente() == "Marta", "La última debería ser Marta"
    assert gestor.atender_siguiente() is None, "Ya no deberían quedar pacientes"

    try:
        gestor.registrar_paciente("Error", 5)
        raise AssertionError("Se esperaba ValueError para una gravedad inválida")
    except ValueError:
        pass

    print("¡Felicidades! Todos los tests han pasado.")
