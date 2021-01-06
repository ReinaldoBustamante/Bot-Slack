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
Redis está basada en una estructura de tablas hash donde cada clave tiene un valor asociado. En comparación con otras bases de datos de tipo Clave-Valor, Redis permite el uso de estructuras más complejas y flexibles que abren una serie de posibilidades ante las distintas necesidades de aplicaciones de negocio.

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
