# from tkinter import Frame, ttk, Tk, Label, Entry, Button
#
# from config import COLORS, SIZE
# from models import LoginUser
# from service.user_service import UserService
#
#
# class LoginView(Frame):
#     def __init__(self, app):
#         super().__init__(app.root)
#
#         self.app = app
#
#         # LEFT FRAME
#         left_frame = Frame(self, bg=COLORS['primary'])
#         left_frame.place(
#             relx=0,
#             rely=0,
#             relwidth=0.50,
#             relheight=1.0
#         )
#         content = Frame(left_frame, bg=COLORS['primary'])
#         content.pack(fill="both", expand=True, padx=40, pady=40)
#
#         Label(
#             content,
#             text="RETAIL POINT OF SALE",
#             font=("Arial", SIZE['text'], 'bold'),
#             bg=COLORS['primary'],
#             fg=COLORS['white'],
#         ).pack(anchor='w', pady=(0,10))
#         Label(
#             content,
#             text="Every sale,\ncounted.",
#             bg=COLORS['primary'],
#             fg=COLORS['white'],
#             font=('Arial', SIZE['title'], "bold"),
#             justify="left"
#         ).pack(anchor='w', pady=(0,20))
#
#
#         Frame(
#             content,
#             bg=COLORS['secondary'],
#             height=4,
#             width=100,
#         ).pack(anchor='w',
#                pady=(2,30)
#         )
#
#         Label(
#             content,
#             text="Fast checkouts for your cashiers. Clear numbers\nfor your business.",
#             bg=COLORS["primary"],
#             fg=COLORS['white'],
#             font=("Arial", SIZE['text']),
#             justify='left',
#             anchor='w'
#         ).pack(anchor='w')
#
#         #TODO: Finish this
#
#
#         #Right Frame where login form is
#
#         right_frame = Frame(self, bg=COLORS['lightGray'])
#         right_frame.place(
#             relx=0.50,
#             rely=0,
#             relheight=1.0,
#             relwidth=0.5
#         )
#
#         login_form = Frame(right_frame, bg=COLORS['white'],  highlightbackground=COLORS['borderGray'], highlightthickness=2)
#         login_form.place(
#             relwidth=0.8,
#             relheight=0.8,
#             rely=0.5,
#             relx=0.5,
#             anchor="center",
#             bordermode='outside'
#         )
#         form = Frame(login_form, bg=COLORS['white'])
#         form.pack(fill="both", expand=True, padx=40, pady=40)
#
#         title_frame = Frame(form, bg=COLORS['white'])
#         title_frame.pack(anchor='w')
#
#         Label(
#             title_frame,
#             text='QUICK',
#             bg=COLORS['white'],
#             fg=COLORS['darkNavy'],
#             font=('Arial', SIZE['subtitle'], 'bold'),
#         ).pack(side='left', anchor='nw')
#         Label(
#             title_frame,
#             text='MART',
#             bg=COLORS['white'],
#             fg=COLORS['primary'],
#             font=('Arial', SIZE['subtitle'], 'bold')
#         ).pack(side='left', anchor='nw')
#
#         Label(
#             form,
#             text="POINT OF SALE",
#             bg=COLORS['white'],
#             fg=COLORS['darkNavy'],
#             font=('Arial', SIZE['smaller'], 'bold'),
#             justify='left'
#         ).pack(padx=10,pady=(10,60),anchor='w')
#
#         Frame(
#             form,
#             bg=COLORS['borderGray'],
#             height=2,
#             width=500
#         ).pack(anchor='w',
#                pady=(2, 30))
#
#         Label(
#             form,
#             bg=COLORS['white'],
#             foreground=COLORS['darkNavy'],
#             text='Sign in to your account',
#             font=('Arial', SIZE['text2'], 'bold')
#         ).pack(anchor='w')
#         Label(
#             form,
#             bg=COLORS['white'],
#             foreground=COLORS['darkerGray'],
#             text='Use the credentials issued by your administrator.',
#             font=('Arial', SIZE['smaller'])
#         ).pack(anchor='w', pady=(0,30))
#
#         login = Frame(form, bg=COLORS['white'])
#         login.pack(anchor='w')
#         Label(
#             login,
#             text="Username",
#             fg=COLORS['darkerGray'],
#             bg='white',
#             font= ('Arial', SIZE['smaller'], 'bold')
#         ).pack(anchor='w')
#
#         username_container = Frame(
#             form,
#             bg=COLORS['white'],
#             highlightthickness=2,
#             highlightcolor=COLORS['primary']
#             )
#
#         username_container.pack(fill='x', pady=10)
#
#         self.username = Entry(
#             username_container,
#             font=('Arial', SIZE['smaller']),
#             bg= COLORS['white'],
#             fg= COLORS['darkerGray'],
#             relief='flat',
#             bd=0,
#             highlightthickness=0,
#             borderwidth=0
#         )
#         self.username.pack(fill='both', padx=10, pady=10)
#
#         Label(
#             form,
#             text="Password",
#             fg=COLORS['darkerGray'],
#             bg='white',
#             font=('Arial', SIZE['smaller'], 'bold')
#         ).pack(anchor='w')
#
#         password_container = Frame(
#             form,
#             bg=COLORS['white'],
#             highlightthickness=2,
#             highlightcolor=COLORS['primary']
#         )
#
#         password_container.pack(fill='x', pady=(10,30))
#
#         self.password = Entry(
#             password_container,
#             font=('Arial', SIZE['smaller']),
#             bg=COLORS['white'],
#             fg=COLORS['darkerGray'],
#             relief='flat',
#             bd=0,
#             highlightthickness=0,
#             borderwidth=0,
#             show='*'
#         )
#         self.password.pack(fill='both', padx=10, pady=10)
#
#         login_button = Button(
#             form,
#             text='Sign In',
#             font=('Arial', SIZE['smaller']),
#             bg=COLORS['primary'],
#             fg=COLORS['white'],
#             activebackground=COLORS['secondary'],
#             activeforeground=COLORS['white'],
#             relief='flat',
#             bd=0,
#             padx=20,
#             pady=10,
#             cursor='hand2',
#             command=self.login
#         )
#
#         login_button.pack(fill='x', pady=10)
#
#         login_button.bind(
#             "<Enter>",
#             lambda e: login_button.config(bg=COLORS['secondary'])
#         )
#
#         login_button.bind(
#             "<Leave>",
#             lambda e: login_button.config(bg=COLORS['primary'])
#         )
#
#     def login(self):
#         username = self.username.get()
#         password = self.password.get()
#         login = LoginUser(username=username, password_hash=password)
#         service = UserService(self.app.db)
#         a = service.auth_login(login)
#         print(a)
#
#
#


