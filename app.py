import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def health_check():
    return 'this app is up and running'

if __name__ == '__main__':
    app.run(debug=True)