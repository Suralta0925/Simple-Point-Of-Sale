from tkinter import Frame, Label


class AdminView(Frame):

    def __init__(self, app):
        super().__init__(app.root)
        self.app =app
        Label(self, text="Admin Page").pack()

