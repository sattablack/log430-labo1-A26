import os
from dotenv import load_dotenv
from pymongo import MongoClient
from models.user import User

class UserDAOMongo:
    def __init__(self):
        load_dotenv(".env")

        db_host = os.getenv("MONGODB_HOST")
        db_user = os.getenv("DB_USERNAME")
        db_pass = os.getenv("DB_PASSWORD")

        self.client = MongoClient(
            host=db_host,
            port=27017,
            username=db_user,
            password=db_pass,
            authSource="admin"
        )

        self.db = self.client["labo01_db"]
        self.collection = self.db["users"]

    def select_all(self):
        """ Select all users from MongoDB """
        documents = self.collection.find()

        users = []
        for doc in documents:
            users.append(
                User(
                    doc["_id"],
                    doc["name"],
                    doc["email"]
                )
            )

        return users


    def insert(self, user):
        """ Insert given user into MongoDB """
        document = {
            "name": user.name,
            "email": user.email
        }

        result = self.collection.insert_one(document)
        return result.inserted_id


    def update(self, user):
        """ Update given user in MongoDB """
        self.collection.update_one(
            {"_id": user.id},
            {
                "$set": {
                    "name": user.name,
                    "email": user.email
                }
            }
        )

    def delete(self, user_id):
        """ Delete user from MongoDB with given user ID """
        self.collection.delete_one({"_id": user_id})        