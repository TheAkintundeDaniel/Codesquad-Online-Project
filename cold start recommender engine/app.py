from flask import Flask, render_template, request, redirect, url_for
from models import db, User
from forms import SurveyForm
from recommendations import recommend_courses

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db.init_app(app)

@app.before_request
def create_tables():
    app.before_request_funcs[None].remove(create_tables)
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def survey():
    form = SurveyForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            interest=form.interest.data,
            skill_level=form.skill_level.data,
            goal=form.goal.data
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('recommend', user_id=user.id))
    return render_template('survey.html', form=form)

@app.route('/recommend/<int:user_id>')
def recommend(user_id):
    user = User.query.get(user_id)
    recommended_courses = recommend_courses(user.interest, user.skill_level)
    return render_template('recommendations.html', courses=recommended_courses)

if __name__ == '__main__':
    app.run(debug=True)
