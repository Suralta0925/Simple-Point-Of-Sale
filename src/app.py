from tkinter import Tk

from core import Session, ScreenManager
from database import Database
from modules import LoginView
from modules.admin import AdminView
from modules.cashier import CashierView


class App:

    def __init__(self, root: Tk):

        self.root = root
        window_width = 1300
        window_height = 900
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calculate center position
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Apply geometry
        root.geometry(f"{window_width}x{window_height}+{x}+{y}")


        self.db = Database()





        self.session = Session()

        self.router = ScreenManager(root)

        self.login_screen = LoginView
        self.admin_screen = AdminView
        self.cashier_screen = CashierView

        self.show_screen(self.login_screen)

    def show_screen(self, screen):
        self.router.show(lambda root : screen(self))

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()