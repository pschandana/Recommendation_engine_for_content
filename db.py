from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client["auth_app"]
users = db["users"]

def add_user(username, password_hash):
    if users.find_one({"username": username}):
        return False
    users.insert_one({"username": username, "password": password_hash})
    return True

def get_user(username):
    return users.find_one({"username": username})
