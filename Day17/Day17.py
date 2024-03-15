import warnings

from question_model import Question
from quiz_master import QuizMaster
from trivia_quiz_art import trivia_quiz_logo
from trivia_quiz_data import trivia_quiz_data

with warnings.catch_warnings():
    warnings.simplefilter('ignore', SyntaxWarning)
    warnings.warn('bad', SyntaxWarning)

print("Day 17 - 100 Days of Code.")
print("Welcome to Trivia Quiz.")
print(trivia_quiz_logo)

question_bank = []
for question in trivia_quiz_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizMaster(question_bank)

while quiz.are_there_more_questions():
    quiz.display_next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.trivia_score}/{quiz.question_number}")
