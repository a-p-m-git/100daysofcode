from question_model import Question
from quiz_brain import QuizBrain
from data import question_data,question_data_otdb

questionBank = []

for dict in question_data_otdb:
    #questionBank.append(Question(dict['text'],dict['answer']))
    questionBank.append(Question(dict['question'],dict['correct_answer']))

quiz = QuizBrain(questionBank)

print(len(questionBank))

while quiz.still_has_questions():
    quiz.next_question()
    
print("Congrats! You've completed the quiz.")
print(f"Your final score was {quiz.player_score}/{quiz.question_number + 1}")