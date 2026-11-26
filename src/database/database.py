from contextlib import contextmanager
import os
import sqlite3

from pydantic import BaseModel


class Database:

    _instance: Database = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance : Database = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, '_initialized'): return
        folder = os.path.dirname(os.path.abspath(__file__))
        self._db_path = os.path.join(folder, 'posDB.db')
        sql_path = os.path.join(folder, 'posDB.sql')

        first_time = not os.path.exists(self._db_path)

        if first_time:
            conn = sqlite3.connect(self._db_path)
            with open(sql_path, 'r', encoding='utf8') as f:
                conn.executescript(f.read())
            conn.commit()
            conn.close()

        self._initialized = True

    @contextmanager
    def transaction(self):
        conn  = sqlite3.connect(self._db_path)
        conn.execute('PRAGMA foreign_keys = ON')
        conn.row_factory = sqlite3.Row
        try:
            yield conn
            conn.commit()
        except BaseException:
            conn.rollback()
            raise
        finally:
            conn.close()

    def fetchAll(self, cursor : sqlite3.Cursor):
        cols = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
        return [dict(zip(cols, row)) for row in rows]

    def fetchOne(self, cursor: sqlite3.Cursor):
        cols = [col[0] for col in cursor.description]
        row = cursor.fetchone()
        return dict(zip(cols, row))

    def hydrate(self, model: type[BaseModel], rows: list[dict] | dict):
        return [model.model_validate(row) for row in rows]