#Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
# pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

currency = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

election = input("Introduce una divisa: ")

print(currency.get(election.title(),"La divisa no esta."))