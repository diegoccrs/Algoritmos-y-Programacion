"""
Saman hotels es el grupo hotelero más importante del país y desea desarrollar un sistemas para la gestión de alojamientos, 
y para ello se le ha contratado para que se desarrolle un programa utilizando las técnicas de programación orientada a objetos.

Tabla 1. Tarifas por noche

TIPO DE HABITACION      PRECIO 
Suite                   100$
Doble                   60$
Sencilla                40$

De cada cliente se requiere conocer sus datos personales, nombre, edad, número de cédula, teléfono y 
la cantidad de personas que trae consigo. 

De todas las habitaciones se conoce la cantidad de camas, baños y su precio; 
en caso de que sea una Suite se conoce si tiene jacuzzi o no, 
y se saben que todas las suites tienen 3 camas; 
de las dobles se conoce el tipo de habitación (Si es matrimonial o Individual), 
y por último de las sencilla se conoce si tiene tv o no.

El programa deberá permitir el registro del hospedaje indicando cuantas noches y habitacion	es requiere el cliente (2 ptos)
El programa deberá permitir a un cliente realizar uno o múltiples hospedajes (2 ptos)
Al cliente finalizar su compra se le deberá mostrar la factura, la cual deberá contener:
Los datos personales del cliente  (1 ptos)
Los datos de cada habitación y la cantidad  (1 ptos)
El total del pago.  (1 ptos)
El descuento de acuerdo a los siguientes criterios:
Si la edad del cliente es un número primo le otorgara un 10% (La verificación debe hacerse mediante una función recursiva)  (3 ptos)
Si el total de la cuenta es un número abundante se le otorga un 10% adicional.  (2 ptos)

El programa debe poder producir las siguiente estadísticas:

Cuántos clientes están alojados (2 ptos)
Promedio de alojamiento por tipo de habitación (2 ptos)
El total facturado por tipo de habitación (2 ptos)

Estructura correcta del programa (Clases, Métodos, Atributos, etc) (1 pto)
Calcular la complejidad del algoritmo del número abundante (1 pto)


NOTA:

Número abundante: todo número natural que cumple que la suma de sus divisores propios es mayor que el propio número. 
Por ejemplo, 12 es abundante ya que sus divisores son 1, 2, 3, 4 y 6 y se cumple que 1+2+3+4+6=16, 
que es mayor que el propio 12.


"""