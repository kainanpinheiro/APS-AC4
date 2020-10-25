import pika

url = 'amqps://oberbmqm:vFgRnxpmsVrvDNEZFyPvOOpRUV3Eu7TE@woodpecker.rmq' \
    '.cloudamqp.com/oberbmqm'
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='ac04')
channel.basic_publish(exchange='',
                      routing_key='ac04',
                      body='Atividade 04 de APS')

print(" [x] Mensagem enviada!")
connection.close()
