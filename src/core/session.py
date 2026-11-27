from models import UserModel


class Session:

    def __init__(self):
        self._user : UserModel | None = None

    def login(self, logged_user: UserModel):
        self._user = logged_user

    def logout(self):
        self._user = None