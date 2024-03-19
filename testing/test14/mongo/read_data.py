import json
from pymongo import MongoClient


File_PATH = "../static/article_data.json"


def read_page_data_from_json(file_path):
    """
    Read page data from a JSON file and return a list of dictionaries.
    """
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

def insert_page_data_into_mongodb(page_data_list, db_name, collection_name):
    """
    Insert page data into a MongoDB collection.
    """
    client = MongoClient()  # Connect to MongoDB
    db = client[db_name]     # Select the database
    collection = db[collection_name]  # Select the collection

    # Insert each page data dictionary into the collection
    for page_data in page_data_list:
        collection.insert_one(page_data)
    print("Page data inserted into MongoDB successfully.")

# Path to the JSON file

def retrieve_page_data_from_mongodb(db_name, collection_name):
    """
    Retrieve page data from MongoDB collection.
    """
    client = MongoClient()  # Connect to MongoDB
    db = client[db_name]     # Select the database
    collection = db[collection_name]  # Select the collection

    # Query the collection to retrieve all documents
    documents = collection.find()

    # Return a list of retrieved documents
    return list(documents)

# Database name and collection name in MongoDB


# Retrieve the page data from MongoDB

db_name = 'test-database'
collection_name = 'test-collection'

# Print the retrieved page data


page_data = retrieve_page_data_from_mongodb(db_name, collection_name)

for data in page_data:
    print(data)

# Database name and collection name in MongoDB


# Read the page data from the JSON file
#page_data_list = read_page_data_from_json(File_PATH)



# Insert the page data into MongoDB
#insert_page_data_into_mongodb(page_data_list, db_name, collection_name)
