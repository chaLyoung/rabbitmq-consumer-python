import os
import json
import cv2
import pika
import urllib.request
import numpy as np
from dotenv import load_dotenv
from DB import sqlJson

load_dotenv()
RABBITMQ_URL = os.environ.get("RABBITMQ_URL")
RABBITMQ_PORT = os.environ.get("RABBITMQ_PORT")
RABBITMQ_VHOST = os.environ.get("RABBITMQ_VHOST")
RABBITMQ_CRED_ID = os.environ.get("RABBITMQ_CRED_ID")
RABBITMQ_CRED_PWD = os.environ.get("RABBITMQ_CRED_PWD")


class consumer_default:
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


class consumer_topic():
    def __init__(self):
        self.queue = 'test_queue'
        self.exchange = 'topic_logs'
        self.routing_key = 'ai.*'
        return

    def on_message(ch, method, header, body):
        file = json.loads(json.loads(body))
        image_url = file['file_path']
        req_image = urllib.request.urlopen(image_url)
        image_array = np.asarray(bytearray(req_image.read()), dtype=np.uint8)
        image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
        cv2.imshow('Color', image)
        cv2.waitKey(0)
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