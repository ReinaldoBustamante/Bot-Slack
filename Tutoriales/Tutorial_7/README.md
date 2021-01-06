# Tutorial 7 SGBD No Relacional(Redis)

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
