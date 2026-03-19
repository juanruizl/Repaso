"""
Ejercicio media - Persona con posicion y Espacio

INSTRUCCIONES
-------------
Completa las clases Persona y Espacio.

1) Clase Persona
   - Constructor con:
       nombre, anio_nacimiento, x=0, y=0
   - Debe guardar esos atributos.
   - Metodo mover_a(x, y): actualiza la posicion.
   - Metodo posicion(): devuelve una tupla (x, y).

2) Clase Espacio
   - Constructor con:
       nombre
   - Debe crear una lista vacia llamada personas.
   - Metodo agregar_persona(persona): anade la persona a la lista.
   - Metodo listar_personas(): devuelve una lista con los nombres.
   - Metodo contar_personas(): devuelve cuantas personas hay en el espacio.

No modifiques los tests.
Sustituye los pass por tu solucion.
"""


class Persona:
    def __init__(self, nombre, anio_nacimiento, x=0, y=0):
        pass

    def mover_a(self, x, y):
        pass

    def posicion(self):
        pass


class Espacio:
    def __init__(self, nombre):
        pass

    def agregar_persona(self, persona):
        pass

    def listar_personas(self):
        pass

    def contar_personas(self):
        pass


if __name__ == "__main__":
    ana = Persona("Ana", 2000)
    luis = Persona("Luis", 1998, 3, 4)

    assert ana.posicion() == (0, 0), "Error: la posicion inicial por defecto debe ser (0, 0)"
    assert luis.posicion() == (3, 4), "Error: la posicion inicial de Luis debe ser (3, 4)"

    ana.mover_a(10, 20)
    assert ana.posicion() == (10, 20), "Error: mover_a() no actualiza bien la posicion"

    parque = Espacio("Parque")
    assert parque.nombre == "Parque", "Error: el nombre del espacio no es correcto"
    assert parque.contar_personas() == 0, "Error: un espacio nuevo debe empezar vacio"
    assert parque.listar_personas() == [], "Error: la lista inicial de personas debe estar vacia"

    parque.agregar_persona(ana)
    assert parque.contar_personas() == 1, "Error: deberia haber 1 persona en el espacio"
    assert parque.listar_personas() == ["Ana"], "Error: listar_personas() no devuelve lo esperado tras anadir a Ana"

    parque.agregar_persona(luis)
    assert parque.contar_personas() == 2, "Error: deberia haber 2 personas en el espacio"
    assert parque.listar_personas() == ["Ana", "Luis"], "Error: el orden de listar_personas() no es correcto"

    print("¡Felicidades! Todos los tests han pasado.")
