from abc import ABC

from database import Database
from models import UserModel, CreateUser
from repository.repository import Repository
from sqlite3 import Connection





class UserRepo(Repository):

    def __init__(self, conn: Connection, db : Database):
        self._conn = conn
        self._db = db

    def create(self, user:CreateUser):
        username = user.username
        password = user.password_hash
        first_name = user.first_name
        last_name = user.last_name
        cursor = self._conn.cursor()
        try:
            cursor.execute('insert into users(username, password, first_name, last_name) values (%s,%s,%s,%s)', (username, password, first_name, last_name))
            return cursor.rowcount > 0
        finally:
            cursor.close()

    def readOne(self, column_name, column_data) -> 'UserModel':
        cursor = self._conn.cursor()
        try:
            cursor.execute(f"""select u.user_id, u.username, u.password_hash, r.role_name, u.first_name, u.last_name, u.must_change_password 
                              from users u inner join roles r on u.role_id=r.role_id  where {column_name}=(?)""", (column_data,))
            row = self._db.fetchOne(cursor)
            user = self._db.hydrate(UserModel, row)
            return user[0] if user else None
        finally:
            cursor.close()

    def readAll(self):
        cursor = self._conn.cursor()
        try:
            cursor.execute('select user_id, username, password_hash, first_name, last_name, must_change_password from users where must_change_password = 1')
            rows = self._db.fetchAll(cursor)
            users : list[UserModel] = self._db.hydrate(UserModel, rows)
            return users
        finally:
            cursor.close()

    def update(self, table_id, column, newData):
        cursor = self._conn.cursor()
        try:
            cursor.execute("update table users set (?)=(?) where user_id = (?)", (column, newData, table_id))
            return cursor.rowcount
        finally:
            cursor.close()

    def delete(self, table_id):
        cursor = self._conn.cursor()
        try:
            cursor.execute("update table users set is_active = 0 where user_id = (?)", (table_id,))
            return cursor.rowcount
        finally:
            cursor.close()


