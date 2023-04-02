elementos = {
    "hidrogeno": {
        "numero":1,
        "peso": 1.00794,
        "simbolo":"H"
    },
    "helio": {
        "numero":2,
        "peso": 4.002602,
        "simbolo": "He"
    }
}

hidrogeno = elementos["hidrogeno"]   # imprime lo que esta dentro de hidrogeno
print(hidrogeno)

peso_helio = elementos["helio"]["peso"] # imprime lo que esta dentro de peso del helio
print(peso_helio)

print("\n")

secciones = [
    ["Maria","Andres","Pedro"],
    ["Stefania","Gabriel","Julia","Manuel"]
]

for seccion in secciones:
    for estudiante in seccion:
        print(f"El nombre del estudiante es {estudiante}")