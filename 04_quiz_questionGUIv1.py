from tkinter import *
from functools import partial  # to prevent unwanted additional windows
import random


class Quiz:
    def __init__(self, parent):
        # formatting variables
        background_colour = "white"
        button_colour = "red"

        # converter frame
        self.question_frame = Frame(width=300, bg=background_colour, pady=10)
        self.question_frame.grid()

        # tempurature Converter heading (row 0)
        self.question_label = Label(self.question_frame,
                                        text="Question goes here...",
                                        font="Arial 16 bold",
                                        bg=background_colour,
                                        padx=10, pady=10)
        self.question_label.grid(row=0)

        # conversion buttons frame (row 3) orchid3 / khaki1
        self.answer_frame = Frame(self.question_frame)
        self.answer_frame.grid(row=3, pady=10)

        # answer button 1
        self.answer_button1 = Button(self.answer_frame,
                                  text="Answer 1", font="Arial 10 bold",
                                  bg="red", padx=15, pady=15)
        self.answer_button1.grid(row=0, column=0)

        # answer button 2
        self.answer_button2 = Button(self.answer_frame,
                                  text="Answer 2", font="Arial 10 bold",
                                  bg="red", padx=15, pady=15)
        self.answer_button2.grid(row=0, column=1)
        # answer button 3
        self.answer_button3 = Button(self.answer_frame,
                                  text="Answer 3", font="Arial 10 bold",
                                  bg="red", padx=15, pady=15)
        self.answer_button3.grid(row=1, column=0)

        # answer button 4
        self.answer_button4 = Button(self.answer_frame,
                                  text="Answer 4", font="Arial 10 bold",
                                  bg="red", padx=15, pady=15)
        self.answer_button4.grid(row=1, column=1)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Pataitai")
    something = Quiz(root)
    root.mainloop()