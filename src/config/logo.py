from tkinter import Label

from config import COLORS


class Logo:

    def __init__(self, parent, size):

        for text, color in (("QUICK", COLORS["darkNavy"]), ("MART", COLORS["primary"])):
            Label(
                parent,
                text=text,
                font=('Arial',size, 'bold'),
                bg=COLORS["white"],
                fg=color,
            ).pack(side="left", anchor="nw")