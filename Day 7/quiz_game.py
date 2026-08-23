# Day 7: putting it together - a simple quiz game

questions = {
    "What does 'len()' do in Python?": "returns length",
    "What symbol starts a comment in Python?": "#",
    "What keyword defines a function?": "def"
}

score = 0
for question, answer in questions.items():
    user_answer = input(f"{question} ").strip().lower()
    if user_answer == answer.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Nope, the answer was: {answer}")

print(f"\nFinal score: {score}/{len(questions)}")