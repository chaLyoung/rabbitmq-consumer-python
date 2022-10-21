import pika
from rabbitmq_info import Rabbitmq

rabbitmq_info = Rabbitmq()


class producer_default:
    def __init__(self):
        self.queue = 'test-queue'
        return

    def main(self):
        global rabbitmq_info

        connection = create_connection()
        channel = connection.channel()
        channel.queue_declare(queue=self.queue)
        channel.basic_publish(
            exchange='',
            routing_key=self.queue,
            body='Hello RabbitMQ'
        )
        connection.close()
        return


class producer_topic:
    def __init__(self):
        self.exchange = 'topic_logs'
        self.routing_key = 'ai.test'
        return

    def main(self):
        global rabbitmq_info

        connection = create_connection()
        channel = connection.channel()
        channel.exchange_declare(exchange=self.exchange, exchange_type='topic')

        channel.basic_publish(
            exchange=self.exchange,
            routing_key=self.routing_key,
            body='Hello'
        )
        connection.close()
        return


def create_connection():
    global rabbitmq_info
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            rabbitmq_info.url
            , rabbitmq_info.port
            , rabbitmq_info.vhost
            , rabbitmq_info.cred
        )
    )
    return connection