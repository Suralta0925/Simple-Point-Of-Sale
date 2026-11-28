from models import UserModel


class Session:

    def __init__(self):
        self.user : UserModel | None = None

    def login(self, logged_user: UserModel):
        self.user = logged_user

    def logout(self):
        self.user = None