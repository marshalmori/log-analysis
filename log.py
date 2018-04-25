from database import CursorFromConnectionFromPool

class Log:
    def __init__(self, path, ip, method, status, time, id):
        self.path = path
        self.ip = ip
        self.method = method
        self.status = status
        self.time = time
        self.id = id

    def __repr__(self):
        return "Path --> {}".format(self.path)

    @classmethod
    def get_three_articles(cls):
        with CursorFromConnectionFromPool() as cursor:
            # cursor.execute("select path, count (*) as num from log group by ip;")
            cursor.execute("select path, count(path) as num from log group by path order by num desc")
            three_articles_data = cursor.fetchall()
            return three_articles_data
