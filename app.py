from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello_page():
    return jsonify({"message" : "Hello"})


if __name__ == '__main__':
    app.run(debug=True)