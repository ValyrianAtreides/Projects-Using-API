from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface():
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain

        self.window=Tk()
        self.window.title("Quizzler")

        self.window.config(padx=20,pady=20,bg=THEME_COLOR,height=500)


        self.canvas=Canvas(width=300,height=250,bg="white")
        self.question_text=self.canvas.create_text(
            150,125,
            text="Hello",
            fill=THEME_COLOR,
            font=("Arial",20,"italic"),
            width=280
        )
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        self.score_label=Label(text="Score:0",fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)

        right_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.green_button = Button(image=right_image, highlightthickness=0,command=self.right_answer)
        self.green_button.grid(column=0, row=2)
        self.red_button = Button(image=false_image, highlightthickness=0,command=self.false_answer)
        self.red_button.grid(column=1,row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="Quiz Ended")
            self.green_button.config(state="disabled")
            self.green_button.config(state="disabled")
    def right_answer(self):
        self.feed_back(self.quiz.check_answer("True"))
    def false_answer(self):
        self.feed_back(self.quiz.check_answer("False"))

    def feed_back(self,is_right):
        if is_right:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)
