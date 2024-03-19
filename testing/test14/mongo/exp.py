from mongo_helper import * 
"""
db_name = "articles"
collections = ["projects","tech","life"]

# Create an instance of the Helper_fun class
helper = Helper_fun()

helper.show_data(db_name,collections[0])
"""
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient()

# Access the database and collection
db = client['articles']  # Replace 'your_database_name' with your actual database name
collection = db['projects']  # Replace 'your_collection_name' with your actual collection name

# Query for documents with article_name "patching-unpatching"
page_data = collection.find_one({'article_name': 'patching-unpatching'})

page_data2 = collection.find_one({'article_name': 'another-article'})
"""
# Iterate over the cursor to retrieve documents
for document in page_data:
    # Access the data block for "patching-unpatching" article
    article_data = {
        'article_name': document['article_name'],
        'titles': document['titles'],
        'image_src': document['image_src'],
        'article_paras': document['article_paras'],
        'card_one_text': document['card_one_text'],
        'image_url_card_one': document['image_url_card_one'],
        'card_two_text': document['card_two_text'],
        'image_url_card_two': document['image_url_card_two'],
        'card_three_text': document['card_three_text'],
        'image_url_card_three': document['image_url_card_three']
    }
    # Process the article_data block as needed
    print(article_data)
"""
print(page_data2)