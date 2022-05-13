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
        root.geometry("400x400")
        root.resizable(False, False)

        self.quiz_frame = Frame(width=400, height=100,
                                padx=1, pady=10, bg=background_colour)
        self.quiz_frame.grid()

        # Quiz Heading (row 0)
        self.quiz_header_label = Label(self.quiz_frame,
                                       text="Pataitai",
                                       font=("Arial", 24, "bold"),
                                       bg=background_colour,
                                       padx=140, pady=5)
        self.quiz_header_label.grid(row=1, column=2)

        # Help Button
        self.help_button = Button(self.quiz_frame, text="?",
                                  font=("Arial bold", 14),
                                  padx=5, pady=5, bg=button_colour)
        self.help_button.grid(row=0, column=3)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Pataitai")
    something = Quiz()
    root.mainloop()
