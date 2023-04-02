"""
Una escuela está tratando de tomar una foto anual de todos los estudiantes. Se les pide a
los estudiantes que se paren en una sola fila en orden no decreciente por altura. Suponga
que este orden esta representado por la lista de enteros donde expected[i] es la altura
esperada del i-ésimo estudiante en la fila.
Se le proporciona una lista de enteros heights que representa el orden actual en el que se
encuentran los estudiantes. Cada heights[i] es la altura del i-ésimo estudiante en la fila.

Realice una función en que devuelva el número de índices donde heights[i] != esperado[i].

Input heights = [1,1,4,2,1,3] y expected - [1,1,1,2,3,4]
Output: 3

Input: heights = [5,1,2,3,4] y expected = [1,2,3,4,5]
Output: 5
"""

def different_heights(heights, expected, counter):
    for i in range(0, len(heights)):
        if heights[i] != expected[i]:
            counter += 1
    return counter

# heights = [5, 1, 2, 3, 4]
# expected = [1, 2, 3, 4, 5]

heights = [1, 1, 4, 2, 1, 3]
expected = [1, 1, 1, 2, 3, 4]

counter = 0

print(different_heights(heights, expected, counter))