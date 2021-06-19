from django.test import TestCase
from pymongo import MongoClient

from storage.mongo import MongoStorage

DUMMY_COLLECTION = "dummy"


class TestMongoStorage(TestCase):

    def setUp(self) -> None:
        self.mongo = MongoStorage()

    def tearDown(self) -> None:
        self.mongo.conn[self.mongo.db][DUMMY_COLLECTION].drop()

    def testInstance(self):
        self.assertIsInstance(
            self.mongo.conn,
            MongoClient
        )

    def test_insert_data(self):
        dummy_data = {"foo": "bar"}
        self.mongo.conn[self.mongo.db][DUMMY_COLLECTION].insert_one(dummy_data)
        from_db = self.mongo.conn[self.mongo.db][DUMMY_COLLECTION].find()
        self.assertDictEqual(
            dummy_data,
            from_db[0]
        )
