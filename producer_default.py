import pika
from rabbitmq_info import Rabbitmq

rabbitmq_info = Rabbitmq()


class Publisher:
    def __init__(self):
        self.__queue = 'test-queue'
        return

    def main(self):
        global rabbitmq_info

        connection = pika.BlockingConnection(pika.ConnectionParameters(rabbitmq_info.__url
                                                                       , rabbitmq_info.__port
                                                                       , rabbitmq_info.__vhost
                                                                       , rabbitmq_info.__cred))
        channel = connection.channel()
        channel.queue_declare(queue=self.__queue)
        channel.basic_publish(
            exchange='',
            routing_key=self.__queue,
            body='Hello RabbitMQ'
        )
        connection.close()
        return


if __name__ == '__main__':
    publisher = Publisher()
    publisher.main()
    # uvicorn.run(app, host="0.0.0.0", port=8000)