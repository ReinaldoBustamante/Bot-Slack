  # Tutoriales 8 Go

## 1. ¿Que es Go?
Go es un lenguaje de programación concurrente y compilado, desarrollado por Google. Además, Go es de tipado estático, pero tiene partes del tipado dinámico, es decir se pueden declarar variables sin indicar de que tipo es, ya que el compilador interpretara que tipo de dato es. por otro lado ya no te permitira cambiar el tipo de dato. 

## 2. Instalacion
Para instalar go ocuparemos snap. Para ello abra su terminal de linux y escriba lo siguiente .
~~~
sudo apt install snapd
~~~
luego haga lo siguiente:
~~~
sudo snap install go --classic
~~~
### 2. ¿Como Utilizar?
para mostrar la sintaxis de go se creara el primer programa que todos siempre hemos creamos, el conocido 'hello world!'.
para ello utilizaremos en el editor de texto que usted desee escriba lo siguiente.
~~~
package main

import "fmt"

func main() {
  fmt.Println("Hello, World!")
}
~~~
Podemos ver que este codigo ocupa 3 aspectos claves de este lenguaje. El primero 'package' indica al tipo de paquete que pertenece este archivo en esta caso 'main'. import indica al compilador que paquetes extras desea utilizar en el archivo. en este caso 'fmt', fmt es un paquete que nos otorgara funciones basicas y utiles, println es una funcion de go que pertenece al paquete fmt la cual nos sera util para mostrar texto en pantalla. ademas tambien es importante mencionar que las aplicaciones go deben poseer un paquete main ademas de una funcion.

para ejecutar el codigo simplemente escriba lo siguiente:
~~~
go run hello.go
~~~
podemos ver que 'go' sirve para compilar la aplicacion, por otro lado 'run' sirve para ejecutar la aplicacion

#### 2.1 Input y Output
para realizar input en go se ocupa la siguiente funcion `fmt.Scanln` la cual nos servira para decirle a la computadora que espere un input. esta se ve con mas detalles a
continuacion
~~~
package main

import "fmt"

