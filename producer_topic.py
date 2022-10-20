import pika
from rabbitmq_info import Rabbitmq


rabbitmq_info = Rabbitmq()


# RabbitMQ 연결
class Publisher:
    def __init__(self):
        self.exchange = 'topic_logs'
        self.routing_key = 'ai.test'
        return

    def main(self):
        global rabbitmq_info

        connection = pika.BlockingConnection(pika.ConnectionParameters(rabbitmq_info.url
                                                                       , rabbitmq_info.port
                                                                       , rabbitmq_info.vhost
                                                                       , rabbitmq_info.cred))
        channel = connection.channel()
        channel.exchange_declare(exchange=self.exchange, exchange_type='topic')

        channel.basic_publish(
            exchange=self.exchange,
            routing_key=self.routing_key,
            body='Hello'
        )
        connection.close()
        return


if __name__ == '__main__':
    publisher = Publisher()
    publisher.main()