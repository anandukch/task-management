from pymongo import mongo_client
import pymongo
# from app.books.schemas import Author
from app.settings import settings


client = mongo_client.MongoClient(settings.MONGO_URL, serverSelectionTimeoutMS=5000)

try:
        conn = client.server_info()
        print(f'Connected to MongoDB {conn.get("version")}')
except Exception:
        print("Unable to connect to the MongoDB server.")


db = client["waterdip"]
User = db.users
Tasks = db.tasks


User.create_index([("email", pymongo.ASCENDING)], unique=True)

