def run_quiz():

    quiz_data = [
        {
            "question": "Which is the capital of Telangana?",
            "options": ["Hyderabad", "Chennai"],
            "answer": "Hyderabad"
        },

        {
            "question": "Which is the capital of India?",
            "options": ["Delhi", "Hyderabad"],
            "answer": "Delhi"
        }
    ]

    score = 0

    print("Welcome to the Quiz Game!")

    for q in quiz_data:

        print("\n" + q["question"])

        for option in q["options"]:
            print("-", option)

        user_answer = input("Enter your answer: ")

        if user_answer.lower() == q["answer"].lower():
            print("Correct Answer!")
            score += 1
        else:
            print("Wrong Answer!")
            print("Correct Answer is:", q["answer"])

    print("\nQuiz Completed!")
    print("Your Score:", score, "/", len(quiz_data))


run_quiz()