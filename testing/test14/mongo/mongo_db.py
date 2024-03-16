from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient()

# Get the list of databases
db_list = client.list_database_names()

# Print the list of databases
print("List of databases:")
for db in db_list:
    print(db)
