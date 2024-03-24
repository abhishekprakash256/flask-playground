def dummy():

    articles_json = {
        "article_name": "patching-unpatching",
        "aticle_data": [
            {"title": "Article 1 Title", "image": "", "article_para": "", "markdown_data": "Article 1 Markdown"},
            {"title": "Article 2 Title", "image": "image2.jpg", "article_para": "Article 2 Paragraph", "markdown_data": "Article 2 Markdown"},
        ],
        "card_one_text": "Some quick example text to build on the card title and make up the bulk of the card's content",
        "image_url_card_one": "..\\static\\images\\misc\\cards.jpg",
        "card_two_text": "Some quick example text to build on the card title and make up the bulk of the card's content",
        "image_url_card_two": "..\\static\\images\\misc\\cards.jpg",
        "card_three_text": "Some quick example text to build on the card title and make up the bulk of the card's content",
        "image_url_card_three": "..\\static\\images\\misc\\cards.jpg"
    }

    #page_data = {"articles_data": articles_json}  # Assuming there are other data in page_data
    
    # Accessing article data
    article_data = articles_json["aticle_data"]
    for article in article_data:
        title = article["title"]
        image = article["image"]
        article_para = article["article_para"]
        markdown_data = article["markdown_data"]
        print("Title:", title)
        print("Image:", image)
        print("Article Paragraph:", article_para)
        print("Markdown Data:", markdown_data)

    print(articles_json['article_name']) 
    print(articles_json['card_one_text'])
    


print(dummy())

