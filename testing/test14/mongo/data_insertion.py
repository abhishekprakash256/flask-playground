#imports 
from mongo_helper import * 
import json



File_PATH = "../static/article_data.json"


def read_page_data_from_json(file_path):
    """
    Read page data from a JSON file and return a list of dictionaries.
    """
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data



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


page_data_list = read_page_data_from_json(File_PATH)

helper.insert_data_one(page_data_list)

#helper.delete_data({'dummy2': True})

#helper.show_collections()
