class QuizBrain():
    def __init__(self, question_list):
        self.question_number = 1
        self.question_list = question_list
        
    def next_question(self):
        current_question = self.question_list[self.question_number]
        input(f"Q.{self.question_number}: {current_question.question} (True/False) ")
        self.question_number +=1
        
    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else: 
            return False
    def answer_check(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got the answer right!")
        else:
            print("You got the answer wrong. ")
        
