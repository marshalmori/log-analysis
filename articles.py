from database import CursorFromConnectionFromPool

class Articles:
    def __init__(self, author, title, slug, lead, body, time, id):
        self.author = author
        self.title = title
        self.slug = slug
        self.lead = lead
        self.body = body
        self.time = time
        self.id = id

    def __repr__(self):
        return "Autor --> {}".format(self.author)


    # @classmethod
    # def get_articles(cls):
    #     with CursorFromConnectionFromPool() as cursor:
    #         cursor.execute('SELECT * FROM articles')
    #         articles_data = cursor.fetchone()
    #         return cls(author=articles_data[0],
    #                    title=articles_data[1],
    #                    slug=articles_data[2],
    #                    lead=articles_data[3],
    #                    body=articles_data[4],
    #                    time=articles_data[5],
    #                    id=articles_data[6])

    @classmethod
    def get_articles(cls):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('select title, name from articles join authors on articles.author = authors.id')
            articles_data = cursor.fetchall()
            return articles_data
