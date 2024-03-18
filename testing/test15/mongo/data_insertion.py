#imports 
from mongo_helper import * 




#const values
collection_lst = ["projects","tech","life"]

# Create an instance of the Helper_fun class
helper = Helper_fun()

# Make the database and collection
helper.make_database_and_collection("articles", "projects")

#make the collectios
for val in collection_lst:
    helper.make_collections(val)

# Show the data in the collection
helper.show_data()

#helper.insert_data_one({"dummy2":True})

#helper.delete_data({'dummy2': True})

helper.show_collections()