func main() {
  fmt.Println("Esperando a que ingrese algo.")
  var dato = ""
  fmt.Scanln(&dato)
  fmt.Println("input recibido.")
  fmt.Printf("se recibio el siguiente dato, %s Gracias)
}
~~~
podemos ver que para imprimir el resultado nos resulta conveniente utilizar Printf ya que con (%s) podemos insertar el texto en cualquier posicion del output. Tambien al crear una variable en esta caso `dato` no es necesario colocar a que tipo de dato pertenece, basta con solo indicar que es una variable utilizando `var` antes del nombre de la variable o con := despues del nombre de la variable. 

#### 2.2 Arreglos y Slice
podemos definir arreglos de 2 formas diferentes. la primera forma es:
~~~
var array [3]string
array[0] = "123"
array[1] = "asd"
array[2] = "azsx"
~~~
nos damos cuenta de que para definir un arreglo es necesario definir el tipo de datos que tendra este. ademas de que los indices de los arreglos siempre parten en 0.
la otra manera de definir un arreglo es la siguiente.
~~~
array := [5]string{"123", "asd", "azsx"}
~~~
nos damos cuenta de que la ultima es mas practica ya que no se estaria escribiendo muchas lineas de codigo.

Es importante mencionar que al crear un arreglo de x elementos tipo entero, este creara un arreglo de dimension x cuyos elementos seran puros 0. Para el caso de un arreglo de tipo string, este creara un arreglo cuyos elementos seran ''. 

Para realizar operaciones sobre los arreglo es importante conocer el tamaño de este. para ello existen 2 funciones importantes, `len(array)` y `cap(array)`

Una herramienta muy util para trabajar con arreglo son los **Slice**. Estos nos serviran para poder recuperar un fragmento del arreglo de manera rapida y eficiente.
por ejemplo 
~~~
package main
import "fmt"
func main() {
  numeros := [10]int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
  fmt.Println(numeros) // esto nos imprimira el arreglo creado anteriormente
  fmt.Println(numeros[0:3]) // esto nos imprimira el arreglo desde la posicion 0 hasta la 3 (sin incluirla) -> [1,2,3]
  fmt.Println(numeros[:3]) // esto nos imprimira el arreglo desde la posicion 0 hasta la 3 (sin incluirla) -> [1,2,3]
  fmt.Println(numeros[3:]) // esto nos imprimira el arreglo desde la posicion 3 hasta la ultima (incluida) -> [4,5,6,7,8,9,10]
}

~~~

#### 2.3 Operaciones
**Operadores aritmeticos :**
~~~
// Suma
a := 1
b := 2
a + b = 3

// Resta
a := 1
b := 2
a - b = -1

// division
a := 1
b := 2
a/b = 0 // esto devuelve solo la parte entera
4/2 = 2
5/2 = 2
// para especificar que lo devuelva en decimal debemos colocar un punto al final de los valores de a y b para indicar que es de tipo flotante

//multiplicacion

a := 1
b := 2
a*b = 2

//resto de una division
a := 1
b := 2
a%b = 1

//identidad de a
a := 1
a+ (resultado 1)

//cambio de signo
a := 1
a- (resultado -1)
~~~
Es importante mencionar que para este lenguaje igual se pueden ocupar `a++` par agregar 1 valor a la variable. ademas de ocupar `a +=1`

**Operadores Logicos :**
~~~
== // sirve para comparar 2 elementos, si son iguales devuelve True si no False
!= // sirve para comparar 2 elementos, si son distintos devuelve True si no False
> // sirve para evaluar si un numero es mayor que el otro, si es mayor devuelve True si no False
< // menor que
>= // mayor igual que
<= // menor igual que
& // and
| // or
^ // xor
~~~
#### 2.4 Estructura de control
Comenzaremos por el **if** :
~~~
package main

import "fmt"

func main() {

    validador := true

    if validador {
        fmt.Println("Es verdadero")
    }
}
~~~
Este validador permite que solo se ejecute la linea que este dentro si la condicion es verdadera, pero ¿Como hacer que ejecute una linea si la primera no se ejecuta?.
~~~
package main

import "fmt"

func main() {

    validador := true

    if validador {
      fmt.Println("Es verdadero")
    } else {
      fmt.println("Es falso")  
    }
}
~~~
Efectivamente, para ese caso se ocupara **else**, Tambien es importante mencionar que el else debe ir despues del if. Ahora si necesitamos comprobar mas de un condicion podemos ocupar else **if**.
~~~
package main

import "fmt"

func main() {

    numero := 100

    if numero>50  {
      fmt.Println("Usted posee un numero alto")
    } else if numero < 50 {
      fmt.println("usted posee un numero bajo")  
    } else{
      fmt.println("Usted esta en la mitad")
    }
}
~~~


Otra estructura de control utilizada es **Switch**
~~~
package main

import "fmt"

func main() {

    numero := 18
    switch {
    case numero > 50:
        fmt.Println("Usted posee un numero alto")
    case numero < 50:
        fmt.Println("Usted posee un numero bajo")
    default:
        fmt.Println("Usted esta en la mitad")
    }
}
~~~

#### 2.5 Estructuras iterativas
Una de las diferencias notables de go, es que este lenguaje no tiene ciclo while, solo usa for. por otro lado esta sentencia es muy flexible. esto se vera a contiuacion.

Comenzaremos por el ciclo **for basico**
~~~
package main

import "fmt"

func main() {
    var i = 0

    for i < 10 {
        fmt.Println(i)
        i++
    }
}
~~~
otro estilo de for es **for estilo while**
~~~
package main

import "fmt"

func main() {
    var i = 0

    for i < 10 {
        fmt.Println(i)
        i++
    }
}
~~~
#### 2.6 Ejercicios
* S
