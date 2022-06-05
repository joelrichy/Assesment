from tkinter import *


class Questions:
    def __init__(self, question, option1, option2, option3, option4, answer):
        self.question = question
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.option4 = option4
        self.answer = answer
        self.opt_selected = StringVar()
        self.opt1_text = StringVar()
        self.opt2_text = StringVar()
        self.opt3_text = StringVar()
        self.opt4_text = StringVar()
        question_list.append(self)
        self.qn = 0
        self.correct = 0
        #self.ques = self.question(self.qn)

        # formatting variables
        background_colour = "red"
        button_colour = "red"


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
                                     bg="red", command=lambda: self.check_answer(), padx=15, pady=15)
        self.answer_button1.grid(row=0, column=0)

        # answer button 2
        self.answer_button2 = Button(self.answer_frame,
                                  text=self.option2, font="Arial 10 bold",
                                  bg="red", command=lambda: self.check_answer(), padx=15, pady=15)
        self.answer_button2.grid(row=0, column=1)
        # answer button 3
        self.answer_button3 = Button(self.answer_frame,
                                  text=self.option3, font="Arial 10 bold",
                                  bg="red", command=self.check_answer(), padx=15, pady=15)
        self.answer_button3.grid(row=1, column=0)

        # answer button 4
        self.answer_button4 = Button(self.answer_frame,
                                  text=self.option4, font="Arial 10 bold",
                                  bg="red", command=lambda: self.check_answer(), padx=15, pady=15)
        self.answer_button4.grid(row=1, column=1)

        global question_num
        question_num += 1


    def check_answer(self):
        self.opt_selected = self.answer_button1.get(), self.answer_button2.get(), self.answer_button3.get(), self.answer_button4.get()
        selected = self.opt_selected
        if selected == self.answer:
            return True


    def to_answer(self):
        while self.check_answer is True:
            correct()

        incorrect()


def correct():
    root = Tk()

    correct_frame = Frame(width=300, pady=10, bg='chartreuse')
    correct_frame.grid()

    correct_label = Label(correct_frame, text="CORRECT", font="Arial 16 bold", bg='chartreuse', padx=10, pady=10)
    correct_label.grid(sticky='')

    next_button = Button(correct_frame, text="NEXT", font="Arial 12 bold", bg='chartreuse', padx=5, pady=5)
    next_button.grid(sticky=SE)

    root.mainloop()

def incorrect():
    root = Tk()

    incorrect_frame = Frame(width=300, pady=10, bg='firebrick1')
    incorrect_frame.grid()

    incorrect_label = Label(incorrect_frame, text="INCORRECT", font="Arial 16 bold", bg='firebrick1', padx=10,
                            pady=10)
    incorrect_label.grid(sticky='')

    next_button = Button(incorrect_frame, text="NEXT", font="Arial 12 bold", bg='firebrick1', padx=5, pady=5)
    next_button.grid(sticky=SE)

    root.mainloop()


question_list = []

# main routine
global question_num
question_num = 1

if __name__ == "__main__":
    root = Tk()
    root.title("Pataitai")
    if question_num == 1:
        question1 = Questions("What is Monday in Maori", "Rātū", "Rāhina", "Rāmere", "Rātapu", "Rāhina")
    elif question_num == 2:
        question2 = Questions("What is Tuesday in Maori", "Rātū", "Rātapu", "Rāpare", "Rāhina", "Rātū")
    elif question_num == 3:
        question3 = Questions("What is Wednesday in Maori", "Rāhina", "Rātapu", "Rāapa", "Ratapu", "Rāapa")
    elif question_num == 4:
        question4 = Questions("What is Thursday in Maori", "Rāmere", "Rāhoroi", "Rāpare", "Rāhina", "Rāpare")
    elif question_num == 5:
        question5 = Questions("What is Friday in Maori", "Rāhina", "Rāmere", "Rāpare", "Rātu", "Rāmere")
    elif question_num == 6:
        question6 = Questions("What is Saturday in Maori", "Rātū", "Rātapu", "Rāapa", "Rāhoroi", "Rāhoroi")
    elif question_num == 7:
        question7 = Questions("What is Sunday in Maori", "Rātapu", "Rāhoroi", "Rāpare", "Rāhina", "Rātapu")

    root.mainloop()
