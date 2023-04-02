"""def if_type_num(div,count,ram):      #NUMERO ABUNDANTE,PERFECTO,DEFICIENTE DE MANERA RECURSIVA
    if count + 1 == div:
        if sum(ram) > div:
            return "Abundante"
        elif sum(ram) == div:
            return "Perfecto"
        else:
            return "Deficiente" 
    else:
        if div%count == 0:
            ram.append(count)
        return if_type_num(div,count+1,ram)

print(if_type_num(60,1,[]))"""


"""
n = int(input("Ingrese el número:",))      #NUMERO ABUNDANTE NORMAL 
count =  1
suma = 0

while (count<n):
  if (n%count==0):
    suma+=count
    print (count)
  count = count + 1
if (suma>(n)):
  print ("El numero es abundante")
else:
  print ("El número no es abundante")
"""

"""def es_primo(num, n=2):                   #NUMERO PRIMO RECURSIVO
    if n >= num:
        print("Es primo")
        return True
    elif num % n != 0:
        return es_primo(num, n + 1)
    else:
        print("No es primo", n, "es divisor")
        return False"""

"""
if numero > 1:                                 #NUMERO PRIMO NORMAL
    cont = 0
    for i in range(2,numero):
        resto = numero%i
        if resto == 0:
            cont += 1
    if cont == 0:
        print("Es primo")
    else:
        print("No es primo")"""



"""
def fib(num):
    if num == 0:                             #fibonacci recursivo
        return 0
    if num == 1:
        return 1
    return fib(num-1)+fib(num-2)

lista = []
for x in range(edad,cedula,.....):
    y = fib(x)
    lista.append(y)
if (edad,cedula.....) not in lista:
    print("no es fibo")
else:
    print("si es fibo")
"""


"""
def fib(n):                                  #fibonacci normal
    a = 0
    b = 1

    for k in range(n):
        c = a+b
        a = b
        b = c

    return b

for x in range(20):
    print(fib(x))
"""
    
