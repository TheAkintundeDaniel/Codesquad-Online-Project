from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

class SurveyForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    interest = StringField('What topics are you interested in?', validators=[DataRequired()])
    skill_level = SelectField('Your skill level:', choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')], validators=[DataRequired()])
    goal = StringField('What are your learning goals?', validators=[DataRequired()])
    submit = SubmitField('Submit')
