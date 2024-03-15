zero = 0
one = 1

class QuizMaster:
    def __init__(self, question_list):
        self.question_number = zero
        self.trivia_score = zero
        self.question_list = question_list

    def are_there_more_questions(self):
        """
        Description:
            Method to determine if there are more questions in the list.
        Return:
            bool: Returns true if there are more questions. Else false.
        """
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer):
        """
        Description:
            Method to check if the answer provided the user is correct.
        """
        correct_answer = self.question_list[self.question_number]
        if user_answer == correct_answer.answer.lower():
            self.trivia_score += one
            print("That is correct! 💯")
        else:
            print("Oh no. That is incorrect. 😢")
        print(f"The correct answer is {correct_answer.text}")

    def display_next_question(self):
        """
        Description:
            Method to display the question and call a method to check the answer provided by the user.
        """
        current_question = self.question_list[self.question_number]
        user_answer = input(f"{self.question_number + one} - {current_question.text} Enter 'True' or 'False'.").lower()
        self.check_answer(user_answer)
        self.question_number += one
        print(f"Current score: {self.trivia_score}/{self.question_number}")
