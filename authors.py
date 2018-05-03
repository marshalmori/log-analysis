from database import CursorFromConnectionFromPool

class Authors:
    @classmethod
    def create_view(cls):
        with CursorFromConnectionFromPool() as cursor:
            return cursor.execute('''create or replace view log_articles as
                                     select author, count(path) as num from
                                     articles join log on articles.slug =
                                     substring(path from 10) group by author
                                     order by num desc limit 4''')

    @classmethod
    def get_author(cls):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('''select name, num from authors join log_articles
                              on authors.id = log_articles.author order by num
                              desc''')
            author_data = cursor.fetchall()
            return author_data
