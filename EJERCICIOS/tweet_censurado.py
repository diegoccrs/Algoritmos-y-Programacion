"""El usuario debera ingresar un tweet y devolverle las palabras dentro de la lista censuradas (*****)"""

tweet = input("Ingrese un tweet: ")

palabras_censuradas = ["racismo", "terrorista", "peligro", "miedo", "odio"]

if palabras_censuradas[0] in tweet:
    tweet = tweet.replace(palabras_censuradas[0],"*****")
if palabras_censuradas[1] in tweet:
    tweet = tweet.replace(palabras_censuradas[1],"*****")
if palabras_censuradas[2] in tweet:
    tweet = tweet.replace(palabras_censuradas[2],"*****")
if palabras_censuradas[3] in tweet:
    tweet = tweet.replace(palabras_censuradas[3],"*****")
if palabras_censuradas[4] in tweet:
    tweet = tweet.replace(palabras_censuradas[4],"*****")

print(tweet)