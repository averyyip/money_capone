from flask import render_template, jsonify, redirect, flash, request
from app import app

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)