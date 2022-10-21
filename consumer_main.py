from consumer import consumer_default
from consumer import consumer_topic


def start(consumer_type):
    if consumer_type == 'default':
        consumer_default.main()
    elif consumer_type == 'topic':
        consumer_topic.main()


if __name__ == '__main__':
    start("topic")  # write default or topic