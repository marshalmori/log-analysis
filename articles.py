from database import CursorFromConnectionFromPool

class Articles:
    '''
    A classe Articles tem apenas o método get_articles() que através do SQL
    seleciona os três artigos mais populares de todos os tempos.
    '''
    
    # Seleciona os 3 artigos mais populares
    @classmethod
    def get_articles(cls):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('''select title, count(path) as num from articles
                              join log on articles.slug =
                              substring(path from 10) group by title order by
                              num desc limit 3''')
            articles = cursor.fetchall()
            return articles
