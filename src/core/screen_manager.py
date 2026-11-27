from tkinter import Tk, Frame


class BaseScreen(Frame):
    def __init__(self, root: Tk):
        super().__init__(root)


class ScreenManager:

    def __init__(self, root: Tk):
        self.root : Tk = root
        self.current_screen : BaseScreen | None = None

    def show(self, screen: type[BaseScreen]):
        if self.current_screen:
            self.current_screen.destroy()

        self.current_screen = screen(self.root)
        self.current_screen.pack(fill="both", expand=True)
