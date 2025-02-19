from flask import Flask, request, jsonify
import git
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Testing auto delivery. After update, check re compile</h1>"

@app.route('/about')
def about():
    return "<h1>About Page</h1><p>This is a simple Flask application.</p>"

@app.route('/webhook', methods=['POST'])
def webhook():
    """
    GitHub webhook that automatically pulls the latest changes from the repository.
    """
    try:
        repo = git.Repo("/home/bmgt407Caifu/flask-app")  # Change this path
        origin = repo.remotes.origin
        origin.pull()
        subprocess.run(["pip", "install", "-r", f"{repo_path}/requirements.txt"], check=True)
        return jsonify({"message": "Repo updated successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
