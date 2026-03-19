"""
Ejercicio media-alta - Herencia, atributo de clase y __str__

INSTRUCCIONES
-------------
Completa las clases Animal, Perro y Gato.

Requisitos:
1) Animal debe tener un atributo de clase:
      reino = "Animal"
2) El constructor de Animal debe recibir:
      nombre
   y guardarlo como atributo.
3) Animal debe tener:
      - sonido(): devuelve "sonido generico"
      - presentarse(): devuelve "Soy NOMBRE del reino Animal"
      - __str__(): devuelve "Animal(nombre=NOMBRE)"
4) Perro debe heredar de Animal y sobrescribir:
      - sonido(): devuelve "guau"
      - __str__(): devuelve "Perro(nombre=NOMBRE)"
5) Gato debe heredar de Animal y sobrescribir:
      - sonido(): devuelve "miau"
      - __str__(): devuelve "Gato(nombre=NOMBRE)"

No modifiques los tests.
Sustituye los pass por tu solucion.
"""


class Animal:
    reino = "Animal"

    def __init__(self, nombre):
        pass

    def sonido(self):
        pass

    def presentarse(self):
        pass

    def __str__(self):
        pass


class Perro(Animal):
    def sonido(self):
        pass

    def __str__(self):
        pass


class Gato(Animal):
    def sonido(self):
        pass

    def __str__(self):
        pass


if __name__ == "__main__":
    animal = Animal("Bicho")
    perro = Perro("Rex")
    gato = Gato("Misu")

    assert Animal.reino == "Animal", "Error: el atributo de clase reino debe valer 'Animal'"
    assert animal.nombre == "Bicho", "Error: el nombre del animal no se guarda bien"
    assert perro.nombre == "Rex", "Error: el nombre del perro no se hereda bien"
    assert gato.nombre == "Misu", "Error: el nombre del gato no se hereda bien"

    assert animal.sonido() == "sonido generico", "Error: Animal.sonido() no es correcto"
    assert perro.sonido() == "guau", "Error: Perro.sonido() debe sobrescribirse"
    assert gato.sonido() == "miau", "Error: Gato.sonido() debe sobrescribirse"

    assert animal.presentarse() == "Soy Bicho del reino Animal", "Error: presentarse() en Animal no es correcto"
    assert perro.presentarse() == "Soy Rex del reino Animal", "Error: presentarse() heredado en Perro no funciona bien"
    assert gato.presentarse() == "Soy Misu del reino Animal", "Error: presentarse() heredado en Gato no funciona bien"

    assert str(animal) == "Animal(nombre=Bicho)", "Error en __str__() de Animal"
    assert str(perro) == "Perro(nombre=Rex)", "Error en __str__() de Perro"
    assert str(gato) == "Gato(nombre=Misu)", "Error en __str__() de Gato"

    print("¡Felicidades! Todos los tests han pasado.")
