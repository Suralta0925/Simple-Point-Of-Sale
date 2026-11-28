from tkinter import Frame, Label, Button, PhotoImage, Canvas
from pathlib import Path

from config import COLORS, SIZE, Logo
base_path = Path(__file__).resolve().parents[2] / "modules" / "assets"

class _IconButtons:

    def __init__(self,parent,  icon, text, command, isActive=False):

        self.name = text
        self.active = isActive
        self.icons = {"default": PhotoImage(
                    file=base_path / f"{icon}.png"
                    ).subsample(10,10),
                    "active" : PhotoImage(
                    file=base_path /  f"{icon}_active.png"
                    ).subsample(10,10  )}
        self.btn = Button(
            parent,
            bg=COLORS['primary'] if self.active else 'white',
            fg='white' if self.active else 'black',
            compound="left",
            image=self.icons['active'] if self.active else self.icons['default'],
            activebackground=COLORS['primary'] if self.active else 'white',
            activeforeground='white' if self.active else 'black',
            text=text,
            font=('arial', SIZE['text2']),
            command=lambda : command(self),
            cursor='hand2',
            relief='flat',
            overrelief='flat',
            borderwidth=0,
            justify='left',
            anchor='w',
            highlightthickness=0,
            takefocus=False
        )
        self.btn.pack(fill='x',anchor='w' )
        self.btn.propagate(False)




    def setActive(self):
        self.active = True
        self._update()
    def setInactive(self):
        self.active=False
        self._update()

    def _update(self):
        if self.active:
            self.btn.config(
                image=self.icons["active"],
                bg=COLORS["primary"],
                fg="white",
                activebackground= COLORS['primary'],
                activeforeground='white'
                )
        else:
            self.btn.config(
                image=self.icons["default"],
                bg='white',
                fg='black',
                activebackground='white',
                activeforeground='black'
            )

class _Card:

    def __init__(self, parent, icon, key, value):
        Frame()

class Dashboard(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        Label(self, text="DashBoard View").pack()

class Users(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        Label(self, text="User View").pack()

class Products(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        Label(self, text="Products View").pack()

class Sales(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        Label(self, text="Sales View").pack()




class AdminView(Frame):

    def __init__(self, app):
        super().__init__(app.root, background='white')
        self.app =app
        self.frames = {
            "Dashboard": Dashboard,
            "Products": Products,
            "Users": Users,
            "Sales": Sales
        }

        self.sidebar = Frame(
            self,
            bg='white',
            width=320
        )
        self.sidebar.pack(fill='y', side='left')
        self.sidebar.propagate(False)
        logoWrapper = Frame(self.sidebar, background='white')
        logoWrapper.pack(fill='x', pady=(30,0),padx=50)
        Logo(logoWrapper, SIZE['subtitle']-5)
        Label(
            self.sidebar,
            text="ADMINISTRATOR",
            bg="white",
            fg=COLORS["darkerGray"],
            font=('Arial', SIZE['text'])
        ).pack(pady=(0,100))

        dashboard = _IconButtons(
            self.sidebar,
            "dashboard",
            "Dashboard",
            self.setActive,
            True
        )
        users = _IconButtons(
            self.sidebar,
            "user",
            "Users",
            self.setActive,
        )

        products = _IconButtons(
            self.sidebar,
            "product",
            "Products",
            self.setActive,
        )

        sales = _IconButtons(
            self.sidebar,
            "sale",
            "Sales",
            self.setActive
        )
        self.sidebar_btn: list['_IconButtons'] = [dashboard, users, products, sales]

        self.content= Frame(
            self,
            bg=COLORS['darkerGray']
        )
        self.content.pack(fill="both", side="right", expand=True)
        self.content.propagate(False)

        self._show_frame(Dashboard)


    def _show_frame(self, frame ):

        for widget in self.content.winfo_children():
            widget.destroy()

        frame(self.content).pack(fill='both', expand="True")

    def setActive(self, button: _IconButtons):

        for btn in self.sidebar_btn:
            if btn.active:
                if btn == button:
                    return
                btn.setInactive()
        button.setActive()
        self._show_frame(self.frames[button.name])




