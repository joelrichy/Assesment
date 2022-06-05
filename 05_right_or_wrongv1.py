from tkinter import *

def correct():
    root = Tk()
    #root.geometry("200x200")

    correct_frame = Frame(width=300, pady=10, bg='chartreuse')
    correct_frame.grid()

    # tempurature Converter heading (row 0)
    correct_label = Label(correct_frame, text="CORRECT", font="Arial 16 bold", bg='chartreuse', padx=10, pady=10)
    correct_label.grid(sticky='')

    next_button = Button(correct_frame, text="NEXT", font="Arial 12 bold", bg='chartreuse', padx=5, pady=5)
    next_button.grid(sticky=SE)

    root.mainloop()

def incorrect():
    root = Tk()
    #root.geometry("200x200")

    incorrect_frame = Frame(width=300, pady=10, bg='firebrick1')
    incorrect_frame.grid()

    # tempurature Converter heading (row 0)
    incorrect_label = Label(incorrect_frame, text="INCORRECT", font="Arial 16 bold", bg='firebrick1', padx=10, pady=10)
    incorrect_label.grid(sticky='')

    next_button = Button(incorrect_frame, text="NEXT", font="Arial 12 bold", bg='firebrick1', padx=5, pady=5)
    next_button.grid(sticky=SE)

    root.mainloop()

correct()
incorrect()
