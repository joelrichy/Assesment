# code to import questions from external file
# 16/5/22

class Questions:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer



def generate_students():
    import csv
    with open('Days of the week.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter='|')
        print("hello")
        for line in filereader:
            print("Question: {}".format(line[1]))
            print("Answer: {}".format(line[2]))


generate_students()
