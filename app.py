from flask import Flask
import git

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Testing auto delivery</h1>"

@app.route('/about')
def about():
    return "<h1>About Page</h1><p>This is a simple Flask application.</p>"

@app.route('/git_update')
def git_update():
    try:
        repo = git.Repo("./bmgt407Caifu")  # Correctly initialize the repo
        origin = repo.remotes.origin  # Get remote repo
        origin.pull()  # Pull latest changes
        return "Updated successfully!", 200
    except Exception as e:
        return f"Error: {str(e)}", 500  # Debugging error message

if __name__ == '__main__':
    app.run(debug=True)
