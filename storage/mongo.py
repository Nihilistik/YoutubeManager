import logging

from django.conf import settings
from pymongo import MongoClient
from pymongo.errors import (
    OperationFailure,
    ServerSelectionTimeoutError
)

logger = logging.getLogger(__name__)


class MongoStorage:

    db: str = ""
    conn: MongoClient = None

    def __init__(self):
        try:
            self.conn = MongoClient(settings.MONGO_URI)
            self.db = settings.MONGO_DB
        except (OperationFailure, ServerSelectionTimeoutError):
            logger.error(f"Error connecting to MongoDb")
            raise
