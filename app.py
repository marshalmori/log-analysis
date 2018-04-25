from log import Log
import re
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

# authors = Authors.get_author()
# for author in authors:
#     print(author[0])

articles = Articles.get_three_articles()
art = []
pth = re.compile(r'\/article\/\s*')

for article in articles:
    if pth.match(article[0]):
        # print(article[0], article[1])
        art.append((article[0], article[1]))


for i in range(3):
    print(art[i])
