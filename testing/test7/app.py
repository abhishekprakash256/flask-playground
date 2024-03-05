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


"""
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
"""


if __name__ == '__main__':
    app.run(debug=True)

