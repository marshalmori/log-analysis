#!/usr/bin/env python3
# coding=utf-8

from database import CursorFromConnectionFromPool


class Authors:
    '''
    A classe Authors cria uma view chamada log_articles com valores da tabela
    articles e log, isso é feito pelo método create_view(), através do SQL que
    pode ser visto abaixo.
    Já o método get_author() seleciona  quem são os autores de artigos mais
    populares retornando uma lista com o nome do autor e a quantidade views que
    o artigo foi acessado.
    '''

    # Cria a view log_articles
    @classmethod
    def create_view(cls):
        with CursorFromConnectionFromPool() as cursor:
            return cursor.execute('''create or replace view log_articles as
                                     select author, count(path) as num from
                                     articles join log on articles.slug =
                                     substring(path from 10) group by author
                                     order by num desc limit 4''')

    # Seleciona os autores dos artigos mais populares
    @classmethod
    def get_author(cls):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('''select name, num from authors join log_articles
                              on authors.id = log_articles.author order by num
                              desc''')
            author_data = cursor.fetchall()
            return author_data
