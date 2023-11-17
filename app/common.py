from pymongo.collection import Collection
from bson import ObjectId

class BaseCrud:
    def __init__(self, db:Collection):
        self.db = db

    def get_all(self):
        return self.db.find({})

    def get(self, id: str):
        return self.db.find_one({"_id": ObjectId(id)})

    def create(self, data: dict):
        return self.db.insert_one(data)
    
    def create_all(self, data: list):
        return self.db.insert_many(data)

    def update(self, condition: dict, data: dict):
        return self.db.update_one(condition, {"$set": data})

    def delete(self, id: str):
        return self.db.delete_one({"_id": ObjectId(id)})