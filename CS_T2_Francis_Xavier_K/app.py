from flask import Flask, render_template, request, redirect, url_for
import csv
from datetime import datetime

app = Flask(__name__)

# Load questions from CSV file
def load_questions():
    questions = []
    with open('questions.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            questions.append(row)
    return questions

# Save participant's score to leaderboard.csv
def save_score(name, university, score):
    with open('leaderboard.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, university, score, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])

# Load leaderboard data from CSV
def load_leaderboard():
    leaderboard = []
    with open('leaderboard.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            leaderboard.append(row)
    return leaderboard

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Exam route
@app.route('/exam', methods=['GET', 'POST'])
def exam():
    questions = load_questions()  # Load questions from the CSV file
    if request.method == 'POST':
        name = request.form['name']
        university = request.form['university']
        score = 0

        # Evaluate the submitted answers
        for i, question in enumerate(questions):
            selected = request.form.get(f'question_{i}')
            correct_answer = question['correctoption'][-1]  # Get the correct option number
            if selected == correct_answer:
                score += 1
        
        # Save the score
        save_score(name, university, score)
        return redirect(url_for('result', score=score))  # Redirect to result page

    # Render the exam page with questions
    return render_template('exam.html', questions=questions)

# Result route
@app.route('/result/<int:score>')
def result(score):
    return render_template('result.html', score=score)

# Leaderboard route
@app.route('/leaderboard')
def leaderboard():
    leaderboard_data = load_leaderboard()
    return render_template('leaderboard.html', data=leaderboard_data)

if __name__ == '__main__':
    app.run(debug=True)
