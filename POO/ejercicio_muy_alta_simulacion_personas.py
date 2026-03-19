"""
Ejercicio muy alta - Simulacion con Persona, Espacio y utils

INSTRUCCIONES
-------------
Completa las clases y funciones de este archivo.

Objetivo:
Modelar un pequeno sistema con personas dentro de espacios, siguiendo la linea
practica del tema de POO.

Debes completar:

1) Clase Persona
   Constructor:
      nombre, anio_nacimiento, espacio, x=0, y=0

   Debe guardar:
      nombre, anio_nacimiento, espacio, x, y

   Ademas, al crear una persona, debe anadirse automaticamente al espacio recibido.

   Metodos:
      - saludar(anio_actual):
            devuelve "Hola, me llamo NOMBRE y tengo EDAD anos"
      - mover_a(x, y):
            cambia la posicion de la persona
      - posicion():
            devuelve (x, y)
      - hablar(con_quien, mensaje):
            si ambas personas estan en el mismo espacio, devuelve:
            "NOMBRE1 le dice a NOMBRE2: MENSAJE"
            si no estan en el mismo espacio, devuelve:
            "NOMBRE1 no puede hablar con NOMBRE2"
      - mover_hacia(otra_persona):
            si estan en el mismo espacio, mueve a la persona a la posicion de la otra
            y devuelve True
            si no, no la mueve y devuelve False
      - salir_del_espacio():
            saca a la persona de su espacio actual y la mueve automaticamente al
            espacio especial EXTERIOR, devolviendo el nuevo espacio

2) Clase Espacio
   Constructor:
      nombre

   Debe crear una lista vacia llamada personas.

   Metodos:
      - agregar_persona(persona):
            anade la persona si no estaba ya en el espacio y actualiza persona.espacio
      - eliminar_persona(persona):
            la quita del espacio si estaba y devuelve True; si no estaba, devuelve False
      - listar_personas():
            devuelve una lista con los nombres de las personas
      - contar_personas():
            devuelve cuantas personas hay
      - mover_persona(persona, x, y):
            si la persona esta en ese espacio, la mueve y devuelve True; si no, False
      - buscar_persona_por_nombre(nombre):
            devuelve el objeto Persona correspondiente o None si no existe

3) Funciones auxiliares
      - calcular_distancia(persona1, persona2):
            distancia euclidiana entre sus posiciones
      - estan_en_misma_posicion(persona1, persona2):
            devuelve True o False
      - obtener_personas_cercanas(persona, espacio, distancia):
            devuelve una lista de nombres de personas del espacio cuya distancia a persona
            sea menor o igual que el valor dado, sin incluir a la propia persona
      - calcular_persona_mas_cercana(persona, espacio):
            devuelve el nombre de la persona mas cercana dentro del espacio
            si no hay ninguna otra persona, devuelve None

4) Espacio especial
   Al final del archivo ya tienes creada una variable global llamada EXTERIOR.
   Debes usarla en salir_del_espacio().

No modifiques los tests.
Sustituye los pass por tu solucion.
"""

from math import sqrt


class Persona:
    def __init__(self, nombre, anio_nacimiento, espacio, x=0, y=0):
        pass

    def saludar(self, anio_actual):
        pass

    def mover_a(self, x, y):
        pass

    def posicion(self):
        pass

    def hablar(self, con_quien, mensaje):
        pass

    def mover_hacia(self, otra_persona):
        pass

    def salir_del_espacio(self):
        pass


class Espacio:
    def __init__(self, nombre):
        pass

    def agregar_persona(self, persona):
        pass

    def eliminar_persona(self, persona):
        pass

    def listar_personas(self):
        pass

    def contar_personas(self):
        pass

    def mover_persona(self, persona, x, y):
        pass

    def buscar_persona_por_nombre(self, nombre):
        pass


def calcular_distancia(persona1, persona2):
    pass


def estan_en_misma_posicion(persona1, persona2):
    pass


def obtener_personas_cercanas(persona, espacio, distancia):
    pass


def calcular_persona_mas_cercana(persona, espacio):
    pass


