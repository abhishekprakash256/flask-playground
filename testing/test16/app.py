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



def dummy():
    articles_json = [
        {"title": "Article 1 Title", "image": "image1.jpg", "article_para": "Article 1 Paragraph", "markdown_data": "Article 1 Markdown"},
        {"title": "Article 2 Title", "image": "image2.jpg", "article_para": "Article 2 Paragraph", "markdown_data": "Article 2 Markdown"}
        # Add more articles as needed
    ]

    page_data = {"articles_data": articles_json}  # Assuming there are other data in page_data

    if page_data is None:
        return "Page data is missing or invalid."

    return render_template('projects/dummy.html', **page_data)






@app.route('/projects/<article_name>')
def article_first(article_name):

    page_data = get_article_data(db_name[0],collections[0],{'article_name': article_name})

    return render_template('projects/article.html', **page_data)




if __name__ == '__main__':
    app.run(debug=True)