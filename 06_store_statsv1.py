
correct = 0
questions_asked = 0

while questions_asked != 7:
    question1 = input("What is Monday in Maori: ")
    if question1 == "Rahina":
        print("correct")
        correct += 1
        questions_asked += 1
    else:
        print("incorrect")
        questions_asked += 1

    question2 = input("What is Tuesday in Maori: ")
    if question2 == "Ratu":
        print("correct")
        correct += 1
        questions_asked += 1
    else:
        print("incorrect")
        questions_asked += 1

    question3 = input("What is Wednesday in Maori: ")
    if question3 == "Raapa":
        print("correct")
        correct += 1
        questions_asked += 1
    else:
        print("incorrect")
        questions_asked += 1

    question4 = input("What is Thursday in Maori: ")
    if question4 == "Rapare":
        print("correct")
        correct += 1
        questions_asked += 1
    else:
        print("incorrect")
        questions_asked += 1

    question5 = input("What is Friday in Maori: ")
    if question5 == "Ramare":
        print("correct")
        correct += 1
        questions_asked += 1
    else:
        print("incorrect")
        questions_asked += 1

    question6 = input("What is Saturday in Maori: ")
    if question6 == "Rahoroi":
        print("correct")
        correct += 1
        questions_asked += 1
    else:
        print("incorrect")
        questions_asked += 1

    question7 = input("What is Sunday in Maori: ")
    if question7 == "Ratapu":
        print("correct")
        correct += 1
        questions_asked += 1
    else:
        print("incorrect")
        questions_asked += 1

print("You got {}/7 correct".format(correct))