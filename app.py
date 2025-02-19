from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Testing auto delivery</p>"

@app.route('/about')
def about():
    return "<h1>About Page</h1><p>This is a simple Flask application.</p>"

@app.route('/git_update', methods=['POST'])
def git_update():
    repo = "./bmgt407Caifu"
    origin = repo.remotes.origin
    repo.create_head('master', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
    origin.pull()
    return '', 200

if __name__ == '__main__':
    app.run(debug=True)
