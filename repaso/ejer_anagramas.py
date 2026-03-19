"""
Ejercicio de autoevaluación: Comprobar anagramas

INSTRUCCIONES
-------------
Completa la función son_anagramas(palabra1, palabra2) para que devuelva True
si ambas cadenas son anagramas, o False en caso contrario.

Un anagrama es una palabra o frase formada al reorganizar las letras de otra,
usando todas las letras originales exactamente una vez.

Requisitos:
- Debes ignorar los espacios en blanco.
- Debes ignorar si las letras están en mayúsculas o minúsculas.
- Intenta resolverlo usando métodos básicos de cadenas, listas o diccionarios.

Ejemplos:
- son_anagramas("Roma", "Amor") debe devolver True
- son_anagramas("Python", "Java") debe devolver False
- son_anagramas("Tom Marvolo Riddle", "I am Lord Voldemort") debe devolver True

TU TAREA
--------
Sustituye 'pass' por tu solución.
"""

def son_anagramas(palabra1, palabra2):
    pass


# =========================
# BLOQUE DE PRUEBAS (TESTS)
# =========================
if __name__ == "__main__":
    assert son_anagramas("Roma", "Amor") == True, "Error: 'Roma' y 'Amor' SON anagramas"
    assert son_anagramas("Listen", "Silent") == True, "Error: 'Listen' y 'Silent' SON anagramas"
    assert son_anagramas("Hola", "Mundo") == False, "Error: 'Hola' y 'Mundo' NO son anagramas"
    assert son_anagramas("Tom Marvolo Riddle", "I am Lord Voldemort") == True, "Error: Fallo al ignorar espacios o mayúsculas"
    assert son_anagramas("aab", "abb") == False, "Error: 'aab' y 'abb' NO son anagramas, la cantidad de letras debe ser exacta"
    assert son_anagramas("a", "a ") == True, "Error: Asegúrate de limpiar bien los espacios al final"
    
    print("¡Felicidades! Todos los tests han pasado.")