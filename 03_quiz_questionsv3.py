
class Questions:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        questions.append(self)

    def display_info(self):
        print("Question: ", self.question)
        print("Answer: ", self.answer)


def print_question():
    for question in questions:
        question.display_info()


def generate_questions():
    import csv
    with open('Days of the week.csv', 'r') as csvfile:
        filereader = csv.DictReader(csvfile)
        for line in filereader:
            Questions(line['\ufeffQuestion'], line['Answer'])
            #questions.append(line['\ufeffQuestion'])
            #answers.append(line['Answer'])
        #print(questions)
        #print(answers)


questions = []
answers = []






# main routine
#if __name__ == "__main__":
    #root = Tk()
    #root.title("Questions")
   # something = Questions(root)
   # root.mainloop()