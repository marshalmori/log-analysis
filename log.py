from database import CursorFromConnectionFromPool

class Log:
    def __init__(self, path, ip, method, status, time, id):
        self.path = path
        self.ip = ip
        self.method = method
        self.status = status
        self.time = time
        self.id = id

    # def __repr__(self):
    #     return "Path {} IP {} Method {} Status {} Time {}".format(
    #     self.path,
    #     self.ip,
    #     self.method,
    #     self.status,
    #     self.time
    #     )

    def __repr__(self):
        return "Path --> {}".format(self.path)

    @classmethod
    def get_log(cls):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('SELECT * FROM log')
            log_data = cursor.fetchall()
            return cls(path=log_data[0],
                       ip=log_data[1],
                       method=log_data[2],
                       status=log_data[3],
                       time=log_data[4],
                       id=log_data[5])
