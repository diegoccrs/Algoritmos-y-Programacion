# 2.8 FECHA
# Elabore un programa que se encargue de solicitar 3 números que serán el día, mes y año de una fecha. 
# El programa debe indicar si la fecha es correcta y leerla por consola. 
# El programa debe cumplir las siguientes características:
# Manejar meses de 28, 30 y 31 días.
# No trabajar con años bisiestos.
# Por ejemplo, al ingresar día: 45, mes: 1, año: 2018, el programa debe enviar una alerta de que la fecha no es correcta. 
# Por el contrario, si el programa recibe datos adecuados, debe indicar que la fecha es correcta e imprimirla 
# (e.g., 25 de enero de 2018).

correcta = False

dia = input("Ingrese dia: ")
mes = input("Ingrese mes: ")
año = input("Ingrese año: ")

if año.isnumeric():
    if mes.isnumeric() and int(mes) in range(1,13):
        if mes == "2":
            if dia.isnumeric() and int(dia) in range(1,29):
                correcta = True
        elif (int(mes) == 1) or (int(mes) == 3) or (int(mes) == 5) or (int(mes) == 7) or (int(mes) == 8) or (int(mes) == 10) or (int(mes) == 12):
            if dia.isnumeric() and int(dia) in range(1,32):
                correcta = True
        else:
            if dia.isnumeric() and int(dia) in range(1,31):
                correcta = True

if correcta:
    print(f"Fecha válida! >> {dia} / {mes} / {año}")
else:
    print("Fecha incorrecta.")