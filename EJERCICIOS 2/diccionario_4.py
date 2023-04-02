#Escribir un programa que pregunte una fecha en formato dd/mm/aaaa 
# y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.

months = {1:"Enero",2:"Febrero",3:"Marzo",4:"Abril",5:"Mayo",6:"Junio",7:"Julio",8:"Agosto",9:"Septiembre",10:"Octubre",11:"Noviembre",12:"Diciembre"}

date = input("Introduzca una fecha en formato dd/mm/aaaa: ")
date = date.split("/")

print(f"{date[0]} de {months[int(date[1])]} de {date[2]}")