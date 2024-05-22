import pika, os, sys
from test import *

def main():
    connection = pika.BlockingConnection(
            pika.ConnectionParameters(host="rabbitmq")
        )
    channel = connection.channel()

    def callback(ch, method, properties, body):
        # function to handle do_any_thing_to_test()
        ...

    channel.basic_consume(
            queue=os.environ.get("TEST_QUEUE"),
            on_message_callback=callback
            )
    print("[WAITING]: waiting for message.")
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("[INTERRUPTED]: keyboard interrupt")
        try:
            sys.exit(0)
        except:
            os._exit(0)
