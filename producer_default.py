import pika
from rabbitmq_info import Rabbitmq

rabbitmq_info = Rabbitmq()


class Publisher:
    def __init__(self):
        self.queue = 'test-queue'
        return

    def main(self):
        global rabbitmq_info

        connection = pika.BlockingConnection(pika.ConnectionParameters(rabbitmq_info.url
                                                                       , rabbitmq_info.port
                                                                       , rabbitmq_info.vhost
                                                                       , rabbitmq_info.cred))
        channel = connection.channel()
        channel.queue_declare(queue=self.queue)
        channel.basic_publish(
            exchange='',
            routing_key=self.queue,
            body='Hello RabbitMQ'
        )
        connection.close()
        return


if __name__ == '__main__':
    publisher = Publisher()
    publisher.main()