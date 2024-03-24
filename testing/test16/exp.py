def dummy():
    articles_json = {
        "articles_data": [
            {
            "title": "Article 1 Title",
            "image": "image1.jpg",
            "article_para": "Article 1 Paragraph",
            "markdown_data": "Article 1 Markdown"
            },
            {
            "title": "Article 2 Title",
            "image": "image2.jpg",
            "article_para": "Article 2 Paragraph",
            "markdown_data": "Article 2 Markdown"
            }
            
        ],
        "card_data": {
            "card_one_text": "Some quick example text to build on the card title and make up the bulk of the card's content",
            "image_url_card_one": "..\\static\\images\\misc\\cards.jpg",
            "card_two_text": "Some quick example text to build on the card title and make up the bulk of the card's content",
            "image_url_card_two": "..\\static\\images\\misc\\cards.jpg",
            "card_three_text": "Some quick example text to build on the card title and make up the bulk of the card's content",
            "image_url_card_three": "..\\static\\images\\misc\\cards.jpg"
        }
        }

    page_data = {"articles_data": articles_json}  # Assuming there are other data in page_data

    if page_data is None:
        return "Page data is missing or invalid."
    
    return page_data


print(dummy())

