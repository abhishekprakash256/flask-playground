from mongo import data_insertion

db_name = "articles"
collections = ["projects","tech","life"]

article_data = data_insertion.helper.show_article_data(db_name,collections[0],{'article_name': 'patching-unpatching'})

print(article_data)