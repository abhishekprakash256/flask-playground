"""
make the main app for the website 
dummy code

"""
#imports
from flask import Flask, render_template
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

@app.route('/patching')
def project():
    return render_template('patching.html')


#make these two function combined and use a json file too read the template and injest data as per requested 
@app.route('/projects/<article_name>')
def article(article_name):

    page_data2 = get_article_data(db_name,collections[0],{'article_name': 'patching-unpatching'})

    return render_template('projects/patching-unpatching/patching-unpatching.html', **page_data2)


@app.route('/test/article')
def article_test(article_name):

    page_data = get_article_data(db_name,collections[0],{'article_name': 'another-article'})

    return render_template('projects/patching-unpatching/patching-unpatching.html', **page_data)  




if __name__ == '__main__':
    app.run(debug=True)