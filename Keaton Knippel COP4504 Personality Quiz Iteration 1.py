def personality_quiz():    
    print("This is a personality quiz! You're about to learn a lot about yourself ;D")
    print("Which Star Wars Character are you?.\n")
    
    personalities = {
        "A": 0,  # Han Solo
        "B": 0,  # Princes Leia
        "C": 0,  # Yoda
        "D": 0,  # Darth Vader
    }

    questions = [
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
                "B": "In a bulstling metropolis with plenty of things to do and see.",
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
    ]

    take_quiz(questions, personalities)


def lotr_quiz():
    print("You've chosen the Lord of The Rings Quiz")
    print("Answer the following questions to find out which Lord of the Rings Character you are most like\n")

    careers = {
        "A": 0,  # Aragorn
        "B": 0,  # Gandalf
        "C": 0,  # Bilbo Baggins
        "D": 0,  # Treebeard
    }

    questions = [
        {
            "question": "Dinner time! What are you cooking up for dinner?",
            "choices": {
                "A": "Ordering delivery, no way im making food myself.",
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
            "question": "Time for excercise! What are we focusing on today?",
            "choices": {
                "A": "Cardio all the way.",
                "B": "Yoga and stretches.",
                "C": "I don't excercise, I need that time to eat more food :D",
                "D": "Core excercises, gotta get those rock hard abs.",
            },
        },
        {
            "question": "Finally, you can relax after a long day. What music are you listening to?",
            "choices": {
                "A": "Taiko arrangements.",
                "B": "I'm singing karaoke by myself!",
                "C": "Folk music with lots of fiddle solos",
                "D": "Hungarian throat singing.",
            },
        },
    ]

    take_quiz(questions, careers)


def take_quiz(questions, categories):
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        for key, value in q["choices"].items():
            print(f"{key}: {value}")
        while True:
            answer = input("Choose A, B, C, or D: ").strip().upper()
            if answer in categories:
                categories[answer] += 1
                break
            print("Invalid choice. Please select A, B, C, or D.")

    # Determine the type with the highest score
    max_category = max(categories, key=categories.get)

    descriptions = {
        "A": "You are Aragorn! Athletic, and determined in some way or another.",
        "B": "You are Gandalf! Very independent and wise.",
        "C": "You are Bilbo! An excellent host, and empathetic towards others.",
        "D": "You are Treebeard! You got the tree guy somehow, but at least you're similar to someone.",
    }

    print("\nYour Results!")
    print(descriptions[max_category])

    # Show scores
    print("\nScores by category:")
    for category, score in categories.items():
        print(f"{category}: {score}")


def main():
    print("We've got a few quizzes to choose from! Check them out below.")
    print("Choose one of the following quizzes:")
    print("1. Star Wars Personality Quiz")
    print("2. Lord of The Rings Character Quiz")

    while True:
        choice = input("Enter 1 or 2: ").strip()
        if choice == "1":
            personality_quiz()
            break
        elif choice == "2":
            lotr_quiz()
            break
        else:
            print("Invalid choice. Please select 1 or 2.")

    print("\nThank you so much for taking the quiz!")


if __name__ == "__main__":
    main()