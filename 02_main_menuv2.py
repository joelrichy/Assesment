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
        root.geometry("390x400")
        root.resizable(False, False)

        self.quiz_frame = Frame(width=400, height=100,
                                padx=1, pady=10, bg=background_colour)
        self.quiz_frame.grid()

        # Quiz Heading (row 0)
        self.quiz_header_label = Label(self.quiz_frame,
                                       text="Pataitai",
                                       font=("Arial", 24, "bold"),
                                       bg=background_colour,
                                       padx=5, pady=5)
        self.quiz_header_label.grid(row=1, column=2)

        # Help Button
        self.help_button = Button(self.quiz_frame, text="?",
                                  font=("Arial bold", 14),
                                  padx=10, pady=10, highlightbackground=button_colour)
        self.help_button.grid(row=0, column=3)

        #quiz_button1
        self.days_button = Button(self.quiz_frame, text="Days of the week",
                                  font=("Arial", 14), padx=10, pady=10, highlightbackground=button_colour)
        self.days_button.grid(row=3, column=1)

        #quiz_button 2
        self.days_button = Button(self.quiz_frame, text="Māori Colours",
                                  font=("Arial", 14), padx=10, pady=10, highlightbackground=button_colour)
        self.days_button.grid(row=3, column=3)

        # quiz_button 3
        self.days_button = Button(self.quiz_frame, text="Numbers 1-10",
                                  font=("Arial", 14), padx=10, pady=10, highlightbackground=button_colour)
        self.days_button.grid(row=4, column=1)

        # quiz_button 3
        self.days_button = Button(self.quiz_frame, text="Months of the year",
                                  font=("Arial", 14), padx=10, pady=10, highlightbackground=button_colour)
        self.days_button.grid(row=4, column=3)
# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Pataitai")
    something = Quiz()
    root.mainloop()
