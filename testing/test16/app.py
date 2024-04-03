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

#test demo for website 
@app.route('/demo')
def project_demo():
    return render_template('exp.html')


@app.route('/tech/<article_name>')
def tech(article_name):

    #page_data = {"articles_json": articles_json}

    data = get_article_data(db_name[0],collections[1],{'article_name': article_name}) 
    page_data2 = {"articles_json": data}

    return render_template('projects/article.html', **page_data2)


#store the data in the json file
def store_form_data(name, email, message):
    # Create a dictionary with the form data
    form_data = {
        'name': name,
        'email': email,
        'message': message
    }
    
    # Open the JSON file in append mode
    with open('form_data.json', 'a') as file:
        # Write the form data to the file
        json.dump(form_data, file)
        file.write('\n')  # Add a new line for each entry
    print("Form data saved to JSON file successfully")



@app.route('/submit_form', methods=['POST'])
def submit_form():
    # Retrieve form data
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    #the data stored in the json file 
    store_form_data(name, email, message)

    return jsonify({'success': True, 'message': 'Form data submitted successfully'})

if __name__ == '__main__':
    app.run(debug=True)