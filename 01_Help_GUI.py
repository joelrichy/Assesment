from tkinter import *
from functools import partial  # To prevent unwanted windows


class Quiz:
    def __init__(self):

        #  formatting variables...
        background_colour = "white"

        # Converter Main Screen GUI
        self.quiz_frame = Frame(width=300, height=300,
                                     padx=10, pady=10, bg=background_colour)
        self.quiz_frame.grid()

        # Tempurature Conversion Heading (row 0)
        self.quiz_header_label = Label(self.quiz_frame,
                                          text="Temperature Converter",
                                          font=("Arial", 16, "bold"),
                                          bg=background_colour,
                                          padx=10, pady=10)
        self.quiz_header_label.grid(row=0)

        # Help Button (row 1)
        self.help_button = Button(self.quiz_frame, text="Help",
                                  font=("Arial", 14),
                                  padx=10, pady=10,
                                  command=self.help)
        self.help_button.grid(row=1)

    def help(self):
        print("You asked for help :)")
        get_help = Help(self)
        get_help.help_text.configure(text="Help text goes here")


class Help:
    def __init__(self, partner):
        background = "white"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # set up child window (ie help box)
        self.help_box = Toplevel()

        # if users press cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help,
                                                           partner))
        # set up Gui Frame
        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid()

        # set up Help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help/Instructions",
                                 font=("Arial", 24, "bold"), bg=background)
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text="", justify=LEFT,
                               width=40, bg=background, wrap=250)
        self.help_text.grid(row=1)

        # dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss",
                                  width=10, bg="orange", font="Ariel 10 bold",
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Pataitai")
    something = Quiz()
    root.mainloop()
