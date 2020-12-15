import wikipedia 
import os
import pymongo 
wikipedia.set_lang("es")

DATABASE="wikipedia1"
COLLECTION="titulo"
COLLECTION2 = 'resultado'

#Conexion mongo  
myclient = pymongo.MongoClient(host=os.environ['MONGO_HOST'], port=int(os.environ['MONGO_PORT']))
db = myclient[DATABASE]
title = myclient[COLLECTION]
result = myclient[COLLECTION2]

#busquedas en wikipedia
def busqueda():
    print('¿Que desea buscar en wikipedia? :')
    busqueda = 'Chile'
    return busqueda, wikipedia.summary(busqueda)
titulo, resultado = busqueda()
#print(resultado)
#print(titulo)

#Agregar a la base de datos
db.title.insert({'titulo': titulo})
db.result.insert({'resultado': resultado})

#Mostrar lo agregado 

print('Se agrego el siguiente cursor a la base da datos: ',db.title.find({'titulo': 'Chile'}))