from abc import ABC

from database import Database
from models import UserModel
from repository.repository import Repository
import bcrypt
from sqlite3 import Connection


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
            cursor.execute('insert into users(username, password, first_name, last_name) values (%s,%s,%s,%s)', (username, password, first_name, last_name))
            return cursor.rowcount > 0
        finally:
            cursor.close()

    def readOne(self, username):
        cursor = self._conn.cursor()
        try:
            cursor.execute('select password from users where username=%s', (username,))
            row = self._db.fetchOne(cursor)
            user = self._db.hydrate(UserModel, row)
            return user[0]
        finally:
            cursor.close()

    def readAll(self):
        cursor = self._conn.cursor()
        try:
            cursor.execute('select username, password_hash, first_name, last_name from users')
            rows = self._db.fetchAll(cursor)
            users : list[UserModel] = self._db.hydrate(UserModel, rows)
            return users
        finally:
            cursor.close()

    def update(self, table_id, data):pass

    def delete(self, table_id):pass


