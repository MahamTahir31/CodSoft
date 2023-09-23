# Codsoft Task-5
# ______________

import random

# Define a list of quiz questions and answers
# ___________________________________________
quiz_questions = [
    {"question": "Who is the father of computer?", "options": ["A. Newton", "B. Charles", "C. Graham"], "correct_answer": "B"},
    {"question": "Which is the parent company of google?", "options": ["A. Google IO", "B. Google old", "C. Alphabet Inc"], "correct_answer": "C"},
    {"question": "What is the largest planet in our solar system?", "options": ["A. Earth", "B. Mars", "C. Jupiter"], "correct_answer": "C"},
    {"question": "Where is the longest bridge located?", "options": ["A. China", "B. Indonesia", "C. South Africa"], "correct_answer": "A"},
    {"question": "Which is the longest river in the world?", "options": ["A. Amazon", "B. Nile", "C. Brahamputra"], "correct_answer": "B"},
    {"question": "Which country has the higheest population density in the world?", "options": ["A. Monaco", "B. Singapore", "C. Macau"], "correct_answer": "C"},
    {"question": "Which is the tallest building in the world?", "options": ["A. Burj khalifa", "B. Eiffel Tower", "C. Sanghai Tower"], "correct_answer": "A"},
    {"question": "Which is the largest salt water lake in the world?", "options": ["A. Lake Urmia", "B. Sambhar Lake", "C. Caspian Sea"], "correct_answer": "C"},
    {"question": "Which is the hottest inhabited place in the world?", "options": ["A. Dallol-Ethopia", "B. Bangkok-Thailand", "C. Lut Desert-Iran"], "correct_answer": "A"},
    {"question": "Which airport is located at the highest altitude?", "options": ["A. Leh Airport-India", "B. Daoching Yading Airport-China", "C. Bangda Airport-Tibet"], "correct_answer": "B"}
]

def display_welcome_message():
    print("\n\t\t\t\t\t\t\t\t\t   Welcome to the Quiz Game!\n\t\t\t\t\t\t\t\t\t===============================")
    print("\n\t\t\t\t\t\tYou will be asked a series of questions. Try to get as many correct answers as possible.")
    print("\n\t\t\t\t\t\t\t\t\t      Let's get started!\n\t\t\t\t\t\t\t\t\t===============================")

def present_questions(questions):
    score = 0
    for question in questions:
        print(question["question"])
        for option in question["options"]:
            print(option)
        user = input("Select the correct option (A, B, or C): ").upper()
        if user == question["correct_answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Sorry, the correct answer is {question['correct_answer']}\n")

    return score

def display_result(score, total_questions):
    print(f"You answered {score} out of {total_questions} questions correctly.\n")
    percentage = (score / total_questions) * 100
    print(f"*** Your score: {round(percentage)}% ***")

def play_again():
    return input("\n\t\t\t\t\t\t\t\t    Do you want to play again? (yes/no): ").lower() == "yes"

# Main Program
# ____________

def main():
    display_welcome_message()
    total_questions = len(quiz_questions)
    
    while True:
        random.shuffle(quiz_questions)  # Shuffle questions for variety
        score = present_questions(quiz_questions)
        display_result(score, total_questions)
        
        if not play_again():
            print("\n\t\t\t\t\t\t\t\t\t      Thanks for playing!\n\t\t\t\t\t\t\t\t\t==============================\n")
            break

if __name__ == "__main__":
    main()
