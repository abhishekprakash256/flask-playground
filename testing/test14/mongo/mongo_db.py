from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient()

# Create a new database
db = client["articles"]

# Select the collection
collection_name = "projects"
collection = db[collection_name]

# List the collections to verify
print("List of collections after creating '{}' collection:".format(collection_name))
print(db.list_collection_names())

# Verify if the collection exists
print("Collection '{}' created:".format(collection_name), collection_name in db.list_collection_names())
