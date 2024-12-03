import tkinter as tk
from tkinter import messagebox


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("500x400")
        self.current_question = 0
        self.current_quiz = None
        self.scores = {}

        self.main_menu()

    def main_menu(self):
        self.clear_window()
        tk.Label(self.root, text="Choose a Quiz!", font=("Calibri", 18)).pack(pady=20)

        tk.Button(self.root, text="Star Wars Personality Quiz", command=self.start_personality_quiz, width=30).pack(pady=10)
        tk.Button(self.root, text="Lord of The Rings Character Quiz", command=self.start_lotr_quiz, width=30).pack(pady=10)

    def start_personality_quiz(self):
        self.start_quiz("Star Wars Personality Quiz", [
            {
                "question": "Those pesky womp rats are eating all your funky space cabbage again! How do you deal with these vermin?",
                "choices": {
                    "A": "Pay a buddy of yours to take care of them for you.",
                    "B": "Finally put that blaster of yours to good use.",
                    "C": "Push them far far away with the force.",
                    "D": "Crush them with all of your anger. DO IT.",
                },
            },
            {
                "question": "What's your ideal vacation?",
                "choices": {
                    "A": "Exploring ancient ruins and diving shipwrecks.",
                    "B": "In a bustling metropolis with plenty of things to do and see.",
                    "C": "At a cottage in the wilderness, a good distance away from your problems.",
                    "D": "Climbing up the fiery molten crags of a volcano. Feel the burn!",
                },
            },
            {
                "question": "A powerful individual has offered you a place at his side, and all you have to do is abandon all morals and ethics! What do you do?",
                "choices": {
                    "A": "Every man for himself! You don't want that responsibility.",
                    "B": "Organize your local community against him.",
                    "C": "Live a life outside the grid, trying your best to escape the system.",
                    "D": "Finally, power! Nothing else matters, time to rule.",
                },
            },
            {
                "question": "What gets you out of bed in the morning?",
                "choices": {
                    "A": "All the MONEY I'm about to make. Woohoo!",
                    "B": "There are people who care about me, and I'm doing my best to make a difference.",
                    "C": "I'm about to make the absolutely best breakfast ever imagined.",
                    "D": "I exist to spite my enemies, and I just got a new idea to cause them pain.",
                },
            },
        ], {
            "A": "You are Han Solo! Charismatic and always ready for an adventure.",
            "B": "You are Princess Leia! A leader with a strong sense of justice.",
            "C": "You are Yoda! Wise and calm in challenging situations.",
            "D": "You are Darth Vader! Driven by power and ambition.",
        })

    def start_lotr_quiz(self):
        self.start_quiz("Lord of The Rings Character Quiz", [
            {
                "question": "Dinner time! What are you cooking up for dinner?",
                "choices": {
                    "A": "Ordering delivery, no way I'm making food myself.",
                    "B": "A complicated and involved recipe, but one you know well and have perfected.",
                    "C": "Carb-heavy, fattening deliciousness.",
                    "D": "What's a meal? It's snack time!",
                },
            },
            {
                "question": "Time to go to work! Where are you going again?",
                "choices": {
                    "A": "Military :)",
                    "B": "I'm homeless, jobless, but so cool B)",
                    "C": "Oh me? I'm a farmer.",
                    "D": "Retired, I'm chilling in my crib as per usual.",
                },
            },
            {
                "question": "Time for exercise! What are we focusing on today?",
                "choices": {
                    "A": "Cardio all the way.",
                    "B": "Yoga and stretches.",
                    "C": "I don't exercise, I need that time to eat more food :D",
                    "D": "Core exercises, gotta get those rock-hard abs.",
                },
            },
            {
                "question": "Finally, you can relax after a long day. What music are you listening to?",
                "choices": {
                    "A": "Taiko arrangements.",
                    "B": "I'm singing karaoke by myself!",
                    "C": "Folk music with lots of fiddle solos.",
                    "D": "Hungarian throat singing.",
                },
            },
        ], {
            "A": "You are Aragorn! Athletic and determined.",
            "B": "You are Gandalf! Independent and wise.",
            "C": "You are Bilbo Baggins! Empathetic and an excellent host.",
            "D": "You are Treebeard! Wise and deeply rooted in tradition.",
        })

    def start_quiz(self, title, questions, descriptions):
        self.clear_window()
        self.current_quiz = {"title": title, "questions": questions, "descriptions": descriptions}
        self.scores = {key: 0 for key in descriptions.keys()}
        self.current_question = 0
        self.show_question()

    def show_question(self):
        question_data = self.current_quiz["questions"][self.current_question]
        self.clear_window()
        tk.Label(self.root, text=self.current_quiz["title"], font=("Calibri", 18)).pack(pady=10)
        tk.Label(self.root, text=question_data["question"], wraplength=400, font=("Calibri", 14)).pack(pady=10)

        for key, value in question_data["choices"].items():
            tk.Button(self.root, text=f"{key}: {value}", command=lambda k=key: self.record_answer(k), wraplength=400).pack(pady=5)

    def record_answer(self, choice):
        self.scores[choice] += 1
        self.current_question += 1
        if self.current_question < len(self.current_quiz["questions"]):
            self.show_question()
        else:
            self.show_results()

    def show_results(self):
        max_score = max(self.scores.values())
        result = [key for key, value in self.scores.items() if value == max_score][0]
        description = self.current_quiz["descriptions"][result]

        self.clear_window()
        tk.Label(self.root, text="Quiz Results", font=("Calibri", 18)).pack(pady=10)
        tk.Label(self.root, text=description, font=("Calibri", 14), wraplength=400).pack(pady=20)

        tk.Button(self.root, text="Return to Main Menu", command=self.main_menu).pack(pady=10)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
