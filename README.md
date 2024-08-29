# _Proyecto Restaurante_

El proyecto simula el funcionamiento de una cadena de restaurantes.

## Funcionalidades

- Funcionalidad 1: Reservar.
- Funcionalidad 2: Ordenar Comida.
- Funcionalidad 3: Dejar Restaurante.
- Funcionalidad 4: Agregar Sede.
- Funcionalidad 5: Crear Evento.

### Funcionalidad 1: Reservar

La funcionalidad comienza mostrando en pantalla las ciudades con sedes disponibles, si el tipo de dato no es valido lo vuelve  a solicitar. La primera interaccion es seleccionMesa, que solicita unos datos del cliente y luego le da a seleccionar entre una mesa de tipo V.I.P o estandar, comprueba la disponibilidad segun la cantidad de comensales y el tipo de mesa, e imprime en pantalla las mesas seleccionables (que no estan ocupadas) y la asigna la escogida al cliente. Las opciones de reserva para clientes estandar termina aca, pero para los clientes V.I.P la funcionalidad continua si el cliente desea ordenar por adelantado, se convoca a la funcion ordenarComida y se establecen los valores para los atributos de la mesa. La funcionalidad sigue preguntandole al cliente si desea hacer el pago de su reserva inmediantamente, si decide no hacerlo, se define el atributo pagoPreconsumo de factura como falso, y se añadirá una propina porcentual obligatoria en su factura. Podra elegir entre agregar una reseña, terminar o cancelar reservacion y termina la funcionalidad; si decide si hacerlo, el atributo pagoPreconsumo se define como verdadero y el valor de la mesa no se vera afectado, mostrará todos los datos de la reserva y confirmar si esta todo correcto para proceder con la facturacion y finalizar la funcionalidad.

### Funcionalidad 2: Ordenar Comida

La funcionalidad comienza mostrando el menú de los platos de la sede del restaurante. La primera interacción ocurre cuando se llama al método escogerComida que recibe como parámetro el Cliente que va a ordenar. Luego el cliente solicita el nombre de los platos y la cantidad que va a pedir de cada uno. El restaurante revisa si tiene inventario de los platos solicitados y si la hay, retorna un objeto Pedido, finalizando así la interacción. La siguiente interacción comienza con el objeto Pedido retornado anteriormente y muestra un resumen del pedido en el que el cliente revisa si está bien tomado. Si considera que no es el caso, se vuelve a la interacción 1, si el Pedido está correcto, se modifican sus atributos y éste es retornado. La última interacción toma nuevamente el Pedido retornado y el Cliente que hace el pedido, se accede al atributo factura del Cliente y agrega el objeto Pedido al atributo pedido de la factura asignada. La interacción finaliza retornando un objeto Factura. 

### Funcionalidad 3: Dejar Restaurante

La primera interacción ocurre en el momento en el que el cliente se desee retirar del restaurante se mostrará la cantidad que debe pagar y pregunta si desea dar una propina para agregarla al valor total de la factura. Luego se pregunta por el método de pago y la interacción finaliza retornando un objeto Cliente. La segunda interacción comienza recibiendo el objeto Cliente retornado anteriormente y pregunta si desea hacer una reserva para otro día, llevándolo a hacer uso de la primera funcionalidad “reservarMesa”. Luego le pide al cliente que deje una calificación del restaurante y, si lo desea, también puede dejar una reseña. La interacción finaliza desligando al cliente y a la mesa entre sí, retornando un objeto Reseña. La última interacción actualiza el valor del atributo calificación de la clase Restaurante, y añade las reseñas que hayan dejado los clientes. 

### Funcionalidad 4: Agregar Sede

Esta funcionalidad permite crear nuevas sedes del restaurante. La primera interacción recibe un parámetro Restaurante y establece la ciudad en la que se ubica, pregunta si tendrá zona VIP y le asigna una calificación aleatoria de 2 a 4. La interacción finaliza retornando un objeto de clase Restaurante. La segunda interacción comienza recibiendo el objeto Restaurante retornado anteriormente para luego crear las mesas, que deberán ser un mínimo de diez. Si hay zona VIP también se crearán mesas VIP, mínimamente cinco. Las mesas serán agregadas al atributo mesas del objeto Restaurante y la interacción finaliza retornando el objeto Restaurante modificado. La última interacción toma nuevamente el objeto Restaurante retornado anteriormente y crea el menú para la nueva sede. Primero se elige la cantidad de platos que serán creados, luego se definen los valores de cada uno de sus atributos y finalmente son añadidos al atributo menú del Restaurante. La interacción finaliza retornando el objeto Restaurante con todos sus atributos inicializados.

### Funcionalidad 5: Crear Evento

Esta funcionalidad se encarga de crear un evento, que tendrá un nombre, descripción y fecha, junto con un coste opcional. En un primer momento se solicitaría la localización del evento, y se llamaría a la primera interacción, la cual se encargará de recomendar una localización para el evento basandose en la capacidad del restaurante, en caso tal de que la localización solicitada previamente sea la que mayor capacidad tiene, se seguirá ejecutando el programa, de lo contrario preguntará si se desea cambiar la localización, de ser así se vuelve a llamar a la funcionalidad, de no ser así se continua con la ejecución, se solicita la fecha del evento, verifica si hay reservas y retorna un Array con los clientes que tienen una reserva para ese día. De aquí se pasa a la interacción 2, que se encarga de preguntar a cada uno de los clientes si desean conservar o no su reserva, en caso de conservarla se realizará un descuento del 50% sobre el coste de la reserva y se retornará un Array con las mesas del restaurante, de lo contrario se preguntará si se desea hacer una reserva para otro día, de ser así se llama a la funcionalidad reservarMesa, de lo contrario simplemente se elimina al cliente, Por último, la interacción 3 establecerá la capacidad máxima del evento teniendo en cuenta las mesas ocupadas, y solicitará los datos del evento, luego se preguntará si tiene coste, de ser así se solicita, de lo contrario no pasa nada, se continua con la ejecución para enlazar al restaurante con el evento y viceversa, para finalmente retornar el Evento.

## Diagramas

Debajo se muestran los links que dan acceso a los diferentes diagramas realizados.

| Nombre | Link |
| ------ | ------ |
| Clases y Funcionalidad 1 | [DiagramaUML/Clases-&-Funcionalidad-1][C/1] |
| Funcionalidades 2 y 3 | [DiagramaUML/Funcionalidades-2-&-3][2/3] |
| Funcionalidades 4 y 5 | [DiagramaUML/Funcionalidades-4-&-5][4/5] |

## Grupo 2 - Equipo 6

### Integrantes

- Juan José Arango Marín.
- Samuel Colorado Castrillón.
- Stiven Saldarriaga Mayorga.

[//]: # (Links de Referencia)

   [C/1]: <https://app.moqups.com/kNpRQwlexDAhDjLi7JJ5aJwmyvrv7bJa/view/page/a4e40d448>
   [2/3]: <https://app.moqups.com/ikQzNogpXinfvw53P0OgYX9Nj1FdOJ8C/view/page/ad64222d5>
   [4/5]: <https://app.moqups.com/u0C7OTlBKLEaXOlkkMftwS60mB081ipv/view/page/ad64222d5>
