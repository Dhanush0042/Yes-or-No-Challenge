import tkinter
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Thaat anta heli")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # label
        self.score = tkinter.Label(text='score: 0', fg="white", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        self.canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(150, 125, width=280, text='Website od something', fill=THEME_COLOR,
                                                font=("arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        #
        # # button
        true_image = PhotoImage(file="Images/true.png")
        self.right_button = tkinter.Button(image=true_image, highlightthickness=0,
                                           command=self.answer_is_right)
        self.right_button.grid(column=0, row=2)
        wrong_image = PhotoImage(file="Images/false.png")
        self.wrong_button = tkinter.Button(image=wrong_image, highlightthickness=0,
                                           command=self.answer_is_wrong)
        self.wrong_button.grid(column=1, row=2)

        self.getting_questions()

        self.window.mainloop()

    def getting_questions(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score :{self.quiz.score}")
            quiz_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=quiz_text)
        else:
            self.canvas.itemconfig(self.question,text="Game Over")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")


    def answer_is_right(self):
        is_right = self.quiz.check_answer("True")
        self.check_answer(is_right)

    def answer_is_wrong(self):
        is_right = self.quiz.check_answer("False")
        self.check_answer(is_right)

    def check_answer(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.getting_questions)



