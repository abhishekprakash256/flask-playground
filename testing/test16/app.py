"""
make the main app for the website 

"""
#imports
import json
from flask import Flask, render_template,abort

from read_data_mongo import get_article_data

#for test 
import json

#const

#db names in mongo
db_name = ["articles","section"]

#collection names in database 
collections = ["projects","section_data"]


app = Flask(__name__)

app.config['STATIC_FOLDER'] = 'static'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/<section_name>')
def section(section_name):

    page_data = get_article_data(db_name[1],collections[1],{'section_name': section_name})

    print(page_data)

    return render_template('section.html',**page_data)


@app.route('/dummy/<article_name>')
def dummy(article_name):
    articles_json = {
        "article_name": "patching-unpatching",
        "aticle_data": [
            {"title": "Article 1 Title", "image_src": "..\\static\\images\\projects\\patching-unpatching\\patching.png", "article_para": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.  It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum", "markdown_data": ""},
            {"title": "Article 2 Title", "image_src": "", "article_para": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.  It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum", "markdown_data": "## Project Description\n\nPatching and Unpatching are a set of tools that are used for image processing. The patching tool is used to cut small square sections of the input image known as patches. The unpatching tool takes those patches and combines them back together to make the final image.\n\n## Installation\n\n```python\npoetry build\npoetry install patching_unpatching-1.0-py3-none-any.whl\n```\n\n## To use\n\n```python\nfrom patching_unpatching.patching_unpatching import patching_input, unpatching\n```"},
        ],
        "card_one_text": "Some quick example text to build on the card title and make up the bulk of the card's content",
        "image_url_card_one": "..\\static\\images\\misc\\cards.jpg",
        "card_first_url": "https://www.meabhi.me",
        "card_two_text": "Some quick example text to build on the card title and make up the bulk of the card's content",
        "image_url_card_two": "..\\static\\images\\misc\\cards.jpg",
        "card_three_text": "Some quick example text to build on the card title and make up the bulk of the card's content",
        "image_url_card_three": "..\\static\\images\\misc\\cards.jpg"
    }

    data = get_article_data(db_name[0],collections[0],{'article_name': article_name}) 

    print(data)
    
    #page_data = {"articles_json": articles_json}
    page_data2 = {"articles_json": data}




    return render_template('projects/dummy.html', **page_data2)






@app.route('/projects/<article_name>')
def article_first(article_name):

    page_data = get_article_data(db_name[0],collections[0],{'article_name': article_name})

    return render_template('projects/article.html', **page_data)




if __name__ == '__main__':
    app.run(debug=True)