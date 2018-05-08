from database import Database
from erros import Erros
from articles import Articles
from authors import Authors

Database.initialise(database="news",
                    user="<seu_usuario>",
                    password="<sua_senha>",
                    host="localhost")

equal_sign = '======================================================='
hashtag_sign = '#######################################################'
main_article_title = 'OS 3 ARTIGOS MAIS POPULARES DE TODOS OS TEMPOS'
main_authors_title = 'AUTORES DOS ARTIGOS MAIS POPULARES DE TODOS OS TEMPOS'
main_title_err_por = 'DIA(S) QUE MAIS DE 1% DAS REQUISIÇÕES RESULTAM EM ERROS'

def popular_articles():
    return Articles.get_articles()

def display_popular_articles():
    lt_articles = popular_articles()
    print(equal_sign)
    print("|    "+ main_article_title +"   |")
    print(equal_sign)
    for i in range(len(lt_articles)):
        print("| \"%s\" -- %s views  |" %(lt_articles[i][0], lt_articles[i][1]))
    print(hashtag_sign)

def popular_authors():
    Authors.create_view()
    return Authors.get_author()

def display_popular_authors():
    lt_authors = popular_authors()
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
    return Erros.select_erros_percentagem()

def display_erros_percentagem():
    lt_erros = erros_percentagem()
    print(equal_sign)
    print("| "+ main_title_err_por +" |")
    print(equal_sign)
    for i in range (len(lt_erros)):
        print ("%s -- %.2f %% errors" %(lt_erros[i][0], float(lt_erros[i][1])))
    print(hashtag_sign)

def generate_log_file():
    lt_articles = popular_articles()
    lt_authors = popular_authors()
    lt_erros = erros_percentagem()
    log_file = open('log_file.txt', 'w')

    log_file.write(main_article_title + '\n')
    for i in range(len(lt_articles)):
        log_file.write(lt_articles[i][0] + ' -- ')
        log_file.write(str(lt_articles[i][1]) + ' views\n')

    log_file.write('\n\n' + main_authors_title + '\n')
    for i in range(len(lt_authors)):
        log_file.write(lt_authors[i][0] + ' -- ')
        log_file.write(str(lt_authors[i][1]) + ' views\n')

    log_file.write('\n\n' + main_title_err_por + '\n')
    for i in range(len(lt_erros)):
        log_file.write(lt_erros[i][0] + ' -- ')
        log_file.write((str(lt_erros[i][1])[0:4]) + ' %\n')

    log_file.close()

display_popular_articles()
display_popular_authors()
display_erros_percentagem()
generate_log_file()
