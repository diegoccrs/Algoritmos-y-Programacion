from personita import Persona

persona = Persona("Marron",1.69,"Hombre")

print(persona.genero)

info = persona.obtener()

print(info)

persona.change()

print(persona.obtener())