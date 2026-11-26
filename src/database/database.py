from contextlib import contextmanager
import os
import sqlite3


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