# Tutorial 7 SGBD No Relacional (Redis)

## 1.Introducion
### 1.1 ¿Que son las SGBD no relacionales?
las Base de datos no relacionales o tambien llamadas NoSQL son bases de datos diseñadas especificamentes para modelos de datos especificos ademas de poseer esquemas flexibles para las aplicaciones modernas. Estas bases de datos son conocidas por su facil implementacion, la funcionalidad que provee ademas de su buen rendimiento. Estas bases de datos son muy utiles en proyectos los cuales no sabemos con exactitud que cosas se van a almacenar.

### 1.2 ¿cual es la diferencia entre SGBD no relacionales y su contraparte?
Estas a diferencia de las bases de datos relacionales no poseen un  identificador que permita la relación entre un conjunto de datos y otros. sino la informacion se organiza normalmente mediante documentos.

### 1.3 Tipos 
- **Clave-Valor**: Las bases de datos clave-valor son altamente divisibles y permiten escalado horizontal a escalas que otros tipos de bases de datos no pueden alcanzar.
- **Documentos**: Las bases de datos de documentos facilitan a los desarrolladores el almacenamiento y la consulta de datos en una base de datos mediante el uso del mismo formato de modelo de documento que emplean en el código de aplicación. La naturaleza flexible, semiestructurada y jerárquica de los documentos y las bases de datos de documentos permite que evolucionen según las necesidades de las aplicaciones.
- **Graficos**: una base de datos de grafos utiliza estructuras de grafos para almacenar, correlacionar y consultar relaciones.
- **En Memoria**: Almacena sus datos en memoria para facilitar tiempos más rápidos de respuesta. 

Para este tutorial se ocupara la base de datos no relacional **Redis**

### 1.4 Redis
Redis está basada en una estructura de tablas hash donde cada clave tiene un valor asociado. En comparación con otras bases de datos de tipo Clave-Valor, Redis permite el uso de estructuras más complejas y flexibles que abren una serie de posibilidades ante las distintas necesidades de aplicaciones de negocio. Tambien es importante mencionar que los datos se ingresan directamente en la memoria principal del servidor

#### 1.4.1 Instalacion
~~~
sudo apt-get update
sudo apt-get install redis-server
~~~
para comprobar que funciona podemos iniciar el servidor y luego mandar un ping, para ello escriba lo siguiente en su terminal
~~~
redis-server
redis-cli
~~~
luego le aparecera algo como esto
~~~
127.0.0.1:6397> 
~~~
En esta parte debera escribir ping, recibiendo como respuesta pong
~~~
127.0.0.1:6397> ping 
PONG
~~~
si le parace esto ultimo en su terminal, significa que se ha instalado correctamente

#### 1.4.2 Configuracion

Una ves dentro del terminal de redis, el cual puede abrir con :
~~~
redis-cli
~~~
Podra obtener una lista de todas las configuraciones que puede realizar con el comando `config get *`
un ejemplo de esto es 
~~~
  1) "dbfilename"
  2) "dump.rdb"
  3) "requirepass"
  4) ""
  5) "masterauth"
  6) ""
  .
  .
  .
~~~
Si nos damos cuenta, esta lista se divide en pares, siendo 1) el nombre de la configuracion y 2) su valor. dicho esto podemos editar su valor con el comando `config set 'nombre campo' 'valor nuevo' `

Para agregar una contraseña, solo debemos configurarla con los comandos mencionados anteriormente.
~~~
127.0.0.1:6397> config set 'requirepass' 'password'
~~~
una vez creada la contraseña al intentar obtener un valor con `config get *`, nos pedira autentificarnos. lo cual lo podemos hacer de la siguiente manera.
~~~
127.0.0.1:6397> auth "password"
~~~
#### 1.4.3 Persistencia de datos
Como se menciono anteriormente redis almacena todos los datos en memoria principal del servidor, es decir al apagarse el servidor esta perderia la informacion almacenada. Por lo cual para lograr una persistencia de datos podemos almacenar una copia de seguridad en el disco duro. Esto se puede lograr con el siguiente comando:

