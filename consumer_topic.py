import pika
from rabbitmq_info import Rabbitmq

rabbitmq_info = Rabbitmq()


class Consumer():
    def __init__(self):
        self.queue = 'queue_name'
        return

    def on_message(ch, method, header, body):
        print("received %s" % body)
        return

    def main(self):
        global rabbitmq_info

        connection = pika.BlockingConnection(pika.ConnectionParameters(rabbitmq_info.url
                                                                       , rabbitmq_info.port
                                                                       , rabbitmq_info.vhost
                                                                       , rabbitmq_info.cred))
        channel = connection.channel()
        channel.exchange_declare(exchange='topic_logs', exchange_type='topic')
        channel.queue_declare(queue=self.queue)
        channel.queue_bind(self.queue, exchange=self.__exchange, routing_key=self.__routing_key);
        channel.basic_consume(queue=self.queue, on_message_callback=Consumer.on_message, auto_ack=True)
        print("Consumer is starting ... ")
        channel.start_consuming()
        return


if __name__ == '__main__':
    consumer = Consumer()
    consumer.main()