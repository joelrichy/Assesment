# code to import questions from external file
# 16/5/22

def generate_students():
    import csv
    with open('Days of the week.csv', 'r') as csvfile:
        filereader = csv.reader(csvfile)
        for line in filereader:
            print(line)

generate_students()
