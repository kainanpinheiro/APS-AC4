import pika

url = 'amqps://oberbmqm:vFgRnxpmsVrvDNEZFyPvOOpRUV3Eu7TE@woodpecker.rmq' \
    '.cloudamqp.com/oberbmqm'
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='ac04')


def callback(ch, method, properties, body):
    print(" [x] Recebido " + str(body))


channel.basic_consume('ac04',
                      callback,
                      auto_ack=True)

print(' [*] Aguardando por mensagens:')
channel.start_consuming()
connection.close()
