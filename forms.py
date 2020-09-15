from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class FirstForm(FlaskForm):
    username = StringField('Name',
                            validators=[DataRequired(), Length(min=2, max=10)])
    email = StringField('Mail likh Bhai',
                            validators=[DataRequired(), Email()])
    password = PasswordField('Password h, Keep it Strong',
                            validators=[DataRequired()])
    confirm_password = PasswordField('Check if it is Strong',
                            validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Bhar du Bhai?')

class SecondForm(FlaskForm):
    email = StringField('Mail likh Bhai',
                        validators=[DataRequired(), Email()])
    password = PasswordField('PassWord Yad h na',
                             validators=[DataRequired()])
    remember = BooleanField('Yaad rkhu?')
    submit = SubmitField('Pakka na Bhai')

