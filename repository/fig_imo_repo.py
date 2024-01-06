from domain.fig_imo import Announce
from pymongo import MongoClient


class AnnounceRepository:
    def __init__(self, connection_string: str, database_name: str, collection_name: str):
        self.client = MongoClient(connection_string)
        self.database = self.client[database_name]
        self.collection = self.database[collection_name]

    def insert_one(self, announce: Announce):
        announce_dict = announce.dict()
        result = self.collection.insert_one(announce_dict)
        return str(result.inserted_id)

    def find_one(self, query: dict):
        return self.collection.find_one(query)

    def find_all(self, query: dict = None):
        return list(self.collection.find(query)) if query else list(self.collection.find())
