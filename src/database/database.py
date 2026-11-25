import mariadb
from contextlib import contextmanager

class Database:

    _instance: Database = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance : Database = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, '_initialized'): return
        self._pool = mariadb.ConnectionPool(
            user='pos_user',
            password='sana_pumasar_yana_na_second_sem',
            host='localhost',
            port=3306,
            pool_name='pos_pool',
            pool_size=5,
            database='posDB'
        )
        self._initialized = True

    @contextmanager
    def transaction(self):
        conn = self._pool.get_connection()
        try:
            conn.begin()
            yield conn
            conn.commit()
        except BaseException:
            conn.rollback()
            raise
        finally:
            conn.close()