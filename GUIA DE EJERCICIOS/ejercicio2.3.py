# 2.3 CODIGO MORSE
# A continuación se te presentan 5 códigos postales escritos en código Morse
# Todos almacenados en un mismo string y separados por “*”. 
# Tu labor consiste en descifrar cuáles son los números que componen cada código.

# codigos_postales = "...._ __... ..... ..___*.____ ___.. ___.. _____*_.... ..___ ...__ _....*
# ..... __... .____ .____*___.. ...._ ____. ____.*"

# Output: 
# 4752
# 1880
# 6236
# 5711
# 8499

codigos_postales = "...._ __... ..... ..___*.____ ___.. ___.. _____*_.... ..___ ...__ _....*..... __... .____ .____*___.. ...._ ____. ____.*"

if ".____" in codigos_postales:
    codigos_postales = codigos_postales.replace(".____","1")

if "..___" in codigos_postales:
    codigos_postales = codigos_postales.replace("..___","2")

if "...__" in codigos_postales:
    codigos_postales = codigos_postales.replace("...__","3")

if "...._" in codigos_postales:
    codigos_postales = codigos_postales.replace("...._","4")

if "....." in codigos_postales:
    codigos_postales = codigos_postales.replace(".....","5")

if "_...." in codigos_postales:
    codigos_postales = codigos_postales.replace("_....","6")

if "__..." in codigos_postales:
    codigos_postales = codigos_postales.replace("__...","7")

if "___.." in codigos_postales:
    codigos_postales = codigos_postales.replace("___..","8")

if "____." in codigos_postales:
    codigos_postales = codigos_postales.replace("____.","9")

if "_____" in codigos_postales:
    codigos_postales = codigos_postales.replace("_____","0")

if "*" in codigos_postales:
    codigos_postales = codigos_postales.replace("*","\n")

print(codigos_postales)