from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from anemiasistem.models import User, Post


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')

class AddData (FlaskForm):

    name = StringField('Emri dhe mbiemri i pacientit',validators=[DataRequired(), Length(min=2, max=30)])

    #gender = SelectField('Gjinia', choices=[('f', 'Femer'), ('m', 'Mashkull')])

    gender = StringField('Gjinia',validators=[DataRequired()])

    rbc = StringField('RBC Rruazat e kuqe te gjakut',validators=[DataRequired()])

    hct = StringField('HCT Hematokriti ',validators=[DataRequired()])

    hb = StringField('Hb Hemoglobina ',validators=[DataRequired()])

    mcv = StringField('MCV Madhësia mesatare e qelizave të kuqe të gjakut',validators=[DataRequired()])

    mch = StringField('MCH Sasia e hemoglobinës për çdo qelizë të kuqe të gjakut',validators=[DataRequired()])

    b12 = StringField('Vitamina B12')

    af = StringField('Acidi Folik')

    submit = SubmitField('Submit')




