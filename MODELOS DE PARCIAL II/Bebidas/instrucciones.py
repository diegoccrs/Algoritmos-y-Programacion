"""Utilizando Programación Orientada a Objetos, construya un programa que le permita al
Samán Bar hacer el control y seguimiento de su inventario de bebidas, así como llevar
un control de sus clientes y las cuentas que deberán pagar.
El bar posee múltiples opciones de bebidas, los tragos que son bebidas alcohólicas, se
caracterizan por el grado alcohólico; y las bebidas no alcohólicas se caracterizan por la
temperatura en la que se beben; adicionalmente se conoce de las bebidas, su precio y
su nombre.
De los clientes se conoce el nombre, la edad y su cédula de identidad. Por mesa de
servicio solamente se podrá tener un cliente quien será el que pague la cuenta de las
bebidas adquiridas por dicha mesa.
El programa debe poder:
1. El programa deberá permitir el registro de nuevas bebidas (2 ptos)
2. El programa deberá permitir a un cliente realizar una o múltiples compras (2
ptos)
3. Si la edad del cliente es menor a 18 años no deberá mostrarle las bebidas
alcohólicas. (1 ptos)
Al cliente finalizar su compra se le deberá mostrar la factura, la cual deberá contener:
1. Los datos personales del cliente (1 pto)
2. Los datos de cada bebida y la cantidad de bebidas compradas (1 pto)
3. El total de la compra (1 pto)
4. El descuento de acuerdo a los siguientes criterios:
a. Si la edad del cliente pertenece a la sucesión de Fibonacci(*) se le
otorgará un 5% (4 ptos)
b. Si el total de la cuenta es un número primo se le otorga un 10% (2 ptos)
El programa debe poder producir las siguiente estadísticas:
1. Cuántas bebidas se vendieron por tipo (1 pto)
2. Cuantos clientes compraron (1 pto) 
3. Cual es la bebida alcohólica y no alcohólica más vendida(1 pto)
4. Cual es el monto promedio de compra (1 pto)
(*): Un número de la sucesión de Fibonacci es aquel que se define como la suma de los
dos anteriores a_n = a_{n-1} - a_{n-2}, considerando que a_0=0 y a_1=1 IMPORTANTE:
este algoritmo debe ser recursivo.
Estructura correcta del programa (Clases, Métodos, Atributos, etc) (3 ptos)
"""