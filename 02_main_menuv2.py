# 02_main_menu version 2
# main menu of quiz
# quiz buttons added
# 6/5/22

from tkinter import *


class Quiz:
    def __init__(self):

        #  formatting variables...
        background_colour = "white"
        button_colour = "red"

        # Quiz Main Menu GUI

        self.quiz_frame = Frame(root, width=400, height=100,
                                padx=1, pady=1, bg=background_colour)
        self.quiz_frame.grid()

        # Quiz Heading (row 0)
        self.quiz_header_label = Label(self.quiz_frame,
                                       text="Pataitai",
                                       font=("Arial", 24, "bold"),
                                       bg=background_colour,
                                       padx=5, pady=5)
        self.quiz_header_label.grid(row=1,)


        # Help Button
        self.help_button = Button(self.quiz_frame, text="?",
                                  font=("Arial bold", 14),
                                  padx=10, pady=10, highlightbackground=button_colour)
        self.help_button.grid(row=0, sticky=E)

        # Button frame
        self.button_frame = Frame(self.quiz_frame)
        self.button_frame.grid(row=2)

        # quiz_button1
        self.days_button = Button(self.button_frame, text=" Maori Days ",
                                  font=("Arial", 14), padx=10, pady=10, highlightbackground=button_colour)
        self.days_button.grid(row=0, column=0, padx=5)

        # quiz_button 2
        self.colours_button = Button(self.button_frame, text="Māori Colours",
                                  font=("Arial", 14), padx=10, pady=10, highlightbackground=button_colour)
        self.colours_button.grid(row=0, column=1, padx=5)

        # quiz_button 3
        self.numbers_button = Button(self.button_frame, text="Numbers 1-10",
                                  font=("Arial", 14), padx=10, pady=10, highlightbackground=button_colour)
        self.numbers_button.grid(row=1, column=0, padx=5)

        # quiz_button 3
        self.month_button = Button(self.button_frame, text="Maori Months ",
                                  font=("Arial", 14), padx=10, pady=10, highlightbackground=button_colour)
        self.month_button.grid(row=1, column=1, padx=5)
# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Pataitai")
    something = Quiz()
    root.mainloop()
