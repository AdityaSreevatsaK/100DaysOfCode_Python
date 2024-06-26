from html import unescape


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        """
            Method to check if there are more questions remaining.
        """
        return self.question_number < len(self.question_list)

    def next_question(self) -> str | None:
        """
            Method to get the next question.
            Returns question string when there are more questions. Else, returns None.
        """
        if not self.still_has_questions():
            return None

        self.current_question = self.question_list[self.question_number]
        self.question_number += 1

        # Unescape function from the html package helps convert the named and numeric character references.
        # in the string to the corresponding unicode characters.
        return f"Q.{self.question_number}: {unescape(self.current_question.text)} (True/False):"

    def check_answer(self, user_answer: str) -> bool:
        """
            Method to check and return if user has selected the right answer.
        """
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
