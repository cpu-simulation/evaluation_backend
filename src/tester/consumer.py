import pika, os, sys
from test import *
from config import Base, DB, RABBIT, TEST_QUEUE
from models import Scenario
    
def main():


    connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=RABBIT)
        )
    channel = connection.channel()

    def callback(ch, method, properties, body):
        # function to handle do_any_thing_to_test()
        ...

    channel.basic_consume(
            queue=TEST_QUEUE,
            on_message_callback=callback
            )
    print("[WAITING]: waiting for message.")
    channel.start_consuming()


if __name__ == "__main__":
    try:
        Base.metadata.create_all(DB)
        main()
    except KeyboardInterrupt:
        print("[INTERRUPTED]: keyboard interrupt")
        try:
            sys.exit(0)
        except:
            os._exit(0)
