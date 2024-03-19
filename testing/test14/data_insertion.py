#imports 
from pymongo import MongoClient
import subprocess


#const values
#db_name = "articles"
#collections = ["projects","tech","life"]



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



def show_article_data(db_name,collection_name,article_name):
    """
    Find the specific data from the collection
    """

    db = mongo_client[db_name]
    collection = db[collection_name]

    if collection is not None:
        # Retrieve all documents in the collection
        page_data = collection.find_one(article_name)
    
    return page_data


#data = show_article_data(db_name,collections[0],{'article_name': 'patching-unpatching'})

#print(data)