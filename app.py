from database import Database
from erros import Erros
from articles import Articles
from authors import Authors


Database.initialise(database="news",
                    user="marshal",
                    password="marshal",
                    host="localhost")

def popular_articles():
    list_articles = Articles.get_articles()
    return list_articles

def display_popular_articles():
    lt_articles = popular_articles()
    print("=======================================================")
    print("|    OS 3 ARTIGOS MAIS POPULARES DE TODOS OS TEMPOS   |")
    print("=======================================================")
    for i in range(len(lt_articles)):
        print("| \"%s\" -- %s views  |" %(lt_articles[i][0], lt_articles[i][1]))
    print("#######################################################")


def popular_authors():
    Authors.create_view()
    list_authors = Authors.get_author()
    return list_authors

def display_popular_authors():
    lt_authors = popular_authors()
    print("=========================================================")
    print("| AUTORES DOS ARTIGOS MAIS POPULARES DE TODOS OS TEMPOS |")
    print("=========================================================")
    for i in range(len(lt_authors)):
        print("\t\"%s\" -- %s views" %(lt_authors[i][0], lt_authors[i][1]))
    print("#########################################################")

display_popular_articles()
display_popular_authors()
