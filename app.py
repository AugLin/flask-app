from flask import Flask, request, jsonify, render_template, redirect, url_for
import git
import subprocess
import os
from dbhelper import DBHelper

app = Flask(__name__)
db = DBHelper()

@app.route('/')
def home():
    users = db.getRows("SELECT * FROM Users")
    return render_template("index.html", users=users)

@app.route('/addUser', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        db.runQuery("INSERT INTO Users (FullName, Username) VALUES ('" + name + "', '"+ username+"')")
        return redirect(url_for('home'))
    return render_template("add_user.html")

@app.route('/about')
def about():
    return "<h1>About Page</h1><p>This is a simple Flask application.</p>"

@app.route('/webhook', methods=['POST'])
def webhook():
    """
    GitHub webhook that automatically pulls the latest changes from the repository.
    """
    try:
        repo_path = "/home/bmgt407Caifu/flask-app"  # Change this path
        repo = git.Repo(repo_path)
        origin = repo.remotes.origin
        origin.pull()
        subprocess.run(["pip", "install", "-r", f"{repo_path}/requirements.txt"], check=True)
        return jsonify({"message": "Repo updated successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
