#imports 
from mongo_helper import * 
from read_data import *
import json


#const files
File_PATH = "../static/article_data.json"
db_name = "articles"
collections = ["projects","tech","life"]


page_data_list = read_page_data_from_json(File_PATH)

# Create an instance of the Helper_fun class
helper = Helper_fun()

# Make the database and collection
helper.make_database_and_collection(db_name, collections[0])
helper.make_database_and_collection(db_name, collections[1])
helper.make_database_and_collection(db_name, collections[2])