from tkinter import Button, Entry, Frame, Label

from config import COLORS, SIZE
from models import LoginUser
from service.user_service import UserService

FONT_FAMILY = "Arial"
PANEL_PAD = 40
ACCENT_BAR_SIZE = (100, 4)  # (width, height)
ERROR_FG = "#C0392B"


def font(size, bold=False):
    return (FONT_FAMILY, size, "bold") if bold else (FONT_FAMILY, size)


class LoginView(Frame):
    def __init__(self, app):
        super().__init__(app.root)
        self.app = app
        self.users = UserService(app.db)

        # Two equal-width columns: brand panel | login form
        self.columnconfigure((0, 1), weight=1, uniform="half")
        self.rowconfigure(0, weight=1)

        self._build_brand_panel().grid(row=0, column=0, sticky="nsew")
        self._build_form_panel().grid(row=0, column=1, sticky="nsew")

        self.username.focus_set()

    # ------------------------------------------------------------------
    # Brand panel (left)
    # ------------------------------------------------------------------
    def _build_brand_panel(self):
        panel = Frame(self, bg=COLORS["primary"])
        content = Frame(panel, bg=COLORS["primary"])
        content.pack(fill="both", expand=True, padx=PANEL_PAD, pady=PANEL_PAD)

        Label(
            content,
            text="RETAIL POINT OF SALE",
            font=font(SIZE["text"], bold=True),
            bg=COLORS["primary"],
            fg=COLORS["white"],
        ).pack(anchor="w", pady=(0, 10))

        Label(
            content,
            text="Every sale,\ncounted.",
            font=font(SIZE["title"], bold=True),
            bg=COLORS["primary"],
            fg=COLORS["white"],
            justify="left",
        ).pack(anchor="w", pady=(0, 20))

        width, height = ACCENT_BAR_SIZE
        Frame(
            content,
            bg=COLORS["secondary"],
            width=width,
            height=height,
        ).pack(anchor="w", pady=(2, 30))

        Label(
            content,
            text="Fast checkouts for your cashiers. Clear numbers\nfor your business.",
            font=font(SIZE["text"]),
            bg=COLORS["primary"],
            fg=COLORS["white"],
            justify="left",
        ).pack(anchor="w")

        return panel

    # ------------------------------------------------------------------
    # Form panel (right)
    # ------------------------------------------------------------------
    def _build_form_panel(self):
        panel = Frame(self, bg=COLORS["lightGray"])

        card = Frame(
            panel,
            bg=COLORS["white"],
            highlightbackground=COLORS["borderGray"],
            highlightthickness=2,
        )
        card.place(
            relx=0.5,
            rely=0.5,
            relwidth=0.8,
            relheight=0.8,
            anchor="center",
            bordermode="outside",
        )

        form = Frame(card, bg=COLORS["white"])
        form.pack(fill="both", expand=True, padx=PANEL_PAD, pady=PANEL_PAD)

        self._build_header(form)
        self._build_fields(form)
        self._build_actions(form)

        return panel

    def _build_header(self, form):
        title = Frame(form, bg=COLORS["white"])
        title.pack(anchor="w")

        for text, color in (("QUICK", COLORS["darkNavy"]), ("MART", COLORS["primary"])):
            Label(
                title,
                text=text,
                font=font(SIZE["subtitle"], bold=True),
                bg=COLORS["white"],
                fg=color,
            ).pack(side="left", anchor="nw")

        Label(
            form,
            text="POINT OF SALE",
            font=font(SIZE["smaller"], bold=True),
            bg=COLORS["white"],
            fg=COLORS["darkNavy"],
            justify="left",
        ).pack(anchor="w", padx=10, pady=(10, 60))

        Frame(form, bg=COLORS["borderGray"], height=2).pack(fill="x", pady=(2, 30))

        Label(
            form,
            text="Sign in to your account",
            font=font(SIZE["text2"], bold=True),
            bg=COLORS["white"],
            fg=COLORS["darkNavy"],
        ).pack(anchor="w")

        Label(
            form,
            text="Use the credentials issued by your administrator.",
            font=font(SIZE["smaller"]),
            bg=COLORS["white"],
            fg=COLORS["darkerGray"],
        ).pack(anchor="w", pady=(0, 30))

    def _build_fields(self, form):
        self.username = self._labeled_entry(form, "Username")
        self.password = self._labeled_entry(form, "Password", show="*", pady=(10, 20))

        # Pressing Enter in either field submits the form
        for entry in (self.username, self.password):
            entry.bind("<Return>", lambda _e: self.login())

    def _build_actions(self, form):
        self.error_label = Label(
            form,
            text="",
            font=font(SIZE["smaller"]),
            bg=COLORS["white"],
            fg=ERROR_FG,
            anchor="w",
            justify="left",
        )
        self.error_label.pack(fill="x", pady=(0, 10))

        self._make_button(form, "Sign In", self.login).pack(fill="x", pady=10)

    # ------------------------------------------------------------------
    # Reusable widget helpers
    # ------------------------------------------------------------------
    def _labeled_entry(self, parent, label, show=None, pady=10):
        Label(
            parent,
            text=label,
            font=font(SIZE["smaller"], bold=True),
            bg=COLORS["white"],
            fg=COLORS["darkerGray"],
        ).pack(anchor="w")

        box = Frame(
            parent,
            bg=COLORS["white"],
            highlightthickness=2,
            highlightbackground=COLORS["borderGray"],  # unfocused ring
            highlightcolor=COLORS["primary"],          # focused ring
        )
        box.pack(fill="x", pady=pady)

        entry = Entry(
            box,
            font=font(SIZE["smaller"]),
            bg=COLORS["white"],
            fg=COLORS["darkerGray"],
            relief="flat",
            bd=0,
            highlightthickness=0,
            show=show,
        )
        entry.pack(fill="both", padx=10, pady=10)
        return entry

    def _make_button(self, parent, text, command):
        button = Button(
            parent,
            text=text,
            font=font(SIZE["smaller"]),
            bg=COLORS["primary"],
            fg=COLORS["white"],
            activebackground=COLORS["secondary"],
            activeforeground=COLORS["white"],
            relief="flat",
            bd=0,
            padx=20,
            pady=10,
            cursor="hand2",
            command=command,
        )
        button.bind("<Enter>", lambda _e: button.config(bg=COLORS["secondary"]))
        button.bind("<Leave>", lambda _e: button.config(bg=COLORS["primary"]))
        return button

    # ------------------------------------------------------------------
    # Behavior
    # ------------------------------------------------------------------
    def _show_error(self, message):
        self.error_label.config(text=message)

    def login(self):
        username = self.username.get().strip()
        password = self.password.get()

        if not username or not password:
            self._show_error("Enter your username and password.")
            return

        credentials = LoginUser(username=username, password_hash=password)
        user = self.users.auth_login(credentials, self.app.session)

        if user:
            self._show_error(user)
            self.password.delete(0, "end")
            self.password.focus_set()
            return

        self._show_error("")

        #todo: make sure to add the must change password screen first



        if self.app.session.user.role_name == 'admin':
            self.app.show_screen(self.app.admin_screen)
        else:
            self.app.show_screen(self.app.cashier_screen)
