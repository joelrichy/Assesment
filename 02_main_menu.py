from tkinter import *
from functools import partial  # to prevent unwanted additional windows
import random


class Quiz:
    def __init__(self, parent):
        # formatting variables
        background_colour = "white"
        button_colour = "red"

        # converter frame
        self.quiz_frame = Frame(width=300, bg=background_colour, pady=10)
        self.quiz_frame.grid()

        # tempurature Converter heading (row 0)
        self.title_label = Label(self.quiz_frame,
                                        text="Maori Days of the Week",
                                        font="Arial 16 bold",
                                        bg=background_colour,
                                        padx=10, pady=10)
        self.title_label.grid(row=0)

        # user instructions (row 1)
        self.temp_instructions_label = Label(self.quiz_frame,
                                             text="Press START to start quiz. Make sure to be sure of your answer"
                                                  "before pressing the button",
                                             font="Arial 10 italic", wrap=250,
                                             justify=CENTER, bg=background_colour,
                                             padx=10, pady=10)
        self.temp_instructions_label.grid(row=1)

        # conversion buttons frame (row 3) orchid3 / khaki1
        self.quiz_button_frame = Frame(self.quiz_frame)
        self.quiz_button_frame.grid(row=3, pady=10)

        self.quiz_button = Button(self.quiz_button_frame,
                                  text="START", font="Arial 10 bold",
                                  bg="red", padx=10, pady=10)
        self.quiz_button.grid(row=0, column=0)

        #  History/Help button frame (row 5)
        self.hist_help_frame = Frame(self.quiz_frame)
        self.hist_help_frame.grid(row=5, pady=10)

        self.calc_hist_button = Button(self.hist_help_frame,
                                       text="History",
                                       font="Arial 12 bold",
                                       width=10)
        self.calc_hist_button.grid(row=0, column=0)

        self.help_button = Button(self.hist_help_frame,
                                  text="Help", font="Arial 12 bold",
                                  width=10, padx=5)
        self.help_button.grid(row=0, column=1)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Pataitai")
    something = Quiz(root)
    root.mainloop()
