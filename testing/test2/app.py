
from flask import Flask, render_template

app = Flask(__name__)



@app.route("/")
def homepage():
    """View function for Home Page."""
    return render_template("index.html")


@app.route("/about")
def about():
    """view the about page"""
    return render_template("about.html")

@app.route("/contact")
def contact():
    """view the contact page"""
    return render_template("contact.html")

#add the code for the button click 
@app.route('/contact', methods=['POST'])
def button_click():
    # Code to execute when the button is clicked
    # You can add your custom logic here
    # For example, update a database, perform calculations, etc.
    return render_template("contact.html")




if __name__ == '__main__':  
   app.run()