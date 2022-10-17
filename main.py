import pika


class Main:
    def __init__(self):
        self.url = 'ip'
        self.port = 'port'
        self.vhost = '/'
        self.cred = pika.PlainCredentials('id', 'passwd')
        self.queue = 'queue_name'
        return

    def on_message(ch, method, header, body):
        print("received %s" %body)
        return

    def main(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(self.url, self.port, self.vhost, self.cred))
        channel = connection.channel()
        channel.basic_consume(
            queue=self.queue
            , on_message_callback=Main.on_message
            , auto_ack=True
        )
        print("Consumer is starting ... ")
        channel.start_consuming()
        return


if __name__ == '__main__':
    consumer = Main()
    consumer.main()