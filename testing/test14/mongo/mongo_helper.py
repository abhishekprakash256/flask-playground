
#imports 
from pymongo import MongoClient
import subprocess



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
            client = MongoClient()
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
db_client = create_mongo_client()



#the helper class for the mongo functions 

class Helper_fun():

    def make_database(self,db_name):
        """
        make the database
        """

        #make the database
        if db_name not in db_client.list_database_names():
        # Create the database
            db = db_client[db_name]
            print("Database '{}' created.".format(db_name))
        else:
            # If the database exists, select it
            db = db_client[db_name]
            print("Database '{}' already exists.".format(db_name))


    def make_collection(self,db_name,collection_name):
        """
        make the colcection in the database
        """

        #make the collection in the datbase

        pass





       





#helper = Helper_fun()
#helper.make_database("articles")
