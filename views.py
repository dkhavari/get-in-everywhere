from app import app
from flask import render_template, request, redirect, url_for

# Homepage.
@app.route("/index.html")
@app.route("/")
def index():
	return render_template("index.html")