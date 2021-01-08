# Tutorial 9 Flask

## ¿Que es?
Flask es un Microframework para facilititar el desarrollo de aplicaciones web con python, con `Micro` quiere decir que flask es un framework pequeño pero extensible 

## ¿Que es un Framework?

son herramientas que nos dan un esquema de trabajo y una serie de utilidades y funciones que nos facilita la construcción de páginas web dinámicas.

## Estructura de un proyecto flask
* static: para los ficheros estaticos
* templates: para las pantillas

## Ventajas
* Es adaptable
* incluye servidor web para pruebas
* cuenta con extensa documentacion
* muy sencillo de utilizar

## Instalacion
Para realizar su instalacion simplemente ocuparemos pip.
~~~
sudo pip install Flask
~~~

## 1. Primer programa
para ello ocupe cualquier editor de texto y cree un programa `programa_flask.py`. una vez creado, escriba lo siguiente:
~~~
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "¡Hola Mundo!"

if __name__ == "__main__":
    app.run()
~~~
Lo primero que uno debe hacer para crear su aplicacion en flask es importar el framework, para ello se ocupa la `primera linea`. Luego se debe crear la aplicacion flask, lo cual la linea 2 cumple ese papel. Luego se deben definir las rutas como se ve en la linea 3 para asi poder escribir el o los metodos asociados a esta ruta, en este caso hello(), finalmente una vez realizado esto se debera instanciar el objeto flask.

## 2. Enrutamiento
Para esto se ocupa `@app.route("/")` lo unico que debemos hacer para crear una nueva ruta es agregar algo despues de `/`.
~~~
from flask import Flask
app = Flask(__name__)

@app.route("/")
def indice():
    return "Indice"
    
@app.route("/ruta1")
def ruta1():
    return "Ruta1"
    
@app.route("/ruta2")
def ruta2():
    return "ruta2"

if __name__ == "__main__":
    app.run()
~~~
si ejecuta este codigo en su computador se podra dar cuenta que al colocar `127.0.0.1:5000/ruta1` , usted accedera a la ruta deseada con sus metodos correspondientes.

## 3. Renderizado de una pagina HTML en flask
Como se menciono anteriormente, la estructura de un proyecto flask se compone por 2 partes, static y templates. por lo que en su proyecto slack debera crear estas 2 carpetas al nivel de su archivo.py. en la carpeta templates deberan estar los archivos .html

### Creando nuestro primer archivo html
~~~
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Tutorial_9_flask</title>
</head>
<body>
    {{ suma }}
</body>
</html>
~~~
como se dijo anteriormente este archivo debe estar en la carpeta templates. ahora debemos modificar el archivo python para renderizar el html.

**ahora en app.py **
~~~
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    numero_1 = 4
    numero_2 = 6
    suma = numero_1 + numero_2
    return render_template('index.html', suma=suma)
if __name__ == "__main__":
    app.run()
~~~
podemos darnos cuenta de que para poder renderizar el archivo html en nuestro archivo python debemos importar render_template, la cual se debera usar al retornar el metodo asociado a la ruta. tambien podemos pasarle datos desde el archivo python al archivo html agregando como hiperparametro este dato a la funcion render_template. para luego ser usado en el archivo html con ``{{dato}}``

Por ultimo en la carpeta static se guardaran los archivos tipo .css o .js y estos se implementaran en el archivo html de la misma manera que siempre.
