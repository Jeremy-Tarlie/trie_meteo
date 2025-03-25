from pymongo import MongoClient

class Database:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["weather_db"]
        self.collection = self.db["weather_data"]

    def insert_data(self, data):
        """Insère les données dans MongoDB"""
        self.collection.insert_one(data)
        print("✅ Données insérées avec succès.")

    def get_all_data(self):
        """Récupère toutes les données stockées"""
        return list(self.collection.find({}, {"_id": 0})) 
