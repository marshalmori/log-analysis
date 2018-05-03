from database import CursorFromConnectionFromPool

class Articles:
    @classmethod
    def get_articles(cls):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('''select title, count(path) as num from articles
                              join log on articles.slug =
                              substring(path from 10) group by title order by
                              num desc limit 3''')
            articles = cursor.fetchall()
            return articles
