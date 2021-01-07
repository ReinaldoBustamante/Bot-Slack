# Tutoriales 8 Go

## 1. ¿Que es Go?
Go es un lenguaje de programación concurrente y compilado, desarrollado por Google. Además, Go es de tipado estático, pero tiene partes del tipado dinámico, es decir se pueden declarar variables sin indicar de que tipo es, ya que el compilador interpretara que tipo de dato es. por otro lado ya no te permitira cambiar el tipo de dato. 

## 2. Instalacion
Para instalar go primero debemos descargar su archivo de instalacion. Para ello abra su terminal de linux y escriba lo siguiente.
~~~
curl -O https://dl.google.com/go/go1.15.6.linux-amd64.tar.gz
~~~
luego haga lo siguiente:
~~~
sudo tar -C /usr/local -xzf go1.15.6.linux-amd64.tar.gz
export PATH=$PATH:/usr/local/go/bin
go version
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
