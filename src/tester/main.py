import logging.config
import os, sys
from config import Base, DB, RABBIT, TEST_QUEUE, setup_logging
from controller import Consumer
import json
import logging


MOCK = json.dumps({"team_id": "7c90d362-c443-40da-b428-fab41656dd0f"})  #FIXME
logger = logging.getLogger(__name__)


def main():
    try:
        Base.metadata.create_all(DB)
        consumer = Consumer(host=RABBIT, queue=TEST_QUEUE)
        consumer.callback(None, None, None, MOCK) #FIXME
        # consumer.start_consuming()

    except KeyboardInterrupt:
        logger.error("INTERRUPTED: keyboard interrupt")
        try:
            sys.exit(0)
        except:
            os._exit(0)

    except Exception as e:
        logger.error(e)
        raise e

if __name__ == "__main__":
    setup_logging()
    main()
