#imports 
from mongo_helper import * 
from read_data import *


#const files
File_PATH = "../static/article_data.json"
db_name = "articles"
collections = ["projects","tech","life"]


page_data_list = read_page_data_from_json(File_PATH)

# Create an instance of the Helper_fun class
helper = Helper_fun()

# Make the database and collection
helper.make_database_and_collection(db_name, collections[0])

#delete the dummy data from 1st collection
helper.delete_data(db_name,collections[0],{'dummy_data': True})

#make the collections 
helper.make_collections(db_name,collection_lst[1])
helper.make_collections(db_name,collection_lst[2])

#show the collections
helper.show_collections(db_name)

#insert the data in collection 0 
helper.insert_data(db_name,collections[0],page_data_list)

#show the data 
helper.show_data(db_name,collections[0])

#the data insertion is working and tested 


