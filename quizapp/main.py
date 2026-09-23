import random
questions = [
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    },
    {
        "question": "What is 5 + 3?",
        "options": ["6", "7", "8", "9"],
        "answer": "8"
    },
    {
        "question": "What is 10 - 4?",
        "options": ["4", "5", "6", "7"],
        "answer": "6"
    },
    {
        "question": "What is 3 × 4?",
        "options": ["7", "10", "12", "14"],
        "answer": "12"
    },
    {
        "question": "What is 20 ÷ 5?",
        "options": ["2", "4", "5", "10"],
        "answer": "4"
    }
]

random.shuffle(questions)

def game(question):
    if not question:
        print("no question available come back next time")
    else:

        score = 0
        letters = ["A", "B", "C", "D"]

        for qst in questions:
            print(qst["question"])

            for i,option in enumerate(qst["options"]):
                print(f"{letters[i]}.{option}")

            answer = input("Choose A, B, C, or D: ").upper().strip()

            if answer == "":
                continue
            elif answer == "EXIT":
                exit()

            while answer not in letters :
                print("Invalid option. Please choose A, B, C, or D.")
                answer = input("Choose A, B, C, or D: ").upper().strip()
                if answer == "EXIT":
                    exit()

            selected_option = qst["options"][letters.index(answer)]
            if answer == "":
                continue

            if selected_option == qst["answer"]:
                print("correct")
                score+=1
            else:
                print(f"Wrong! The correct answer is {qst['answer']}.")

        print(score)


def start():
    user_res = input("do you want to start y/n").lower().strip()
    if user_res == "y":
        game(questions)
    else:
        exit()
start()
