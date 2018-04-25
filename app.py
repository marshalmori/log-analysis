from log import Log
from articles import Articles
from authors import Authors
from database import Database

Database.initialise(database="news",
                    user="marshal",
                    password="marshal",
                    host="localhost")

# logs = Log.get_log()
# print(logs)
#
# articles = Articles.get_articles()
# for article in articles:
#     print(article[0])

authors = Authors.get_author()
for author in authors:
    print(author[0])
