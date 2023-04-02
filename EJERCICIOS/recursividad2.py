"""Funcion recursiva que invierte una palabra"""

def invertir_palabra(texto):
    if len(texto) == 0:
        return texto
    else:
        return invertir_palabra(texto[1:]) + texto[0]
 
def main():
    palabra = input("Ingrese una palabra: ")
    print(invertir_palabra(palabra))

main()