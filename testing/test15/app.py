"""
make the main app for the website 

"""
#imports
import json
from flask import Flask, render_template,abort

from read_data_mongo import get_article_data


#const
db_name = "articles"
collections = ["projects","tech","life"]


app = Flask(__name__)

app.config['STATIC_FOLDER'] = 'static'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/showcase')
def card():
    return render_template('showcase.html')


@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/projects/<article_name>')
def article_first(article_name):

    page_data = get_article_data(db_name,collections[0],{'article_name': article_name})

    return render_template('projects/article.html', **page_data)



if __name__ == '__main__':
    app.run(debug=True)