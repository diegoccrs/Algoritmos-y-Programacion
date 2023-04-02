# 2.6 MAD LIBS
# Este juego consiste en solicitar varias palabras en inglés por teclado 
# Y luego insertarlas en un texto con espacios vacíos para crear una historia.

# Las palabras a solicitar son:
# 6 adjetivos (adj)
# 4 sustantivos plurales (plnoun)
# 1 ciudad (city)
# 1 lugar (place)
# 1 celebridad (cel)
# 1 número (num)
# 1 verbo (verb)
# 2 partes del cuerpo (body)
# 1 letra del alfabeto (letter)
# 2 sustantivos singulares (noun)
# 1 nombre femenino (name)
# 1 pieza de ropa (clothes)
# El orden de las palabras en el texto es: 
# adj1, noun1, plnoun1, name1, adj2, clothes, noun2, city1, plnoun2, adj3, body1, letter1, 
# cel1, plnoun3, adj4, place1, body2, adj5, adj6, verb1, plnoun4, num1.

# Como output se espera el texto impreso con las palabras dadas.

# historia = "There are many __ ways to choose a/an __ to read. First, you could ask for recommendations from your friends and __. Just don't ask Aunt __ -- she only reads __ books with __-ripping goddesses on the cover. If your friends and family are no help, try checking out the __ Review in 'The __ Times'. If the __ featured there are too __ for your taste, try something a little more low-__, like __: 'The __ Magazine', or '__ Magazine'. You could also choose a book the __-fashioned way. Head to your local library or __ and browse the shelves until something catches your __. Or, you could save yourself a whole lot of __ trouble and log on to www.bookish.com, the __ new website to __ for books! With all the time you'll save not having to search for __, you can read __ more books!"

historia = "There are many __ ways to choose a/an __ to read. First, you could ask for recommendations from your friends and __. Just don't ask Aunt __ -- she only reads __ books with __-ripping goddesses on the cover. If your friends and family are no help, try checking out the __ Review in 'The __ Times'. If the __ featured there are too __ for your taste, try something a little more low-__, like __: 'The __ Magazine', or '__ Magazine'. You could also choose a book the __-fashioned way. Head to your local library or __ and browse the shelves until something catches your __. Or, you could save yourself a whole lot of __ trouble and log on to www.bookish.com, the __ new website to __ for books! With all the time you'll save not having to search for __, you can read __ more books!"

print("¡Bienvenido a mi juego de 'Mad Libs'!\nIngresa las siguientes palabras EN INGLÉS para crear tu historia:\n")

adj1 = input("Adjetivo: ")
noun1 = input("Sustantivo: ")
plnoun1 = input("Sustantivo plural: ")
name1 = input("Nombre femenino: ")
adj2 = input("Adjetivo: ")
clothes = input("Artículo de ropa: ")
noun2 = input("Sustantivo: ")
city1 = input("Ciudad: ")
plnoun2 = input("Sustantivo plural: ")
adj3 = input("Adjetivo: ")
body1 = input("Parte del cuerpo: ")
letter1 = input("Letra del alfabeto: ")
cel1 = input("Celebridad: ")
plnoun3 = input("Sustantivo plural: ")
adj4 = input("Adjetivo: ")
place1 = input("Lugar: ")
body2 = input("Parte del cuerpo: ")
adj5 = input("Adjetivo: ")
adj6 = input("Adjetivo: ")
verb1 = input("Verbo: ")
plnoun4 = input("Sustantivo plural: ")
num1 = input("Número: ")

print("\n")

historia = historia.replace("__","{}")

print(historia.format(adj1,noun1,plnoun1,name1,adj2,clothes,noun2,city1,plnoun2,adj3,body1,letter1,cel1,plnoun3,adj4,place1,body2,adj5,adj6,verb1,plnoun4,num1))