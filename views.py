# FLASK IS CONTROLLER MODEL
# VIEW -- TEMPLATES
# MODEL
# app. route(__name__) return webapp
# aap.route --create request


from flask import Flask
from flask import render_template
from datetime import datetime
from . import app


posts = [
    {
        "author": "author",
        "title": "sindhi",
        "date_posted": "jan2023"
    },
    {
        "author": "author",
        "title": "English",
        "date_posted": "feb2023"
    },
]


@app.route("/")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about/")
def about():
    return render_template('about.html', title='about')


# @app.route("/contact/")
# def contact():
#     return render_template("contact.html")


# @app.route("/hello/")
# @app.route("/hello/<name>")
# def hello_there(name=None):
#     return render_template(
#         "hello_there.html",
#         name=name,
#         date=datetime.now()
#     )


@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")


# name is our module name
# if __name__ == '__main__':
#     app.run()
