from sqlalchemy.orm import Session, declarative_base
import sqlalchemy as sa
from pathlib import Path
import os, json, logging, atexit

BASE_DIR = Path(__file__).resolve().parent.parent

# Database and orm configuration
DB = sa.create_engine(os.environ.get("DB_URL"))
Session = Session(DB)
Base = declarative_base()

# RabbitMQ configuration
RABBIT = os.environ.get("RABBITMQ_URL", "rabbitmq")
TEST_QUEUE = os.environ.get("TEST_QUEUE", "Test_Queue")

logger_file = open("config/logger.json")
LOGGING = json.loads(logger_file.read())
logger_file.close()

def setup_logging():
    f = BASE_DIR / "logs"
    f.mkdir(exist_ok=True)
    logging.config.dictConfig(LOGGING) 
    queue_handler = logging.getHandlerByName("queue_handler")
    if queue_handler is not None:
        queue_handler.listener.start()
        atexit.register(queue_handler.listener.stop)

