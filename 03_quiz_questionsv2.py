# code to import questions from external file
# 16/5/22

def generate_students():
    import csv
    questions = []
    answers = []
    with open('Days of the week.csv', 'r') as csvfile:
        filereader = csv.DictReader(csvfile)
        for line in filereader:
            questions.append(line['\ufeffQuestion'])
            answers.append(line['Answer'])
        print(questions)
        print(answers)


generate_students()
