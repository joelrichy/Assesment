# 02_main_menu version 1
# main menu of quiz
# 6/5/22

from tkinter import *


class Quiz:
    def __init__(self):

        #  formatting variables...
        background_colour = "white"
        button_colour = "red"

        # Quiz Main Menu GUI
        self.quiz_frame = Frame(width=100, height=100,
                                padx=100, pady=100, bg=background_colour)
        self.quiz_frame.grid()

        # Quiz Heading (row 0)
        self.quiz_header_label = Label(self.quiz_frame,
                                       text="Pataitai",
                                       font=("Arial", 16, "bold"),
                                       bg=background_colour,
                                       padx=10, pady=10)
        self.quiz_header_label.grid(row=1, sticky=N)

        # Help Button
        self.help_button = Button(self.quiz_frame, text="?",
                                  font=("Arial bold", 14),
                                  padx=5, pady=5, bg=button_colour)
        self.help_button.grid(row=0, sticky=NE)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Pataitai")
    something = Quiz()
    root.mainloop()
