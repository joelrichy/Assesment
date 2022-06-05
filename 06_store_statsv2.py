class Questions:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        self.question_list = []
        self.question_list.append(question)
        self.correct = 0
        self.questions_asked = 0

    def ask_questions(self):
        for question in self.question_list:
            question = input(self.question)
            if question == self.answer:
                print("correct")
                self.correct += 1
                self.questions_asked += 1
            else:
                print("incorrect")
                self.questions_asked += 1

def quiz(self):
    while self.questions_asked != 7:
        self.ask_questions()

    print(self.correct)



question1 = Questions("What is Monday in Maori", "Rāhina")
question2 = Questions("What is Tuesday in Maori", "Rātū")
question3 = Questions("What is Wednesday in Maori", "Rāapa")
question4 = Questions("What is Thursday in Maori", "Rāpare")
question5 = Questions("What is Friday in Maori", "Rāmere")
question6 = Questions("What is Saturday in Maori", "Rāhoroi")
question7 = Questions("What is Sunday in Maori", "Rātapu")




