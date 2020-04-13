"""
Main module of the server file
"""
from flask import Flask, flash, request, redirect, render_template
import connexion
from flask_cors import CORS
import os

app = connexion.App(__name__, specification_dir="./")
cors = CORS(app.app, resources={r"/api/*": {"origins": "*"}})

app.add_api("swagger.yml")

# Create a URL route in our application for "/"
@app.route("/")
def home():
    """
    This function just responds to the browser URL
    localhost:5000/

    :return:        the rendered template "home.html"
    """
    return render_template("home.html")


if __name__ == "__main__":
    app.run(host = '0.0.0.0',debug=True, port=int
    (os.environ.get("PORT", 5000)))
