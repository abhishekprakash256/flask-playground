"""
make the main app for the website 

"""
#imports
import json
from flask import Flask, render_template, request, jsonify

from read_data_mongo import get_article_data

#for test 
import json

#const

#db names in mongo
db_name = ["articles","section"]

#collection names in database 
collections = ["projects","tech","life","section_data"]


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

    page_data = get_article_data(db_name[1],collections[3],{'section_name': section_name})

    print(page_data)

    return render_template('section.html',**page_data)


@app.route('/projects/<article_name>')
def projects(article_name):

    #page_data = {"articles_json": articles_json}

    data = get_article_data(db_name[0],collections[0],{'article_name': article_name}) 
    page_data2 = {"articles_json": data}

    return render_template('projects/article.html', **page_data2)


@app.route('/tech/<article_name>')
def tech(article_name):

    #page_data = {"articles_json": articles_json}

    data = get_article_data(db_name[0],collections[1],{'article_name': article_name}) 
    page_data2 = {"articles_json": data}

    return render_template('projects/article.html', **page_data2)



@app.route('/submit_form', methods=['POST'])
def submit_form():
    # Retrieve form data
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    #printh the data 
    print(name)
    print(email)
    print(message)
    
    # Here you can add code to save the form data to your database or perform any other required actions
    
    # Return a JSON response indicating success
    return jsonify({'success': True, 'message': 'Form data submitted successfully'})


if __name__ == '__main__':
    app.run(debug=True)

    print(submit_form())