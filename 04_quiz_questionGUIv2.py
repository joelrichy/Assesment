from tkinter import *


class Questions:
    def __init__(self, question, option1, option2, option3, option4, answer):
        self.question = question
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.option4 = option4
        self.answer = answer
        question_list.append(self)

        #self.ques = self.question(self.qn)

        # formatting variables
        background_colour = "white"


        # converter frame
        self.question_frame = Frame(width=300, bg=background_colour, pady=10)
        self.question_frame.grid()

        # tempurature Converter heading (row 0)
        self.question_label = Label(self.question_frame,
                                        text=self.question,
                                        font="Arial 16 bold",
                                        bg=background_colour,
                                        padx=10, pady=10)
        self.question_label.grid(row=0)

        # conversion buttons frame (row 3)
        self.answer_frame = Frame(self.question_frame)
        self.answer_frame.grid(row=3, pady=10)

        # answer button 1
        self.answer_button1 = Button(self.answer_frame,
                                     text=self.option1, font="Arial 10 bold",
                                     bg="red", padx=15, pady=15)
        self.answer_button1.grid(row=0, column=0)

        # answer button 2
        self.answer_button2 = Button(self.answer_frame,
                                  text=self.option2, font="Arial 10 bold",
                                  bg="red", padx=15, pady=15)
        self.answer_button2.grid(row=0, column=1)
        # answer button 3
        self.answer_button3 = Button(self.answer_frame,
                                  text=self.option3, font="Arial 10 bold",
                                  bg="red", padx=15, pady=15)
        self.answer_button3.grid(row=1, column=0)

        # answer button 4
        self.answer_button4 = Button(self.answer_frame,
                                  text=self.option4, font="Arial 10 bold",
                                  bg="red", padx=15, pady=15)
        self.answer_button4.grid(row=1, column=1)

        global question_num
        question_num += 1

question_list = []

# main routine
global question_num
question_num = 1

if __name__ == "__main__":
    root = Tk()
    root.title("Pataitai")
    if question_num == 1:
        question1 = Questions("What is Monday in Maori", "R??t??", "R??hina", "R??mere", "R??tapu", "R??hina")
    elif question_num == 2:
        question2 = Questions("What is Tuesday in Maori", "R??t??", "R??tapu", "R??pare", "R??hina", "R??t??")
    elif question_num == 3:
        question3 = Questions("What is Wednesday in Maori", "R??hina", "R??tapu", "R??apa", "Ratapu", "R??apa")
    elif question_num == 4:
        question4 = Questions("What is Thursday in Maori", "R??mere", "R??horoi", "R??pare", "R??hina", "R??pare")
    elif question_num == 5:
        question5 = Questions("What is Friday in Maori", "R??hina", "R??mere", "R??pare", "R??tu", "R??mere")
    elif question_num == 6:
        question6 = Questions("What is Saturday in Maori", "R??t??", "R??tapu", "R??apa", "R??horoi", "R??horoi")
    elif question_num == 7:
        question7 = Questions("What is Sunday in Maori", "R??tapu", "R??horoi", "R??pare", "R??hina", "R??tapu")

    root.mainloop()
