from sqlalchemy.orm import Session, declarative_base
import sqlalchemy as sa
import os
from pathlib import Path

# Database and orm configuration
DB = sa.create_engine(os.environ.get("DB_URL"))
Session = Session(DB)
Base = declarative_base()

# RabbitMQ configuration
RABBIT = os.environ.get("RABBITMQ_URL", "rabbitmq")
TEST_QUEUE = os.environ.get("TEST_QUEUE", "Test_Queue")
