from tkinter import Frame, Label


class CashierView(Frame):

    def __init__(self, app):
        super.__init__(app.root)
        self.app = app
        Label(self, text="Cashier Page")
