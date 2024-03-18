#imports 
from pymongo import MongoClient
import subprocess


def check_mongo_status():
    try:
        # Execute the command to check MongoDB server status
        result = subprocess.run(['mongod', '--version'], capture_output=True, text=True)
        
        # Check if the command was successful
        if result.returncode == 0:
            print("MongoDB is installed and running.")
            return True
        else:
            print("MongoDB is not installed or not running.")
            return False
    
    except FileNotFoundError:
        # Handle the case where 'mongod' command is not found (MongoDB not installed)
        print("MongoDB is not installed.")
        return False

# Usage example:




#create the database client 
def create_mongo_client():


    mongo_status = check_mongo_status()

    if mongo_status:
        try:

            # Attempt to create a MongoClient
            client = MongoClient('localhost', 27017)
            print("MongoDB client created successfully.")
            return client

        except ImportError:
            # Print error message if pymongo is not installed
            print("MongoDB is not installed on this system.")
            return None

        except Exception as e:
            # Print error message if MongoClient creation fails for other reasons
            print("Error creating MongoDB client:", e)
            return None
    
    else:
        return "Mongo Missing"


#make the mongo client 
mongo_client = create_mongo_client()



#the helper class for the mongo functions 
# Helper class for MongoDB functions
class Helper_fun():
    def make_database_and_collection(self, db_name,db_collection):
        """
        Make the database
        """
        # Print the list of existing databases before attempting to create the database
        print("Existing databases before creating '{}':".format(db_name), mongo_client.list_database_names())

        # Make the database if it doesn't exist
        if db_name not in mongo_client.list_database_names():

            #create the database 
            self.db = mongo_client[db_name]

            #create the collection
            self.collection = self.db[db_collection]

            #insert the data 
            # Define dummy data
            dummy_data = {"dummy_data":True}

            # Insert dummy data into the collection
            insert_data = self.collection.insert_one(dummy_data)

            print("Database '{}' created.".format(db_name))
        else:
            self.db = mongo_client[db_name]
            print("Database '{}' already exists.".format(db_name))
        
        # Print the list of existing databases after attempting to create the database
        print("Existing databases after creating '{}':".format(db_name), mongo_client.list_database_names())


    def make_collection(self,db_name,collection_name):
        """
        make the colcection in the database
        """

        #make the collection in the datbase

        pass





helper = Helper_fun()
helper.make_database_and_collection("articles","projects")
