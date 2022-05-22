from tkinter import *
from functools import partial  # to prevent unwanted additional windows
import random

class Questions:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer



question1 = Questions("1", "2")
question2 = Questions("3", "Hello")

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Questions")
    something = Questions(root)
    root.mainloop()