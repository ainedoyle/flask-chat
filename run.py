import os
from datetime import datetime
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello There</h1>"
    
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)