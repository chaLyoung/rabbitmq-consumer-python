from producer import producer_default
from producer import producer_topic


def start(producer_type):
    if producer_type == 'default':
        producer_default.main()
    elif producer_type == 'topic':
        producer_topic.main()


if __name__ == '__main__':
    start("topic")  # write default or topic