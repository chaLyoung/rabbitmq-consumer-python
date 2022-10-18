import pika


class Rabbitmq:
    def __init__(self):
        self.url = 'ip here'
        self.port = 'port jere'
        self.vhost = 'virtual host name here'
        self.cred = pika.PlainCredentials('id here', 'password here')