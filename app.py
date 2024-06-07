from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///survey.db'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)


class Survey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    end_date = db.Column(db.DateTime, nullable=False)
    questions = db.relationship('Question', backref='survey', lazy=True)
    responses = db.relationship('Response', backref='survey', lazy=True)


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    survey_id = db.Column(db.Integer, db.ForeignKey('survey.id'), nullable=False)
    question_text = db.Column(db.String(500), nullable=False)
    question_type = db.Column(db.String(50), nullable=False)  # 'multiple_choice' or 'free_form'
    choices = db.Column(db.String(500))  # Comma-separated choices for multiple-choice questions


class Response(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    survey_id = db.Column(db.Integer, db.ForeignKey('survey.id'), nullable=False)
    responder_id = db.Column(db.Integer, nullable=True)  # Anonymous responses allowed
    answers = db.relationship('Answer', backref='response', lazy=True)


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    response_id = db.Column(db.Integer, db.ForeignKey('response.id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    answer_text = db.Column(db.String(500), nullable=True)
    choice_id = db.Column(db.Integer, nullable=True)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.before_first_request
def create_tables():
    db.create_all()


def close_survey(survey_id):
    # Your code to mark the survey as closed in the database
    pass


def get_survey_responses(survey_id):
    # Your code to retrieve all responses for a closed survey from the database
    return SurveyResponse.query.filter_by(survey_id=survey_id).all()


def generate_summary(responses):
    # Your code to process responses and generate a summary
    summary = {}  # Placeholder for summary data
    for response in responses:
        # Process response and aggregate data
        pass
    return summary


@app.route('/survey_summary/<int:survey_id>')
@login_required
def survey_summary(survey_id):
    survey = Survey.query.get_or_404(survey_id)
    responses = get_survey_responses(survey_id)
    summary = generate_summary(responses)
    return render_template('survey_summary.html', survey=survey, summary=summary)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully. You can now login.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/create_survey', methods=['GET', 'POST'])
@login_required
def create_survey():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        end_date = datetime.strptime(request.form.get('end_date'), '%Y-%m-%d')
        questions = request.form.getlist('questions')
        question_types = request.form.getlist('question_types')
        choices = request.form.getlist('choices')

        if len(questions) < 5 or len(questions) > 20:
            flash('Survey must have between 5 and 20 questions.')
            return redirect(url_for('create_survey'))

        new_survey = Survey(title=title, description=description, creator_id=current_user.id, end_date=end_date)
        db.session.add(new_survey)
        db.session.commit()

        for i in range(len(questions)):
            new_question = Question(
                survey_id=new_survey.id,
                question_text=questions[i],
                question_type=question_types[i],
                choices=choices[i] if question_types[i] == 'multiple_choice' else None
            )
            db.session.add(new_question)

        db.session.commit()
        return redirect(url_for('index'))

    return render_template('create_survey.html')


@app.route('/survey/<int:survey_id>', methods=['GET', 'POST'])
def survey(survey_id):
    survey = Survey.query.get_or_404(survey_id)
    if request.method == 'POST':
        if datetime.utcnow() > survey.end_date:
            return "Survey is closed."

        response = Response(survey_id=survey_id)
        db.session.add(response)

        for question in survey.questions:
            answer_text = request.form.get(f'question_{question.id}_text')
            answer_choice = request.form.get(f'question_{question.id}_choice')

            if answer_choice:
                response.answers.append(Answer(question_id=question.id, choice_id=answer_choice))
            elif answer_text:  # Check if there's a text response
                response.answers.append(Answer(question_id=question.id, answer_text=answer_text))

        db.session.commit()
        return redirect(url_for('index'))

    return render_template('respond_survey.html', survey=survey)


@app.route('/responses/<int:survey_id>')
@login_required
def view_responses(survey_id):
    survey = Survey.query.get_or_404(survey_id)
    questions = survey.questions
    responses = survey.responses

    return render_template('view_responses.html', survey=survey, questions=questions, responses=responses)

app.route('/survey/<int:survey_id>/results')
@login_required
def view_survey_results(survey_id):
    survey = Survey.query.get_or_404(survey_id)
    questions = survey.questions
    responses = survey.responses

    # Create a dictionary to store response counts for each question choice
    summary = {question.id: {choice.id: 0 for choice in question.choices} for question in questions}

    # Count the responses for each question choice
    for response in responses:
        if response.answers:
            for answer in response.answers:
                if answer.choice_id:
                    summary[answer.question_id][answer.choice_id] += 1
                elif answer.answer_text:  # Check if there's a text response
                    summary[answer.question_id]['text_response'] = summary[answer.question_id].get('text_response', 0) + 1

    return render_template('survey_results.html', survey=survey, questions=questions, summary=summary)

@app.route('/')
def index():
    surveys = Survey.query.all()
    return render_template('index.html', surveys=surveys)




if __name__ == "__main__":
    app.run(debug=True)

