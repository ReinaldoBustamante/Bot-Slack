#!/usr/bin/env python
import pika, sys, os, wikipedia, time
wikipedia.set_lang("es")

def main():

    #Conexión al servidor RabbitMQ   
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    #Nos aseguramos que existe una cola 'hello'
    channel.queue_declare(queue='wikipedia')

    #Recibir mensajes de la cola es más complejo. Funciona suscribiendo una función de devolución de llamada ("callback"). Cada vez que recibimos un mensaje, esta función "callback" es llamada por la libreria Pika. En nuestro caso, esta función imprimirá en la pantalla el contenido del mensaje.
    def callback(ch, method, properties, body):
        #wikipedia
        print(" [x] Elemento recibido en la cola wikipedia: %r" % body)
        print("\n")
        print(wikipedia.summary(body))
        time.sleep(body.count(b'.'))
        print(" [x] Done")
        print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.basic_consume(queue='wikipedia', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

    #Bocle infinita
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)




