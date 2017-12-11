from flask import Flask,render_template
app = Flask(__name__)
from flask_restplus import Resource, Api


@app.route("/")
def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()