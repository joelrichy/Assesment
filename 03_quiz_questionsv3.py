# Trial 2 of 03_quiz_questions
# test to see if using a class system is better than importing questions from Csv


class Questions:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        question_list.append(self)

    def display_info(self):
        print("Question: ", self.question)
        print("Answer: ", self.answer)


def print_question():
    for question in question_list:
        question.display_info()


question_list = []

question1 = Questions("1", "2")
question2 = Questions("3", "4")
question3 = Questions("5", "6")
question4 = Questions("7", "8")
question5 = Questions("9", "10")


print_question()



# main routine
#if __name__ == "__main__":
    #root = Tk()
    #root.title("Questions")
   # something = Questions(root)
   # root.mainloop()