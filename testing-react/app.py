from flask import Flask, jsonify, request

app = Flask(__name__)

# Example GET endpoint
@app.route('/')
def index():
    # Return a simple HTML string directly
    return "<h1>Welcome to the Home Page!</h1>"


@app.route('/data', methods=['GET'])
def get_data():
    data = {"message": "Hello from Flask!", "number": 42}
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)