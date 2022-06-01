from tkinter import *


class Questions:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer
        question_list.append(self)

    def display_info(self):
        print("Question: ", self.question)
        print("Options: ", self.options)
        print("Answer: ", self.answer)


def print_question():
    for question in question_list:
        question.display_info()


question_list = []

question1 = Questions("What is Monday in Maori", ["Rātū", "Rāhina", "Rāmere", "Rātapu"], "Rāhina")
question2 = Questions("What is Tuesday in Maori", ["Rātū", "Rātapu", "Rāpare", "Rāhina"],"Rātū")
question3 = Questions("What is Wednesday in Maori",["Rātū", "Rātapu", "Rāpare", "Rāhina"], "Rāapa")
question4 = Questions("What is Thursday in Maori",["Rātū", "Rātapu", "Rāpare", "Rāhina"], "Rāpare")
question5 = Questions("What is Friday in Maori",["Rātū", "Rātapu", "Rāpare", "Rāhina"], "Rāmere")
question6 = Questions("What is Saturday in Maori",["Rātū", "Rātapu", "Rāpare", "Rāhina"], "Rāhoroi")
question7 = Questions("What is Sunday in Maori",["Rātū", "Rātapu", "Rāpare", "Rāhina"], "Rātapu")

print_question()



# main routine
#if __name__ == "__main__":
    #root = Tk()
    #root.title("Questions")
   # something = Questions(root)
   # root.mainloop()