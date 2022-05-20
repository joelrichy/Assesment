# code to import questions from external file
# 16/5/22

class Questions:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer



def generate_students():
    import csv
    questions = []
    answers = []
    with open('Days of the week.csv', 'r') as csvfile:
        filereader = csv.DictReader(csvfile)
        for line in filereader:
            print(line)
            questions.append(line['\ufeffQuestion'])
            answers.append(line['Answer'])




    generate_students()
