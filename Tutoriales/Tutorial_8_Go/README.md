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
podemos ver que para imprimir el resultado nos resulta conveniente utilizar Printf ya que con (%s) podemos insertar el texto en cualquier posicion del output. Tambien al crear una variable en esta caso `dato` no es necesario colocar a que tipo de dato pertenece, basta con solo indicar que es una variable con `var`.

#### 2.2 Arreglos y Slice


#### 2.3 Operaciones

#### 2.4 Estructura de control

#### 2.5 Estructuras iterativas

##### 2.5.1 Ciclo for

##### 2.5.1 Ciclo while

#### 2.6 Ejercicios

