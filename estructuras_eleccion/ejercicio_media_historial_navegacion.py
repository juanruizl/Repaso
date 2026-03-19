"""
Ejercicio media: historial de navegación con dos pilas

INSTRUCCIONES
-------------
Completa la clase HistorialNavegacion para simular el funcionamiento básico
explicado en el tema:
- una pila para el historial pasado
- una pila para el historial futuro

La clase debe comportarse así:
- Se crea con una página inicial.
- visitar(url):
    * guarda la página actual en el historial pasado
    * cambia la página actual a la nueva url
    * vacía el historial futuro
- atras():
    * si se puede retroceder, guarda la página actual en el historial futuro,
      recupera la última del historial pasado y la devuelve
    * si no se puede, devuelve la página actual sin cambiar nada
- adelante():
    * si se puede avanzar, guarda la página actual en el historial pasado,
      recupera la última del historial futuro y la devuelve
    * si no se puede, devuelve la página actual sin cambiar nada
- pagina_actual(): devuelve la página actual

RESTRICCIONES
-------------
- Usa listas de Python como pilas.
- Sustituye cada 'pass' por tu solución.
- No modifiques los tests.
"""

class HistorialNavegacion:
    def __init__(self, pagina_inicial):
        pass

    def visitar(self, url):
        pass

    def atras(self):
        pass

    def adelante(self):
        pass

    def pagina_actual(self):
        pass


# =========================
# BLOQUE DE PRUEBAS (TESTS)
# =========================
if __name__ == "__main__":
    historial = HistorialNavegacion("inicio.com")

    assert historial.pagina_actual() == "inicio.com", "La página inicial no es correcta"

    historial.visitar("python.org")
    historial.visitar("uax.com")
    historial.visitar("chat.openai.com")

    assert historial.pagina_actual() == "chat.openai.com", "La página actual debería ser chat.openai.com"

    assert historial.atras() == "uax.com", "Al ir atrás debería volver a uax.com"
    assert historial.atras() == "python.org", "Al ir atrás otra vez debería volver a python.org"
    assert historial.pagina_actual() == "python.org", "La página actual debería ser python.org"

    assert historial.adelante() == "uax.com", "Al ir adelante debería volver a uax.com"
    assert historial.pagina_actual() == "uax.com", "La página actual debería ser uax.com"

    historial.visitar("github.com")
    assert historial.pagina_actual() == "github.com", "La página actual debería ser github.com"
    assert historial.adelante() == "github.com", "Tras visitar una página nueva no debe quedar historial futuro"

    assert historial.atras() == "uax.com", "Debe poder volver a uax.com"
    assert historial.atras() == "python.org", "Debe poder volver a python.org"
    assert historial.atras() == "inicio.com", "Debe poder volver a la página inicial"
    assert historial.atras() == "inicio.com", "Si no hay más historial, debe mantenerse en inicio.com"

    print("¡Felicidades! Todos los tests han pasado.")
