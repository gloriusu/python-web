from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, AnyOf

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired('A username is required'),
                                                   Length(min=5, max=10,
                                                          message='Username length must be in range 5-10')])
    password = PasswordField('password', validators=[InputRequired('Password is required'),
                                                     AnyOf(values=['password', 'secret'])])


@app.route("/form", methods=['GET', 'POST'])
def form():
    form = LoginForm()

    flash('Password value must be --> password or secret')
    if form.validate_on_submit():
        return f'<h1>The username is {form.username.data}. The password is {form.password.data}</h1>'
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
