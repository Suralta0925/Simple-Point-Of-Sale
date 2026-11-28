from core import Session
from database import Database
import bcrypt
from repository import UserRepo


from models import UserModel, CreateUser, LoginUser


class UserService:

    def __init__(self, db: Database):
        self._db = db

    def _hash_password(self, password: str):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def createAccount(self, user: CreateUser):
        try:
            with self._db.transaction() as conn:
                repo = UserRepo(conn, self._db)
                if repo.create(user):
                    return "Successfully Created User"
                return 'Unable to create User'
        except BaseException as e:
            return e


    def auth_login(self, user_login:LoginUser, session: Session):
        try:
            with self._db.transaction() as conn:
                repo = UserRepo(conn, self._db)
                user : UserModel | None= repo.readOne('username', user_login.username)
                if user is None: return "Invalid Credentials"
                if user_login.password_hash != user.password_hash: return "Invalid Credentials"
                session.login(user)
        except BaseException as e:
            return e




    def updatePassword(self, user_id, plain_password):
        try:
            with self._db.transaction() as conn:
                repo = UserRepo(conn, self._db)
                if repo.readOne('user_id',user_id).must_change_password == 1:
                    # this is when where cashier updates her password
                    # set by the admin to make it private
                    repo.update(user_id, 'password_hash', self._hash_password(plain_password))
                else:
                    # if cashier forgot the password admin will set a temporary plain text password
                    # which is later to be updated and hashed on what the cashier set the password
                    repo.update(user_id, 'password_hash', plain_password)
                    repo.update(user_id, 'must_change_password', 1)
            return "Successfully updated password!"
        except BaseException as e:
            return e

