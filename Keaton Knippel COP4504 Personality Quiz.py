def personality_quiz():
    print("This is a personality quiz! You're about to learn a lot about yourself ;D")
    print("Which Star Wars Character are you?.\n")

    # personality categories
    personalities = {
        "A": 0,  # Han Solo
        "B": 0,  # Princes Leia
        "C": 0,  # Yoda
        "D": 0,  # Darth Vader
    }

    # all of the questions and choices written out
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

    # quiz loop
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        for key, value in q["choices"].items():
            print(f"{key}: {value}")
        while True:
            answer = input("Choose A, B, C, or D: ").strip().upper()
            if answer in personalities:
                personalities[answer] += 1
                break
            print("Invalid choice. Please select A, B, C, or D.")

    # chooses the personality type that has the highest score
    max_personality = max(personalities, key=personalities.get)
    personality_descriptions = {
        "A": "You are Han Solo. Strong and Independent, if not a bit stubborn.",
        "B": "You are Princess Leia! A natural born leader who cares deeply about those around them.",
        "C": "You are Yoda! Calm, methodical, and perhaps a bit of a hermit.",
        "D": "You are Darth Vader! Comically evil, you likely have unresolved childhood trauma.",
    }

    print("\nYour Results!")
    print(personality_descriptions[max_personality])

    # Show scores
    print("\nScores by category:")
    for category, score in personalities.items():
        print(f"{category}: {score}")

if __name__ == "__main__":
    personality_quiz()
