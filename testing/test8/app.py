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


@app.route('/navbar')
def test():
    return render_template('navbar.html')



@app.route('/body')
def body():
    return render_template('body.html')



@app.route('/footer')
def about():
    return render_template('footer.html')

@app.route('/blog')
def contact():
    return render_template('blog.html')


@app.route('/showcase')
def card():
    return render_template('showcase.html')

if __name__ == '__main__':
    app.run(debug=True)