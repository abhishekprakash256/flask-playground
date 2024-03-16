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
def article(article_name):
    page_data = {
        'article_name': 'patching-unpatching',
        'titles': [
            'First Heading',
            'Second Heading',
            'Third Heading'
        ],

        'image_src': '..\static\images\projects\patching-unpatching\patching.png',
        'article_paras': [
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.  It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.  It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
        ],
        'card_one_text': "Some quick example text to build on the card title and make up the bulk of the card's content",
        'image_url_card_one': "../static/images/misc/cards.jpg",
        'card_two_text': "Some quick example text to build on the card title and make up the bulk of the card's content",
        'image_url_card_two': "../static/images/misc/cards.jpg",
        'card_three_text': "Some quick example text to build on the card title and make up the bulk of the card's content",
        'image_url_card_three': "../static/images/misc/cards.jpg"

    }

    return render_template('projects/patching-unpatching/patching-unpatching.html', **page_data)



if __name__ == '__main__':
    app.run(debug=True)