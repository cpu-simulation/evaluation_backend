import logging.config
import os, sys
from config import Base, DB, RABBIT, TEST_QUEUE, setup_logging
from controller import Consumer
import json
import logging


logger = logging.getLogger(__name__)


def main(db, consumer, base):
    try:
        base.metadata.create_all(db)
        consumer.connect()
        consumer.start_consuming()

    except KeyboardInterrupt:
        logger.error("INTERRUPTED: keyboard interrupt")
        try:
            sys.exit(0)
        except:
            os._exit(0)

    except Exception as e:
        logger.error(e)
        raise e

def get_db():
    return DB

def get_consumer():
    return Consumer(host=RABBIT, queue=TEST_QUEUE)

if __name__ == "__main__":
    setup_logging()
    main(db=get_db(), consumer=get_consumer(), base=Base)
