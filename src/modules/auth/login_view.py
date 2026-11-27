from tkinter import Frame, ttk, Tk, Label

from config import COLORS, SIZE


class LoginView(Frame):
    def __init__(self, app):
        super().__init__(app.root)

        self.app = app

        # LEFT FRAME
        left_frame = Frame(self, bg=COLORS['primary'])
        left_frame.place(
            relx=0,
            rely=0,
            relwidth=0.50,
            relheight=1.0
        )
        content = Frame(left_frame, bg=COLORS['primary'])
        content.pack(fill="both", expand=True, padx=40, pady=40)

        Label(
            content,
            text="RETAIL POINT OF SALE",
            font=("Arial", SIZE['text'], 'bold'),
            bg=COLORS['primary'],
            fg=COLORS['white'],
        ).pack(anchor='w', pady=(0,10))
        Label(
            content,
            text="Every sale,\ncounted.",
            bg=COLORS['primary'],
            fg=COLORS['white'],
            font=('Arial', SIZE['title'], "bold"),
            justify="left"
        ).pack(anchor='w', pady=(0,20))


        Frame(
            content,
            bg=COLORS['secondary'],
            height=4,
            width=100,
        ).pack(anchor='w',
               pady=(2,30)
        )

        Label(
            content,
            text="Fast checkouts for your cashiers. Clear numbers\nfor your business.",
            bg=COLORS["primary"],
            fg=COLORS['white'],
            font=("Arial", SIZE['text']),
            justify='left',
            anchor='w'
        ).pack(anchor='w')

        #TODO: Finish this


        #Right Frame where login form is

        right_frame = Frame(self, bg=COLORS['lightGray'])
        right_frame.place(
            relx=0.50,
            rely=0,
            relheight=1.0,
            relwidth=0.5
        )

        login_form = Frame(right_frame, bg=COLORS['white'],  highlightbackground=COLORS['borderGray'], highlightthickness=2)
        login_form.place(
            relwidth=0.8,
            relheight=0.8,
            rely=0.5,
            relx=0.5,
            anchor="center",
            bordermode='outside'
        )
        form = Frame(login_form, bg=COLORS['white'])
        form.pack(fill="both", expand=True, padx=40, pady=40)

        title_frame = Frame(form, bg=COLORS['white'])
        title_frame.pack(anchor='w')

        Label(
            title_frame,
            text='QUICK',
            bg=COLORS['white'],
            fg=COLORS['darkNavy'],
            font=('Arial', SIZE['subtitle'], 'bold'),
        ).pack(side='left', anchor='nw')
        Label(
            title_frame,
            text='MART',
            bg=COLORS['white'],
            fg=COLORS['primary'],
            font=('Arial', SIZE['subtitle'], 'bold')
        ).pack(side='left', anchor='nw')

        Label(
            form,
            text="POINT OF SALE",
            bg=COLORS['white'],
            fg=COLORS['darkNavy'],
            font=('Arial', SIZE['smaller'], 'bold'),
            justify='left'
        ).pack(padx=10,pady=(10,60),anchor='w')

        Frame(
            form,
            bg=COLORS['borderGray'],
            height=2,
            width=500
        ).pack(anchor='w',
               pady=(2, 30)
               )
