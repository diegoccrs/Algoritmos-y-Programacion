"""
Funcion que determina si dos palabras tienen la misma cantidad de letras y las mismas letras
"""

def es_anagrama(txt1,txt2):
    if sorted(txt1) == sorted(txt2):
        return "Es anagrama"
    else:
        return "No es anagrama"

print(es_anagrama("roma","amor"))