class QuizBrain:
    def __init__(self,questionList) -> None:
        self.question_number = 0
        self.player_score = 0
        self.questionList = questionList

    def still_has_questions(self):
        return self.question_number < len(self.questionList) - 1
        """  if self.question_number < len(self.questionList) - 1:
            return True
        else:
            return False """
        
        
    def next_question(self):
        self.question_number +=1

        answer = input(f"Q{self.question_number}: {self.questionList[self.question_number].text}. (True/False)?: ").lower()
        self.check_answer(answer,self.questionList[self.question_number].answer)
        
    def check_answer(self,answer,qanswer):
        if answer.lower() == qanswer.lower():
            self.player_score +=1
            print("You got it right!")
        else:
            print("You got it wrong!")
        
        print(f"The correct answer is: {qanswer}")
        print(f"Your Current Score is {self.player_score}/{self.question_number}\n\n")
        