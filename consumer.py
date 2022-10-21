import pika
from rabbitmq_info import Rabbitmq

rabbitmq_info = Rabbitmq()


class default_consumer:
    def __init__(self):
        self.queue = 'test_queue'
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
        channel.queue_declare(queue=self.queue)

        channel.basic_consume(queue=self.queue, on_message_callback=self.on_message, auto_ack=True)
        print("Consumer is starting ... ")
        channel.start_consuming()
        return


class topic_consumer():
    def __init__(self):
        self.queue = 'test_queue'
        self.exchange = 'topic_logs'
        self.routing_key = 'ai.*'
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
        channel.exchange_declare(exchange=self.exchange, exchange_type='topic')
        channel.queue_declare(queue=self.queue)
        channel.queue_bind(self.queue, exchange=self.exchange, routing_key=self.routing_key)
        channel.basic_consume(queue=self.queue, on_message_callback=self.on_message, auto_ack=True)
        print("Consumer is starting ... ")
        channel.start_consuming()
        return


if __name__ == '__main__':
    consumer = topic_consumer()
    consumer.main()