~~~
127.0.0.1:6397> bgsave
~~~

Esto creara un archivo en el disco duro con el nombre de **dump.rdb**. Ademas tambien es posible programar un save automatico con `bgsave 'tiempo' 'cantidad de cambios'`, es decir que si se han producido x cantidad de cambios en el intervalo de tiempo(Segundos), se guardara automaticamente una copia de seguridad.

Tambien existe el comando **save** pero no es recomendable, ya que si el sistema esta en funcionamiento este comando no permitiria a los clientes acceder a la base de datos.

#### 1.4.4 Ingresar valores a la base de datos

En redis podemos almacenar diferentes tipos de datos. estos son:
- String
- Enteros
- Listas
- Hashes
- Sets. 

Para almacenar **String y enteros simplemente podemos escribir lo siguiente**:
~~~
set nombre_variable 'hola mundo' 
set nombre_variable 1 
~~~
La variable string se caracteriza por llevar comillas, por otro lado las variables INT no.
Para acceder los valores de las variables creadas anteriormente podemos utilizar:
~~~
get nombre_variable 
~~~
y para borrar 
~~~
del nombre_variable 
~~~
Ademas si deseamos agregar mas de 1 variable podemos hacer lo siguiente.
~~~
mset variable1 "valor variable1" variable2 "valor variable2" 
~~~
igualmente esto se puede utilizar para hacer las consultas
~~~
mget variable1 variable2 
~~~

Para almacenar **Listas** podemos hacerlo de 2 maneras, agregar elementos a una lista por la derecha o por la izquierda.
~~~
lpush mylist 1
lpush mylist 2
~~~
al realizar la consulta de mylist obtenemos lo siguiente.
~~~
127.0.0.1:6397> lrange mylist 0 5 
1) '2'
2) '1'
~~~
note que lpush agrega valores a la lista por la izquierda ya que la posicion 1 corresponde al ultimo agregado. en cambio si quisieramos agregar por la derecha simplemente cambiamos la **l** por una **r**.
~~~
127.0.0.1:6397> rpush mylist 3
1) '2'
2) '1'
3) '3'
~~~
tambien para ver lo elementos de la lista podemos ocupar el comando usado anteriormente 
~~~
127.0.0.1:6397> lrange mylist inicio fin 
~~~
finalmente para eliminar se ocupa lrem
~~~
127.0.0.1:6397> lrem mylist 0 1
~~~
esto eliminara el elemento 1 de la lista

Para almacenar **Sets** podemos hacerlo de la siguiente manera
~~~
127.0.0.1:6397> sadd nombre_set "hola"
127.0.0.1:6397> sadd nombre_set "mundo"
~~~
podemos consultar el set con:
~~~
127.0.0.1:6397> smembers nombre_set
1) "hola"
2) "mundo"
~~~
tambien podemos validar si existe un valor
~~~
127.0.0.1:6397> sismember nombre_set valor
~~~
si nos da 0 es por que no esta el valor, por otro lado si nos devuelve 1 si esta.
Tambien podemos eliminar un valor del set
~~~
127.0.0.1:6397> srem nombre_set 'valor'
~~~

Ahora el punto fuerte de redis es el almacenamiento de **Hashes** este se puede realizar de la siguiente forma
~~~
hset nombre_hash_set campo1 "valor" campo2 "valor" campo3 "valor"
~~~
para obtener los valores de un campo en especifico.
~~~
hget nombre_hash_set campo
~~~
para obtener los valores de un campo en especifico.
~~~
hgetall nombre_hash_set
~~~
para obtener solo los valores de todos los campos
~~~
hvals nombre_hash_set
~~~
para ver las keys del hash
~~~
hkeys nombre_hash_set
~~~
Para eliminar un campo
~~~
hdel nombre_hash_set campo
~~~
para eliminar el hash
~~~
del nombre_hash_set 
~~~

**Si deseamos eliminar todas las entradas de la base de datos podemos ocuapr el comando `flushall`**
