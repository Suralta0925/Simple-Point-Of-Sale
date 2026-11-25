from database import Database
from repository.repository import Repository
import bcrypt
from mariadb import Connection


def _hash_password(password: str):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class UserRepo(Repository):

    def __init__(self, conn: Connection, db : Database):
        self._conn = conn
        self._db = db

    def create(self, **kwargs):
        username = kwargs['username']
        password = _hash_password(kwargs['password'])
        first_name = kwargs['first_name']
        last_name = kwargs['last_name']
        cursor = self._conn.cursor()
        try:
            cursor.execute('insert into users(username, password, first_name, last_name) values (%s,%s,%s,%s)', (username, password.decode('utf-8'), first_name, last_name))
            return cursor > 0
        finally:
            cursor.close()

    def readOne(self, username):
        cursor = self._conn.cursor()
        try:
            cursor.execute('select password from users where username=%s', (username,))
            user = cursor.fetchone()
            return user
        finally:
            cursor.close()