EXTERIOR = Espacio("Exterior")


if __name__ == "__main__":
    parque = Espacio("Parque")
    oficina = Espacio("Oficina")

    ana = Persona("Ana", 2000, parque, 0, 0)
    luis = Persona("Luis", 1998, parque, 3, 4)
    marta = Persona("Marta", 2001, parque, 1, 1)
    juan = Persona("Juan", 1997, oficina, 10, 10)

    # Creacion y pertenencia a espacios
    assert parque.listar_personas() == ["Ana", "Luis", "Marta"], "Error: las personas no se anaden bien al parque"
    assert oficina.listar_personas() == ["Juan"], "Error: Juan debe estar en la oficina"
    assert EXTERIOR.listar_personas() == [], "Error: Exterior debe empezar vacio"

    # Saludo y posicion
    assert ana.saludar(2025) == "Hola, me llamo Ana y tengo 25 anos", "Error en saludar() de Ana"
    assert luis.posicion() == (3, 4), "Error: la posicion inicial de Luis debe ser (3, 4)"

    # Hablar en el mismo espacio / distinto espacio
    assert ana.hablar(luis, "Hola") == "Ana le dice a Luis: Hola", "Error: hablar() en el mismo espacio no funciona"
    assert ana.hablar(juan, "Hola") == "Ana no puede hablar con Juan", "Error: hablar() entre espacios distintos no funciona"

    # Distancia y misma posicion
    assert calcular_distancia(ana, luis) == 5.0, "Error: la distancia entre Ana y Luis debe ser 5.0"
    assert estan_en_misma_posicion(ana, marta) is False, "Error: Ana y Marta no estan en la misma posicion"

    # Mover dentro del espacio
    parque.mover_persona(ana, 1, 1)
    assert ana.posicion() == (1, 1), "Error: mover_persona() no mueve bien a Ana"
    assert estan_en_misma_posicion(ana, marta) is True, "Error: ahora Ana y Marta deberian coincidir"

    # Personas cercanas
    cercanas_a_ana = obtener_personas_cercanas(ana, parque, 0)
    assert cercanas_a_ana == ["Marta"], "Error: a distancia 0 de Ana solo debe estar Marta"

    cercanas_a_marta = obtener_personas_cercanas(marta, parque, 5)
    assert cercanas_a_marta == ["Ana", "Luis"], "Error: las personas cercanas a Marta no son correctas"

    # Persona mas cercana
    assert calcular_persona_mas_cercana(luis, parque) == "Ana", "Error: la persona mas cercana a Luis debe ser Ana"
    assert calcular_persona_mas_cercana(juan, oficina) is None, "Error: Juan esta solo en la oficina"

    # Buscar por nombre
    assert parque.buscar_persona_por_nombre("Luis") is luis, "Error: buscar_persona_por_nombre('Luis') debe devolver a Luis"
    assert parque.buscar_persona_por_nombre("Pedro") is None, "Error: buscar_persona_por_nombre('Pedro') debe devolver None"

    # mover_hacia
    assert luis.mover_hacia(marta) is True, "Error: Luis y Marta estan en el mismo espacio, deberia poder moverse hacia ella"
    assert luis.posicion() == (1, 1), "Error: Luis deberia haberse movido a la posicion de Marta"
    assert juan.mover_hacia(ana) is False, "Error: Juan no esta en el mismo espacio que Ana"
    assert juan.posicion() == (10, 10), "Error: Juan no deberia haberse movido"

    # salir_del_espacio
    nuevo_espacio = ana.salir_del_espacio()
    assert nuevo_espacio is EXTERIOR, "Error: salir_del_espacio() debe devolver EXTERIOR"
    assert ana.espacio is EXTERIOR, "Error: Ana debe pasar a estar en EXTERIOR"
    assert parque.listar_personas() == ["Luis", "Marta"], "Error: Ana debe haber salido del parque"
    assert EXTERIOR.listar_personas() == ["Ana"], "Error: Ana debe aparecer en EXTERIOR"

    print("¡Felicidades! Todos los tests han pasado.")
