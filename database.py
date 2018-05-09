#!/usr/bin/env python3
# coding=utf-8

from psycopg2 import pool


class Database():
    '''
    Esta classe cria um Pool para fazer a conexão com o banco de Dados
    Postgresql. Com basta instanciar o objeto da class e com o método
    initialise() inicializar o banco. A classe cuida da criação do cursor
    e do fechamento do banco.
    '''
    __connection_pool = None

    @classmethod
    def initialise(cls, **kwargs):
        cls.__connection_pool = pool.SimpleConnectionPool(1,
                                                          10,
                                                          **kwargs)

    @classmethod
    def get_connection(cls):
        return cls.__connection_pool.getconn()

    @classmethod
    def return_connection(cls, connection):
        Database.__connection_pool.putconn(connection)

    @classmethod
    def close_all_connection(cls):
        Database.__connection_pool.closeall()


class CursorFromConnectionFromPool:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = Database.get_connection()
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exception_type, exception_value, exception_traceback):
        if exception_value is not None:
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
        Database.return_connection(self.connection)
