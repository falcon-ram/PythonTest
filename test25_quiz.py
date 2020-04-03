from Question import Question

questions_prompt = [
    "What colour are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n==>",
    "What colour are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n==>",
    "What colour are strawberries\n(a) Yellow\n(b) Red\n(c) Blue\n\n==>"
]

questions = [
    Question(questions_prompt[0], "a"),
    Question(questions_prompt[1], "c"),
    Question(questions_prompt[2], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("Your score: " + str(score) + " out of " + str(len(questions)))

run_test(questions)