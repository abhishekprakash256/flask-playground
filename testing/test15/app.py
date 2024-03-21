"""
make the main app for the website 

"""
#imports
import json
from flask import Flask, render_template,abort

from read_data_mongo import get_article_data


#const
db_name = ["articles"]
collections = ["projects","tech","life"]


app = Flask(__name__)

app.config['STATIC_FOLDER'] = 'static'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

#use this in future for each section till artcles need to be passed
@app.route('/section')
def section():

    #page_data = get_article_data(db_name[0],collections[0],{'article_name': article_name})

    return render_template('section.html')


@app.route('/<section_name>')
def tech(section_name):
        
        
    page_data = {
        "section_name": "Tech",
        "card_one_texts": [
            "Some quick example text to build on the card title and make up the bulk of the card's content",
            "Some quick example text to build on the card title and make up the bulk of the card's content",
            "Some quick example text to build on the card title and make up the bulk of the card's content",
            "Some quick example text to build on the card title and make up the bulk of the card's content",
            "Some quick example text to build on the card title and make up the bulk of the card's content",
            "Some quick example text to build on the card title and make up the bulk of the card's content",
            "Some quick example text to build on the card title and make up the bulk of the card's content",
            "Some quick example text to build on the card title and make up the bulk of the card's content",
            "Some quick example text to build on the card title and make up the bulk of the card's content",
        ],

        "image_urls_card_one": [
            "../static/images/misc/cards.jpg",
             "../static/images/misc/cards.jpg",
              "../static/images/misc/cards.jpg",
               "../static/images/misc/cards.jpg",
                "../static/images/misc/cards.jpg",
                 "../static/images/misc/cards.jpg",
                  "../static/images/misc/cards.jpg",
                   "../static/images/misc/cards.jpg",
                    "../static/images/misc/cards.jpg",
        ],

                "card_first_urls": [
            "../static/images/misc/cards.jpg",
             "../static/images/misc/cards.jpg",
              "../static/images/misc/cards.jpg",
               "../static/images/misc/cards.jpg",
                "../static/images/misc/cards.jpg",
                 "../static/images/misc/cards.jpg",
                  "../static/images/misc/cards.jpg",
                   "../static/images/misc/cards.jpg",
                    "../static/images/misc/cards.jpg",
        ],




        "more_link": "..\\static\\images\\misc\\cards.jpg"
    }

    return render_template('section.html',**page_data)



"""
@app.route('/projects')
def projects():

    return render_template('section.html')


@app.route('/life')
def life():

    return render_template('section.html')
"""


@app.route('/projects/<article_name>')
def article_first(article_name):

    page_data = get_article_data(db_name[0],collections[0],{'article_name': article_name})

    return render_template('projects/article.html', **page_data)




if __name__ == '__main__':
    app.run(debug=True)