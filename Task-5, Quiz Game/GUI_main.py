# Codsoft Task-5
# ______________

import tkinter as tk
from tkinter import messagebox

quiz_questions = [
    {"question": "Who is the father of computer?", "options": ["A. Newton", "B. Charles", "C. Graham"], "correct_answer": "B"},
    {"question": "Which is the parent company of Google?", "options": ["A. Google IO", "B. Google old", "C. Alphabet Inc"], "correct_answer": "C"},
    {"question": "What is the largest planet in our solar system?", "options": ["A. Earth", "B. Mars", "C. Jupiter"], "correct_answer": "C"},
    {"question": "Where is the longest bridge located?", "options": ["A. China", "B. Indonesia", "C. South Africa"], "correct_answer": "A"},
    {"question": "Which is the longest river in the world?", "options": ["A. Amazon", "B. Nile", "C. Brahamputra"], "correct_answer": "B"},
    {"question": "Which country has the higheest population density in the world?", "options": ["A. Monaco", "B. Singapore", "C. Macau"], "correct_answer": "C"},
    {"question": "Which is the tallest building in the world?", "options": ["A. Burj khalifa", "B. Eiffel Tower", "C. Sanghai Tower"], "correct_answer": "A"},
    {"question": "Which is the largest salt water lake in the world?", "options": ["A. Lake Urmia", "B. Sambhar Lake", "C. Caspian Sea"], "correct_answer": "C"},
    {"question": "Which is the hottest inhabited place in the world?", "options": ["A. Dallol-Ethopia", "B. Bangkok-Thailand", "C. Lut Desert-Iran"], "correct_answer": "A"},
    {"question": "Which airport is located at the highest altitude?", "options": ["A. Leh Airport-India", "B. Daoching Yading Airport-China", "C. Bangda Airport-Tibet"], "correct_answer": "B"}
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.score = 0
        self.current_question = 0
        self.total_questions = len(quiz_questions)
        
        self.question_label = tk.Label(root, text="", font=("Arial", 14))
        self.question_label.pack(pady=10)
        
        self.option_buttons = []
        for i in range(3):
            button = tk.Button(root, text="", font=("Arial", 12), command=lambda i=i: self.check_answer(i))
            button.pack(pady=5)
            self.option_buttons.append(button)
        
        self.next_question_button = tk.Button(root, text="Next", font=("Arial", 12), state=tk.DISABLED, command=self.next_ques)
        self.next_question_button.pack(pady=10)
        
        self.display_ques()
    
    def display_ques(self):
        if self.current_question < self.total_questions:
            question_data = quiz_questions[self.current_question]
            self.question_label.config(text=question_data["question"])
            for i in range(3):
                self.option_buttons[i].config(text=question_data["options"][i])
            self.next_question_button.config(state=tk.DISABLED)
        else:
            self.show_result()
    
    def check_answer(self, selected_option):
        question_data = quiz_questions[self.current_question]
        if question_data["correct_answer"] == chr(ord('A') + selected_option):
            self.score += 1
        self.current_question += 1
        for button in self.option_buttons:
            button.config(state=tk.DISABLED)
        self.next_question_button.config(state=tk.NORMAL)
    
    def next_ques(self):
        for button in self.option_buttons:
            button.config(state=tk.NORMAL)
        if self.current_question < self.total_questions:
            self.display_ques()
        else:
            self.result()
    
    def result(self):
        percentage = (self.score / self.total_questions) * 100
        result_message = f"You answered {self.score} out of {self.total_questions} questions correctly.\nYour score: {round(percentage)}%"
        
        play_again = messagebox.askyesno("Quiz Result", result_message + "\n\nDo you want to play again?")
        if play_again:
            self.play_again()
        else:
            self.root.quit()
    
    def play_again(self):
        self.score = 0
        self.current_question = 0
        self.display_ques()

def main():
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()