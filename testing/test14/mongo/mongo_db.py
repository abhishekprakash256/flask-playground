from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient()

# Create a new database
db = client["articles"]


# List the databases to verify
print("List of databases after creating 'articles':")
print(client.list_database_names())
