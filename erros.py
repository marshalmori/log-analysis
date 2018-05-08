from database import CursorFromConnectionFromPool

class Erros:
    @classmethod
    def create_tb_estatus_erros(cls):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('''create or replace view tb_status_erros as select
                              to_char(date(time), 'Month DD, YYYY') as mes_dia_ano
                              , count(status) as status_erros from log where
                              status='404 NOT FOUND' group by date(time)
                              order by date(time)''')

    @classmethod
    def create_tb_status_all(cls):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('''create or replace view tb_status_all as select
                              to_char(date(time), 'Month DD, YYYY') as m_d_a,
                              count(status) as status_all from log group by
                              date(time) order by date(time)''')

    @classmethod
    def create_tb_all_erros(cls):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('''create or replace view tb_all_erros as select
                              mes_dia_ano, status_all, status_erros
                              from tb_status_all join tb_status_erros on
                              tb_status_all.m_d_a = tb_status_erros.mes_dia_ano
                              group by mes_dia_ano, status_all, status_erros
                              order by mes_dia_ano''')

    @classmethod
    def select_erros_percentagem(cls):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('''select mes_dia_ano,
                              (cast(status_erros as float)/(status_all)*100) as
                              porcentagem from tb_all_erros where
                              (cast(status_erros as float8)/cast(status_all as float8)*100) > 1  order by mes_dia_ano''')
            err_percentagem = cursor.fetchall()
            return err_percentagem
