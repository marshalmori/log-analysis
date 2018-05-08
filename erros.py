from database import CursorFromConnectionFromPool

class Erros:
    '''
    A classe Erros tem 4 métodos, dentre os quais 3 (create_tb_estatus_erros,
    create_tb_status_all e create_tb_all_erros) são para criar 3 views
    com o objetivo de agrupar os valores das datas e a quantidade de requisições
    HTTP, separando as que foram bem sucedidas das que tiveram erro
    (404 Not Found). Ja o método select_erros_percentagem serve para selecionar
    dentre as datas aquela que apresenta erro 404 com porcentagem maior que 1%.
    '''

    # Cria a view tb_status_erros
    @classmethod
    def create_tb_estatus_erros(cls):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('''create or replace view tb_status_erros as select
                              to_char(date(time), 'Month DD, YYYY') as mes_dia_ano
                              , count(status) as status_erros from log where
                              status='404 NOT FOUND' group by date(time)
                              order by date(time)''')

    # Cria a view tb_status_all
    @classmethod
    def create_tb_status_all(cls):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('''create or replace view tb_status_all as select
                              to_char(date(time), 'Month DD, YYYY') as m_d_a,
                              count(status) as status_all from log group by
                              date(time) order by date(time)''')

    # Cria a view tb_all_erros
    @classmethod
    def create_tb_all_erros(cls):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('''create or replace view tb_all_erros as select
                              mes_dia_ano, status_all, status_erros
                              from tb_status_all join tb_status_erros on
                              tb_status_all.m_d_a = tb_status_erros.mes_dia_ano
                              group by mes_dia_ano, status_all, status_erros
                              order by mes_dia_ano''')

    # Seleciona os dias com mais de 1% de requisições 404.
    @classmethod
    def select_erros_percentagem(cls):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('''select mes_dia_ano,
                              (cast(status_erros as float)/(status_all)*100) as
                              porcentagem from tb_all_erros where
                              (cast(status_erros as float8)/cast(status_all as float8)*100) > 1  order by mes_dia_ano''')
            err_percentagem = cursor.fetchall()
            return err_percentagem
