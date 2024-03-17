from pymongo import MongoClient


#class for the database connection ini
class Connector():
    
    def connect_db(self):
        self.client = MongoClient()
    


