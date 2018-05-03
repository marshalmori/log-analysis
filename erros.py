from database import CursorFromConnectionFromPool

class Erros:
    @classmethod
    def get_log(cls):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute("select date(time), count(status) as num from log where status = '404 NOT FOUND' group by date(time) order by date(time);")
            log_data = cursor.fetchall()
            return log_data
            
# Essa é a parcial ainda
# select date(time), count(status) as num from log where status = '404 NOT FOUND' group by date(time) order by date(time);
