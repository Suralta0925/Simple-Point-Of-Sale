from tkinter import Tk

from core import Session, ScreenManager
from modules import LoginView


class App:

    def __init__(self, root: Tk):

        self.root = root
        self.root.geometry("1300x900")






        self.session = Session()

        self.router = ScreenManager(root)

        self.login_screen = LoginView

        self.show_screen(self.login_screen)

    def show_screen(self, screen):
        self.router.show(lambda root : screen(self))

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()