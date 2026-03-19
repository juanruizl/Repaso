"""
Ejercicio facil - Clase Persona basica

INSTRUCCIONES
-------------
Completa la clase Persona.

Debe cumplir lo siguiente:
1) El constructor debe recibir:
   - nombre
   - anio_nacimiento
2) Debe guardar esos valores como atributos del objeto.
3) Debe tener un metodo edad_en(anio_actual) que devuelva la edad.
4) Debe tener un metodo saludar(anio_actual) que devuelva exactamente:
   "Hola, me llamo NOMBRE y tengo EDAD anos"

No modifiques los tests.
Sustituye los pass por tu solucion.
"""


class Persona:
    def __init__(self, nombre, anio_nacimiento):
        pass

    def edad_en(self, anio_actual):
        pass

    def saludar(self, anio_actual):
        pass


if __name__ == "__main__":
    ana = Persona("Ana", 2000)
    luis = Persona("Luis", 1998)

    assert ana.nombre == "Ana", "Error: el atributo nombre de Ana no es correcto"
    assert ana.anio_nacimiento == 2000, "Error: el anio de nacimiento de Ana no es correcto"
    assert luis.nombre == "Luis", "Error: el atributo nombre de Luis no es correcto"
    assert luis.anio_nacimiento == 1998, "Error: el anio de nacimiento de Luis no es correcto"

    assert ana.edad_en(2025) == 25, "Error: la edad de Ana en 2025 debe ser 25"
    assert luis.edad_en(2025) == 27, "Error: la edad de Luis en 2025 debe ser 27"
    assert ana.edad_en(2010) == 10, "Error: la edad de Ana en 2010 debe ser 10"

    assert ana.saludar(2025) == "Hola, me llamo Ana y tengo 25 anos", "Error en saludar() para Ana"
    assert luis.saludar(2025) == "Hola, me llamo Luis y tengo 27 anos", "Error en saludar() para Luis"

    print("¡Felicidades! Todos los tests han pasado.")
