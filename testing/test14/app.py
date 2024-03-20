"""
make the main app for the website 
dummy code

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

# Load the route-template mapping and article data from the JSON file
"""
with open('./static/route_template_map.json', 'r') as file:
    route_template_map = json.load(file)
    #print(route_template_map)
"""


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/showcase')
def card():
    return render_template('showcase.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/patching')
def project():
    return render_template('patching.html')



@app.route('/projects/<article_name>')
def article_first(article_name):

    page_data = get_article_data(db_name,collections[0],{'article_name': article_name})

    print(page_data)

    return render_template('projects/article.html', **page_data)


"""
@app.route('/test/article')
def article_test(article_name):

    page_data = get_article_data(db_name,collections[0],{'article_name': 'another-article'})

    return render_template('projects/federated-learning/federated-learning.html', **page_data)  


@app.route('/projects/<article_name>')
def article_first(article_name):

    if article_name not in route_template_map:
        abort(404)

    template_path = route_template_map[article_name]["template_path"]
    page_data = get_article_data(db_name,collections[0],{'article_name': article_name})

    print(page_data)

    return render_template(template_path, **page_data)
"""



if __name__ == '__main__':
    app.run(debug=True)