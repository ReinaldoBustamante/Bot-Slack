#!/usr/bin/env python
import pika
import time
import os

time.sleep(30)


########### CONNEXIÓN A RABBIT MQ #######################
HOST = os.environ['RABBITMQ_HOST']

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=HOST))
channel = connection.channel()

#El consumidor utiliza el exchange 'nestor'
channel.exchange_declare(exchange='nestor', exchange_type='topic', durable=True)

#Se crea un cola temporaria exclusiva para este consumidor (búzon de correos)
result = channel.queue_declare(queue="bot", exclusive=True, durable=True)
queue_name = result.method.queue

#La cola se asigna a un 'exchange'
channel.queue_bind(exchange='nestor', queue=queue_name, routing_key="bot")


##########################################################


########## ESPERA Y HACE UN BUSQUEDA WIKIPEDIA CUANDO RECIBE UN MENSAJE ####

print(' [*] Waiting for messages. To exit press CTRL+C')


#print('hola')
#print(msn.insert({'mensaje': '1'}))
#print('h')
def callback(ch, method, properties, body):
    print(body)
    if str(body).startswith("b'[bot]"):
        channel.basic_publish(exchange='nestor', routing_key="publicar_slack", body='Comandos del bot: ')
        channel.basic_publish(exchange='nestor', routing_key="publicar_slack", body='Almacenamiento de mensajes:')
        channel.basic_publish(exchange='nestor', routing_key="publicar_slack", body='[link] -> almacena link')
        channel.basic_publish(exchange='nestor', routing_key="publicar_slack", body='[repo] -> almacena repositorio')
        channel.basic_publish(exchange='nestor', routing_key="publicar_slack", body='[aviso] -> almacena avisos')  
        channel.basic_publish(exchange='nestor', routing_key="publicar_slack", body='[fechas] -> almacena fechas')

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()

###########################################################
