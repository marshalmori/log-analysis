from database import Database
from erros import Erros
from articles import Articles
from authors import Authors


Database.initialise(database="news",
                    user="marshal",
                    password="marshal",
                    host="localhost")

equal_sign = '======================================================='
hashtag_sign = '#######################################################'

log_file = open('arquivo_log.txt', 'w')

def popular_articles():
    list_articles = Articles.get_articles()
    return list_articles

def display_popular_articles():
    lt_articles = popular_articles()
    main_article_title = 'OS 3 ARTIGOS MAIS POPULARES DE TODOS OS TEMPOS'
    print(equal_sign)
    print("|    "+ main_article_title +"   |")
    print(equal_sign)
    for i in range(len(lt_articles)):
        print("| \"%s\" -- %s views  |" %(lt_articles[i][0], lt_articles[i][1]))
    print(hashtag_sign)


def popular_authors():
    Authors.create_view()
    list_authors = Authors.get_author()
    return list_authors

def display_popular_authors():
    lt_authors = popular_authors()
    main_authors_title = 'AUTORES DOS ARTIGOS MAIS POPULARES DE TODOS OS TEMPOS'
    print(equal_sign)
    print("| "+ main_authors_title +" |")
    print(equal_sign)
    for i in range(len(lt_authors)):
        print("\t\"%s\" -- %s views" %(lt_authors[i][0], lt_authors[i][1]))
    print(hashtag_sign)


def erros_percentagem():
    Erros.create_tb_estatus_erros()
    Erros.create_tb_status_all()
    Erros.create_tb_all_erros()
    list_erros = Erros.select_erros_percentagem()
    return list_erros

def display_erros_percentagem():
    lt_erros = erros_percentagem()
    print(equal_sign)
    print("| DIA QUE MAIS DE 1% DAS REQUISIÇÕES RESULTAM EM ERROS  |")
    print(equal_sign)
    for i in range (len(lt_erros)):
        print ("%s -- %.2f %% errors" %(lt_erros[i][0], float(lt_erros[i][1])))
    print(hashtag_sign)

display_popular_articles()
display_popular_authors()
display_erros_percentagem()
