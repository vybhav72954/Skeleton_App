from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class FirstForm(FlaskForm):
    # TODO Change the Screen Outputs
    username = StringField('Whats Your Name???',
                            validators=[DataRequired(), Length(min=2, max=10)])
    nickname = StringField('What Sh ould I call You??? (P.S.-Nickname?)',
                           validators=[ Length(min=2, max=10)])
    email = StringField('Your E-Mail',
                            validators=[DataRequired(), Email()])
    password = PasswordField('Password, Keep it Strong ;)',
                            validators=[DataRequired()])
    confirm_password = PasswordField('Check if it\'s Strong',
                            validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Recheck n Click')

class SecondForm(FlaskForm):
    # TODO Change the Screen Outputs
    email = StringField('E-Mail',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password (Secret)',
                             validators=[DataRequired()])
    remember = BooleanField('Shall I remember these?')
    submit = SubmitField('Let\'s Go')

