from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import Length, InputRequired, Regexp, DataRequired


class FamiliarForm(FlaskForm):
    last_name = StringField('Last Name', validators=[InputRequired(), Length(min=3, max=20)])
    first_name = StringField('First Name', validators=[InputRequired(), Length(min=3, max=20)])
    phone_number = StringField('Phone Number',
                               validators=[InputRequired(), Regexp('[0-9]{7}', message='Min Length - 7'),
                                           Length(min=7, max=7)])
    gender = SelectField('Gender', choices=[('male', 'male'), ('female', 'female')])
    birth_date = StringField('Birth Date')
    category = SelectField('Category', coerce=int)
    hobby = StringField('Hobby', validators=[InputRequired(), Length(min=3, max=20)])


class CategoryForm(FlaskForm):
    name = StringField('Category name', validators=[DataRequired(), Length(min=0, max=40)])
    submit = SubmitField('')