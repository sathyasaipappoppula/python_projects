import threading, time, sys

# ---------------- Timed Input ---------------- #
def timed_input(prompt, timeout=10):
    """
    Ask for input with a timeout.
    Returns None if time runs out.
    """
    result = [None]

    def ask():
        try:
            result[0] = input(prompt)
        except EOFError:
            pass

    t = threading.Thread(target=ask, daemon=True)
    t.start()
    t.join(timeout)
    return result[0]

# ---------------- Question Bank ---------------- #
questions = [
    {
        "q": "What is the capital of France?",
        "choices": ["A) Paris", "B) Rome", "C) Madrid", "D) Berlin"],
        "answer": "A"
    },
    {
        "q": "The Sun is a star. (T/F)",
        "choices": [],
        "answer": "T"
    },
    {
        "q": "Which planet is known as the Red Planet?",
        "choices": ["A) Venus", "B) Jupiter", "C) Mars", "D) Mercury"],
        "answer": "C"
    },
    {
        "q": "Python lists are immutable. (T/F)",
        "choices": [],
        "answer": "F"
    },
    {
        "q": "Which language is primarily used for iOS app development?",
        "choices": ["A) Swift", "B) Kotlin", "C) Java", "D) Objective-C"],
        "answer": "A"
    },
]

# ---------------- Quiz Logic ---------------- #
score = 0
results = []

print("="*50)
print("         TIMED QUIZ APP (10s per question)      ")
print("="*50)

for i, q in enumerate(questions, 1):
    print(f"\nQ{i}. {q['q']}")
    for choice in q["choices"]:
        print(choice)

    start = time.time()
    ans = timed_input("Your answer: ", 10)  # 10 seconds each
    elapsed = time.time() - start

    correct = (ans and ans.strip().upper() == q["answer"].upper())
    if correct:
        print(f"✅ Correct! ({elapsed:.1f}s)")
        score += 1
    else:
        if ans is None:
            print("⏰ Time's up!")
        else:
            print("❌ Wrong.")
        print(f"Correct Answer: {q['answer']}")

    results.append({
        "question": q["q"],
        "given": ans,
        "correct": correct,
        "time": round(elapsed, 1)
    })

# ---------------- Summary ---------------- #
print("\n" + "="*50)
print("                QUIZ FINISHED")
print("="*50)
print(f"Score: {score}/{len(questions)} ({score/len(questions)*100:.1f}%)")
avg_time = sum(r["time"] for r in results)/len(results)
print(f"Average time per question: {avg_time:.1f}s")
print("="*50)

# Show detailed results
print("\nDetailed Results:")
for r in results:
    status = "Correct" if r["correct"] else "Wrong"
    print(f"- {r['question']} → {status} (Your answer: {r['given']}, Time: {r['time']}s)")
