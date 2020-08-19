from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='posgresql://postgres:postgres123@localhost/height_collector'
db=SQLAlchemy(app)

class Datq(db.Model)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    if request.method == 'POST':
        email=request.form["email_name"]
        height = request.form["height_name"]
        print(email,height)
        return render_template("success.html")

if __name__ == '__main__':
    app.debug = True
    app.run()
