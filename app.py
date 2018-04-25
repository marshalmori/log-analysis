import re
from log import Log
from articles import Articles
from database import Database

Database.initialise(database="news",
                    user="marshal",
                    password="marshal",
                    host="localhost")

def display_title_slug():
    title_slug = Articles.get_title_slug()
    return title_slug




def three_most_popular_articles():
    articles = Log.get_three_articles()
    art = []
    slug = []
    pth = re.compile(r'\/article\/\s*')

    for article in articles:
        if pth.match(article[0]):
            # print(article[0], article[1])
            art.append((article[0], article[1]))
            slug.append((article[0].split('/'))[2])

    for i in range(3):
        print(art[i])

    # slug.sort()
    # print(slug)


three_most_popular_articles()
display_title_slug()
