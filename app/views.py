from flask import render_template

from flask import current_app as app
from .controller import user_info


@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html", user_info=user_info())


@app.route("/about")
def about():
    info = "I'm write my first Flask app!"
    checker = True
    return render_template("about.html", checker=checker, info=info, user_info=user_info())


@app.route("/projects")
def projects():
    projects_list = ['project1', 'project2', 'project3', 'project4', 'project5', 'project6', 'project7']
    return render_template("projects.html", projects_list=projects_list, user_info=user_info())


@app.route("/contacts")
def contacts():
    contact_dict = {
        'Cell': '123456789',
        'Email': 'email@gmail.com',
        'Telegram': '@nickname'
    }
    return render_template("contacts.html", contacts_dict=contact_dict, user_info=user_info())


@app.errorhandler(404)
def page_not_found():
    return render_template('404.html')
