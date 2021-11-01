from flask import render_template, session, flash, redirect, url_for
import json
from . import app
from .controller import user_info, validate_fields, json_data
from .forms import LoginForm, DocRegistration


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


@app.route("/form", methods=['GET', 'POST'])
def form():
    form = LoginForm()

    flash('Password value must be --> password or secret')
    if form.validate_on_submit():
        return f'<h1>The username is {form.username.data}. The password is {form.password.data}</h1>'
    return render_template('form.html', form=form, user_info=user_info())


@app.route("/doc_registration", methods=['GET', 'POST'])
def doc_registration():
    doc_reg = DocRegistration()
    validate_fields(doc_reg)

    if doc_reg.validate_on_submit():
        session['email'] = doc_reg.email.data
        json_data(doc_reg)
        flash('Data successfully added to json')
        return redirect(url_for('doc_registration'))

    try:
        session_data = session['email']
    except KeyError:
        return render_template('doc_registration.html', doc_reg=doc_reg)

    with open('data.json') as file:
        data = json.load(file)

    return render_template('doc_registration.html', doc_reg=doc_reg, email=session_data,
                           number=data[session_data]['number'], pin=data[session_data]['pin'],
                           year=data[session_data]['year'], serial=data[session_data]['serial'],
                           doc_number=data[session_data]['doc_number'])
