import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Test Content</h1>"

#app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)
app.run(host=os.getenv('IP'), port=int(5000), debug=True)