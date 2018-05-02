import re
from log import Log
from articles import Articles
from database import Database
from operator import itemgetter

Database.initialise(database="news",
                    user="marshal",
                    password="marshal",
                    host="localhost")

def count_all_articles():
    articles = Log.get_all_paths_log()
    art = []
    pth = re.compile(r'\/article\/\s*')

    for article in articles:
        if pth.match(article[0]):
            art.append((article[0], article[1], article[0].split('/')[2]))
    return art

def return_three_most_articles():
    all_articles = count_all_articles()
    three_articles = []

    for i in range(3):
        three_articles.append(all_articles[i])
    return  three_articles

def all_title_slug():
    title_slug = Articles.get_title_slug()
    return title_slug

def compare_slugs():
    list_titles_slugs = all_title_slug()
    list_three_articles = return_three_most_articles()
    final_list_articles = []
    for i in range(len(list_titles_slugs)):
        for j in range(len(list_three_articles)):
            if list_titles_slugs[i][1] == list_three_articles[j][2]:
                final_list_articles.append((list_titles_slugs[i][0], list_three_articles[j][1]))
    final_list_articles = sorted(final_list_articles, key=itemgetter(1), reverse=True)
    return final_list_articles

def display_three_most_popular_articles():
    cp = compare_slugs()
    for i in range(len(cp)):
        print("\"%s\" -- %s views" %(cp[i][0], cp[i][1]))

# print(count_all_articles())
# display_title_slug()
# print(return_three_most_articles())
# print(display_title_slug())
# print(compare_slugs())
display_three_most_popular_articles()
