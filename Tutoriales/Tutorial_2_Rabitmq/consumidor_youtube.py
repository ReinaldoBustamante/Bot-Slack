#!/usr/bin/env python
import pika, sys, os
from youtube_search import YoutubeSearch

def main():

    #Conexión al servidor RabbitMQ   
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    #Nos aseguramos que existe una cola 'hello'
    channel.queue_declare(queue='youtube')


    #Recibir mensajes de la cola es más complejo. Funciona suscribiendo una función de devolución de llamada ("callback"). Cada vez que recibimos un mensaje, esta función "callback" es llamada por la libreria Pika. En nuestro caso, esta función imprimirá en la pantalla el contenido del mensaje.
    def callback(ch, method, properties, body,max_results=1,order="relevance", token=None, location=None, location_radius=None):
        print(" [x] Elemento recibido en cola youtube: %r" % body)
        search = YoutubeSearch(body, max_results=5).to_dict()
        resultados = search
        for i in range(5):
            print('\n')
            print('Titulo: ',resultados[i]['title'])
            print('Link:','https:youtube.com'+resultados[i]['url_suffix'])
            print('Duracion:',resultados[i]['duration'],'minutos')
            print('Visitas:',resultados[i]['views'])
            print('Canal:',resultados[i]['channel'])
        print('\n')
        print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.basic_consume(queue='youtube', on_message_callback=callback, auto_ack=True)

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