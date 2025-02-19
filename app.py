from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Testing auto delivery</p>"

@app.route('/about')
def about():
    return "<h1>About Page</h1><p>This is a simple Flask application.</p>"

if __name__ == '__main__':
    app.run(debug=True)
