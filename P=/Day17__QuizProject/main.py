from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    question_model = Question(question_text, question_answer)
    question_bank.append(question_model)
 
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():   
    quiz.next_question()
