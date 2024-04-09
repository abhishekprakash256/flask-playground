"""
make the main app for the website 

"""
#imports
import json
import os 
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



#the demo route for projects
@app.route('/demo/<project_name>')
def project_demo(project_name):
    # Define nested data dictionary with project names as keys
    demo_data = {
        'project_urls': {
            'academic-website': "projects/Academic-Website/index.html",
            'another-project': "projects/Another-Project/index.html",
            # Add more projects and their URLs as needed
        }
    }
    return render_template('reusable/demo.html', project_name= project_name, data=demo_data)





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
    
    # Append the form data to a list or create a new list if the file doesn't exist
    form_data_list = []
    if os.path.exists('form_data.json'):
        with open('form_data.json', 'r') as list_file:
            try:
                form_data_list = json.load(list_file)
            except json.decoder.JSONDecodeError:
                pass
    
    form_data_list.append(form_data)
    
    # Write the list to the JSON file
    with open('form_data.json', 'w') as list_file:
        json.dump(form_data_list, list_file, indent=4)
    print("Form data saved to list in JSON file successfully")





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