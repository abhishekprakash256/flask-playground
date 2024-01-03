from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

lst = []

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        lst.append([[name],[email]])
        print(lst)
        return "Thanks for your Message"



if __name__ == '__main__':
    app.run(debug=True)
