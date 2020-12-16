#!/usr/bin/env python
import pika
import sys

#Nuestra tarea pasada como argumento
message = ' '.join(sys.argv[1:]) or "Hello World!"

#Conexión al servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#Creación de la cola
channel.queue_declare(queue='wikipedia')
channel.queue_declare(queue='youtube')

#Publicación del mensaje en el consumidor wikipedia
channel.basic_publish(exchange='',
                      routing_key='wikipedia',
                      body=message)

#Publicación del mensaje en el consumidor youtube
channel.basic_publish(exchange='',
                      routing_key='youtube',
                      body=message)
print(" [x] Sent %r" % message)

connection.close()
