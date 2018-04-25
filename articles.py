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
        return "Título --> {}, Slug --> {}".format(self.title, self.slug)

    @classmethod
    def get_title_slug(cls):
        with CursorFromConnectionFromPool() as cursor:
            # cursor.execute("select path, count (*) as num from log group by ip;")
            cursor.execute("select title, slug from articles")
            title_slug_data = cursor.fetchall()
            return title_slug_data
