#1.1 CUENTA BANCARIA 
# Debes realizar un programa que ejecute las operaciones que se llevan a cabo en una cuenta bancaria.
# 1.- 2020/04/10: El saldo inicial es de $3480
# 2.- 2020/04/11: Se hace una compra en una tienda de ropa y se gastan $96
# 3.- 2020/04/17: Se cobran $1200 de salario
# 4.- 2020/04/30: Se cobra un 3% del saldo de la cuenta en intereses
# 5.- 2020/05/02: Se hace una compra en el supermercado y se gastan $51

# Como output se espera: 
# - Mostrar la cantidad de dinero recibida/retirada.
# - Mostrar el saldo actual de la cuenta y la fecha, al iniciar el programa y  cada vez que se realice una operación.
# Por ejemplo:
# Se han retirado $96.
# Saldo actual a la fecha (2020/04/11): ${saldo_restante}

x = 3480
print(f"2020/04/10: El saldo inicial es de {x}","$")

y = x-96
print("Se han retirado 96$")
print(f"2020/04/11: El saldo actual es de {y}","$")

z = y+1200
print("Se han cobrado 1200$")
print(f"2020/04/17: El saldo actual es de {z}","$")

w = z+(z*0.03)
print("Se ha cobrado un 3% del saldo")
print(f"2020/04/30: El saldo actual es de {w}","$")

j = w-51
print("Se han retirado 51$")
print(f"2020/05/02: El saldo actual es de {j}","$")