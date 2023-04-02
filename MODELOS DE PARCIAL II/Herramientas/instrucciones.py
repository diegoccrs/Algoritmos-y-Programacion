"""
Saman tools es el grupo ferretero más importante del país y desea desarrollar un sistemas para la gestión de ventas, 
y para ello se le ha contratado para que se desarrolle un programa utilizando las técnicas de programación orientada a objetos.

Tabla1. Tarifas por tipo de herrmienta 
TIPO DE HERRAMIENTA      PRECIO

Plomeria                  50$
Herreria                  40$
Carpinteria               30$

De cada cliente se requiere conocer sus datos personales, nombre, edad, número de cédula y teléfono. 

De todas las herramientas se conoce la marca, el color, el precio y su tipo; 
en caso de que sean de plomería se conocen las pulgadas para las cuales fueron hechas, 
si son ajustables y si requieren mantenimiento; 
de las herramientas para herreria se conoce cuánto calor soporta (grados celsius), 
y por último de las de carpintería se conoce cuantos años de garantia posee.

1.	El programa deberá permitir a un cliente realizar uno o múltiples compras (2ptos)
2.	Al cliente finalizar su compra se le deberá mostrar la factura, la cual deberá contener:
a.	Los datos personales del cliente  (1 ptos)
b.	Los datos de cada herramienta y la cantidad comprada  (2 ptos)
c.	El total del pago.  (2 ptos)
d.	El descuento de acuerdo a los siguientes criterios:
i.	Si la edad del cliente es un número abundante le otorgara un 10% (La verificación debe hacerse mediante una función recursiva)  (3 ptos)
ii.	Si el total de la cuenta es un número primo se le otorga un 10% adicional.  (2 ptos)

El programa debe poder producir las siguiente estadísticas:

1.	Cuántos clientes diferentes compraron productos (2 ptos)
2.	Promedio de compra por tipo de herramienta (2 ptos)
3.	El total facturado por tipo de herramienta (2 ptos)

Estructura correcta del programa (Clases, Métodos, Atributos, etc) (1 pto)
Calcular la complejidad del algoritmo del número primo (1 pto)

NOTA:
●	Número abundante: todo número natural que cumple que la suma de sus divisores propios es mayor que el propio número. 
Por ejemplo, 12 es abundante ya que sus divisores son 1, 2, 3, 4 y 6 y se cumple que 1+2+3+4+6=16, que es mayor que el propio 12.

"""