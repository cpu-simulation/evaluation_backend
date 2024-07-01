from django.conf import settings
import pika
import json
import logging

logger = logging.getLogger()
import pika.spec

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=settings.RABBIT_HOST)
    )
channel = connection.channel()


def push_task(msg:dict):
    logger.debug("publish rabbit msg")
    try:
        channel.basic_publish(
            exchange="",
            body=json.dumps(msg),
            routing_key=settings.TEST_QUEUE,
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            )
        )
    except Exception as e:
        logger.debug(f"[FAILED]: failed to publish rabbit msg. {e}")
        raise e