"""
make the main app for the website 
dummy code

"""

from flask import Flask, render_template


app = Flask(__name__)


app.config['STATIC_FOLDER'] = 'static'

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/article')
def article():
    return render_template('article-page.html')


@app.route('/showcase')
def card():
    return render_template('showcase.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/patching')
def project():
    return render_template('patching.html')


@app.route('/project/<article_name>')
def article_test(article_name):
    page_data = {
        'article_name': 'patching-unpatching',
        'first_heading': 'this is heading',
        'para_content': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        'second_heading': "This is heading",
    }
    return render_template('article-page-test.html', **page_data)



if __name__ == '__main__':
    app.run(debug=True)