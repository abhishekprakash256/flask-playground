"""
make the main app for the website 
dummy code

"""

from flask import Flask, render_template


app = Flask(__name__)


app.config['STATIC_FOLDER'] = 'static'

@app.route('/')
def home():
    return render_template('new.html')


@app.route('/nav_bar')
def test():
    return render_template('nav_bar.html')



@app.route('/body')
def body():
    return render_template('body.html')



@app.route('/full')
def about():
    return render_template('full-body.html')

@app.route('/blog')
def contact():
    return render_template('blog_page.html')


@app.route('/card')
def card():
    return render_template('card_page.html')

if __name__ == '__main__':
    app.run(debug=True)

