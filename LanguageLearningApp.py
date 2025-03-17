class LanguageLearningApp:
    def __init__(self, user_name):
        self.user_name = user_name
        self.lessons = {
            "Lesson 1": ["apple", "banana", "orange"],
            "Lesson 2": ["dog", "cat", "bird"],
            "Lesson 3": ["house", "car", "tree"]
        }
        self.completed_lessons = []
        self.user_score = 0
        self.total_score = 0
        self.current_lesson = None

    def show_welcome_message(self):
        print(f"Welcome, {self.user_name}! Let's start learning!")

    def start_lesson(self, lesson_name):
        if lesson_name not in self.lessons:
            print(f"Lesson {lesson_name} is not available.")
            return
        self.current_lesson = lesson_name
        print(f"\nStarting {lesson_name}...")
        self.show_lesson()

    def show_lesson(self):
        words = self.lessons[self.current_lesson]
        print(f"Learn these words:")
        for word in words:
            print(f"- {word}")

    def take_quiz(self):
        if not self.current_lesson:
            print("Please start a lesson first!")
            return

        print(f"\nQuiz for {self.current_lesson}:")
        quiz_answers = self.lessons[self.current_lesson]
        correct_answers = 0

        for word in quiz_answers:
            user_answer = input(f"What's the translation for '{word}'? ").strip().lower()
            if user_answer == word:
                correct_answers += 1
                print("Correct!")
            else:
                print(f"Wrong! The correct word is '{word}'.")

        self.update_score(correct_answers)
        self.show_progress()

    def update_score(self, correct_answers):
        self.user_score += correct_answers
        self.total_score += len(self.lessons[self.current_lesson])
        self.completed_lessons.append(self.current_lesson)

    def show_progress(self):
        print(f"\nYou got {self.user_score}/{self.total_score} answers correct!")
        print(f"Completed Lessons: {', '.join(self.completed_lessons)}")
        print(f"Your current score: {self.user_score} out of {self.total_score}.")

    def show_achievements(self):
        print("\nYour achievements:")
        if len(self.completed_lessons) > 0:
            print(f"Completed {len(self.completed_lessons)} lessons!")
        if self.user_score >= 3:
            print("Achievement Unlocked: Vocabulary Master!")
        if self.user_score >= 5:
            print("Achievement Unlocked: Grammar Genius!")


# Usage
def main():
    user_name = input("Enter your name: ")
    app = LanguageLearningApp(user_name)
    app.show_welcome_message()

    while True:
        print("\nAvailable Lessons:")
        for lesson in app.lessons.keys():
            print(f"- {lesson}")

        lesson_choice = input("\nChoose a lesson to start (or type 'exit' to quit): ").strip()
        
        if lesson_choice.lower() == 'exit':
            print("Goodbye! See you next time.")
            break
        
        app.start_lesson(lesson_choice)
        app.take_quiz()
        app.show_achievements()

if __name__ == "__main__":
    main()
