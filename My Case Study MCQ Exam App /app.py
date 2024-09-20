from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

QUESTIONS_FILE = 'questions.csv'
LEADERBOARD_FILE = 'leaderboard.csv'


# Load questions from CSV
def load_questions():
    questions = []
    with open(QUESTIONS_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            questions.append(row)
    return questions


# Save participant's score to leaderboard CSV
def save_score(name, university, score):
    with open(LEADERBOARD_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, university, score])


# Route for homepage (starting the quiz)
@app.route('/', methods=['GET', 'POST'])
def exam():
    if request.method == 'POST':
        name = request.form['name']
        university = request.form['university']

        questions = load_questions()
        user_answers = []
        for question in questions:
            answer = request.form.get(f'question_{question["num"]}', '')
            user_answers.append(answer)

        # Calculate score
        score = 0
        for i, question in enumerate(questions):
            if user_answers[i] == question['correctoption'][-1]:
                score += 1

        save_score(name, university, score)
        return redirect(url_for('result', name=name, university=university, score=score))

    questions = load_questions()
    return render_template('exam.html', questions=questions)


# Route for displaying the result after the exam
@app.route('/result')
def result():
    name = request.args.get('name')
    university = request.args.get('university')
    score = request.args.get('score')
    return render_template('result.html', name=name, university=university, score=score)


# Route for displaying the leaderboard
@app.route('/leaderboard')
def leaderboard():
    try:
        with open(LEADERBOARD_FILE, mode='r') as file:
            reader = csv.reader(file)
            leaderboard = sorted(reader, key=lambda row: int(row[2]), reverse=True)[:5]
    except FileNotFoundError:
        leaderboard = []

    return render_template('leaderboard.html', leaderboard=leaderboard)


if __name__ == '__main__':
    app.run(debug=True)
