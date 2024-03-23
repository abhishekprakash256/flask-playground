def dummy():
    articles_json = [
        {"title": "Article 1 Title", "image": "image1.jpg", "article_para": "Article 1 Paragraph", "markdown_data": "Article 1 Markdown"},
        {"title": "Article 2 Title", "image": "image2.jpg", "article_para": "Article 2 Paragraph", "markdown_data": "Article 2 Markdown"}
        # Add more articles as needed
    ]

    page_data = {"articles_data": articles_json}  # Assuming there are other data in page_data

    if page_data is None:
        return "Page data is missing or invalid."
    
    return page_data


print(dummy())

