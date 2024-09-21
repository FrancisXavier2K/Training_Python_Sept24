import csv
from datetime import datetime

# Load questions from CSV file
def load_questions():
    questions = []
    with open('questions.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            questions.append(row)
    return questions

# Function to save participant's score to leaderboard.csv
def save_score(name, university, score):
    with open('leaderboard.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, university, score, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])

# Main function to conduct the exam
def conduct_exam():
    # Gather participant details
    name = input("Enter your name: ")
    university = input("Enter your university: ")

    # Load questions
    questions = load_questions()

    # Initialize score
    score = 0

    # Loop through each question
    for i, question in enumerate(questions):
        print(f"\nQuestion {i+1}: {question['question']}")
        print(f"1) {question['option1']}")
        print(f"2) {question['option2']}")
        print(f"3) {question['option3']}")
        print(f"4) {question['option4']}")
        answer = input("Enter your choice (1/2/3/4): ")

        # Check if the answer is correct
        correct_answer = question['correctoption'][-1]  # Get the number from 'op1', 'op2', etc.
        if answer == correct_answer:
            score += 1

    # Display final score
    print(f"\n{name}, you scored {score} out of {len(questions)}.\n")

    # Save the score to leaderboard
    save_score(name, university, score)

if __name__ == '__main__':
    conduct_exam()
