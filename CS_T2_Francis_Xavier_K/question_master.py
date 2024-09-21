import csv

def add_question():
    question = input("Enter the question: ")
    option1 = input("Enter option 1: ")
    option2 = input("Enter option 2: ")
    option3 = input("Enter option 3: ")
    option4 = input("Enter option 4: ")
    correct_option = input("Enter the correct option (op1/op2/op3/op4): ")
    
    with open('questions.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([None, question, option1, option2, option3, option4, correct_option])

def display_questions():
    with open('questions.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

if __name__ == '__main__':
    while True:
        print("1. Add a question")
        print("2. Display all questions")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_question()
        elif choice == '2':
            display_questions()
        else:
            break
